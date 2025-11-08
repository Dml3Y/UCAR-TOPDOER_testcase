from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from .database import SessionLocal, engine
from . import models, schemas, crud

# Создаем таблицы в БД
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Incident API",
    description="API для учета инцидентов",
    version="1.1.2"
)

# Зависимость для получения сессии БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/incidents", response_model=schemas.Incident)
def create_incident(incident: schemas.IncidentCreate, db: Session = Depends(get_db)):
    """
    Создание нового инцидента
    """
    return crud.create_incident(db=db, incident=incident)


@app.get("/incidents", response_model=List[schemas.Incident])
def read_incidents(
    status: Optional[str] = Query(None, description="Фильтр по статусу"),
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    Получение списка инцидентов с возможностью фильтрации по статусу
    """
    incidents = crud.get_incidents(db, status=status, skip=skip, limit=limit)
    return incidents


@app.get("/incidents/{incident_id}", response_model=schemas.Incident)
def read_incident(incident_id: int, db: Session = Depends(get_db)):
    """
    Получение инцидента по ID
    """
    db_incident = crud.get_incident(db, incident_id=incident_id)
    if db_incident is None:
        raise HTTPException(status_code=404, detail="Инцидент не найден")
    return db_incident


@app.patch("/incidents/{incident_id}", response_model=schemas.Incident)
def update_incident_status(
    incident_id: int,
    status_update: schemas.IncidentStatusUpdate,
    db: Session = Depends(get_db)
):
    """
    Обновление статуса инцидента
    """
    db_incident = crud.update_incident_status(
        db, incident_id=incident_id, status=status_update.status
    )
    if db_incident is None:
        raise HTTPException(status_code=404, detail="Инцидент не найден")
    return db_incident


@app.get("/")
def root():
    return {"message": "Incident API Service"}