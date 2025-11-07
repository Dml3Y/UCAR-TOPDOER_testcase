# UCAR-TOPDOER_testcase

API-сервис учёта инцидентов для UCAR<>TOPDOER

## API

| Метод  | Путь                       | Описание                     |
|--------|----------------------------|------------------------------|
| POST   | `/incidents`               | Создание инцидента           |
| GET    | `/incidents`               | Получение списка инцидентов  |
| GET    | `/incidents/{incident_id}` | Получение инцидента по ID    |
| PATCH  | `/incidents/{incident_id}` | Обновление статуса инцидента |

## Модель данных

Инцидент содержит:

| Поле          | Описание                                    |
|---------------|---------------------------------------------|
| `id`          | Уникальный идентификатор                    |
| `description` | Описание проблемы                           |
| `status`      | Статус (new, in_progress, resolved, closed) |
| `source`      | Источник (operator, monitoring, partner)    |
| `created_at`  | Время создания                              |

## Требования

* Python 3.13.1
* FastApi 0.104.1
* PostgreSQL 18.0

## Установка

1. `git clone https://github.com/Dml3Y/UCAR-TOPDOER_testcase.git`
2. `python -m venv .venv`
3. Запуск виртуальной среды:
  - Windows, PowerShell: `.\.venv\Scripts\Activate.ps1`
  - Windows, командная строка: `.\.venv\Scripts\activate.bat`
  - Linux: `source .venv/Scripts/activate`
1. Установите зависимости:
- `pip install -r requirements.txt`
2. Настройте базу данных PostgreSQL:
- Создайте БД `incident_db`
- Обновите строку подключения в `app/database.py`:
  - `SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Zxc983354@localhost:5432/incident_db?client_encoding=utf8"`
3. Запустите сервер:
- `uvicorn app.main:app --reload`

Сервер будет доступен по адресу: http://localhost:8000

Документация API: http://localhost:8000/docs

## Порт запуска по умолчанию
8000