from app.database import SessionLocal
from app import models

def init_test_data():
    db = SessionLocal()
    try:
        # Проверяем, есть ли уже данные
        if db.query(models.Incident).count() == 0:
            # Создаем тестовые инциденты
            test_incidents = [
                models.Incident(
                    description="Самокат №123 не в сети уже 2 часа",
                    source=models.IncidentSource.OPERATOR
                ),
                models.Incident(
                    description="Точка выдачи на Варшавском шоссе не отвечает",
                    source=models.IncidentSource.MONITORING,
                    status=models.IncidentStatus.IN_PROGRESS
                ),
                models.Incident(
                    description="Отчёт по продажам за январь не выгрузился",
                    source=models.IncidentSource.PARTNER,
                    status=models.IncidentStatus.RESOLVED
                )
            ]

            db.add_all(test_incidents)
            db.commit()
            print("Тестовые данные добавлены")
        else:
            print("Данные уже существуют")
    finally:
        db.close()


if __name__ == "__main__":
    init_test_data()