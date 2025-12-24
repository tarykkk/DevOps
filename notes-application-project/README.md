# 📝 Notes Application

[Перейти до репозиторію](https://github.com/tarykkk/DevOps/tree/main/notes-application-project)

Контейнеризований вебзастосунок на **Flask** та **PostgreSQL**, створений для демонстрації роботи з **Docker** і **Docker Compose**.

---

## Опис проєкту

Цей проєкт реалізує просту систему керування нотатками як практичну роботу з:
- контейнеризації вебзастосунків
- оркестрації кількох контейнерів через Docker Compose
- інтеграції бази даних та збереження даних
- проєктування RESTful API

---

## Можливості

- ✅ RESTful API для керування нотатками  
- ✅ PostgreSQL з постійним збереженням даних  
- ✅ Повна контейнеризація через Docker  
- ✅ Health check endpoint  
- ✅ Автоматична ініціалізація бази даних  
- ✅ Connection pooling для кращої продуктивності  
- ✅ Простий HTML-інтерфейс  

---

## Вимоги

- Docker Engine 20.10+
- Docker Compose 2.0+
- Git

---

## Швидкий старт

### 1. Клонування репозиторію
```bash
git clone 
cd lab7-notes-app
```
### 2. Налаштування середовища
```bash
cp .env.example .env
# Відредагуй .env за потреби
```
### 3. Запуск застосунку
```bash
docker-compose up -d
docker-compose logs -f
docker-compose ps
```
### Ініціалізація бази даних (опційно)

База ініціалізується автоматично, але за потреби:
```bash
chmod +x scripts/setup_db.sh
./scripts/setup_db.sh
```
### API Endpoints
Головна сторінка
```bash
GET http://localhost:5000/
```
Повертає HTML-інтерфейс з документацією.

### Health Check
```bash
curl http://localhost:5000/health
```
```bash
{
  "status": "healthy",
  "database": "connected",
  "timestamp": "2024-12-08T10:30:00"
}
```
### Отримати всі нотатки
```bash
curl http://localhost:5000/api/notes
```
### Створити нотатку
```bash
curl -X POST http://localhost:5000/api/notes \
  -H "Content-Type: application/json" \
  -d '{
    "title": "My Note",
    "content": "Note content here"
  }'
```
### Схема бази даних
```bash
CREATE TABLE notes (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE,
    updated_at TIMESTAMP WITH TIME ZONE
);
```
### Структура проєкту
```bash
.
├── src/
│   └── app.py
├── database/
│   └── init.sql
├── scripts/
│   ├── setup_db.sh
│   └── verify_db.sh
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```
### Основні Docker команди
```bash
docker-compose up -d
docker-compose down
docker-compose restart
docker-compose down -v
```
### Тестування
```bash
curl http://localhost:5000/health
curl http://localhost:5000/api/notes
```
### Усунення проблем
```bash
Контейнери не запускаються
docker-compose logs
docker-compose up -d --build

Проблеми з підключенням до БД
docker-compose exec database pg_isready
docker-compose exec webapp env | grep DB_
```
### Розробка без Docker
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

export DB_HOST=localhost
export DB_NAME=notesdb
export DB_USER=postgres
export DB_PASSWORD=secretpass

python src/app.py
```

## Автор

Тарасюк Максим
