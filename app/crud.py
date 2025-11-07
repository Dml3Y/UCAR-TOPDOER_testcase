from sqlalchemy.orm import Session
from typing import List, Optional
from . import models, schemas


def create_incident(db: Session, incident: schemas.IncidentCreate) -> models.Incident:
    """
    Создание нового инцидента в БД
    """
    db_incident = models.Incident(
        description=incident.description,
        source=incident.source,
        status=models.IncidentStatus.NEW
    )
    db.add(db_incident)
    db.commit()
    db.refresh(db_incident)
    return db_incident


def get_incident(db: Session, incident_id: int) -> Optional[models.Incident]:
    """
    Получение инцидента по ID
    """
    return db.query(models.Incident).filter(models.Incident.id == incident_id).first()


def get_incidents(
        db: Session,
        status: Optional[str] = None,
        skip: int = 0,
        limit: int = 100
) -> List[models.Incident]:
    """
    Получение списка инцидентов с возможностью фильтрации по статусу
    """
    query = db.query(models.Incident)

    if status:
        # Фильтрация по статусу
        query = query.filter(models.Incident.status == status)

    return query.offset(skip).limit(limit).all()


def update_incident_status(
        db: Session,
        incident_id: int,
        status: schemas.IncidentStatus
) -> Optional[models.Incident]:
    """
    Обновление статуса инцидента
    """
    db_incident = get_incident(db, incident_id)
    if db_incident:
        db_incident.status = status
        db.commit()
        db.refresh(db_incident)
    return db_incident