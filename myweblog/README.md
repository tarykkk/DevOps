# MyWebLog - Django Blog Application

Простий блог на Django для практичної роботи.

[Перейти до репозиторію](https://github.com/tarykkk/DevOps/tree/main/myweblog)

## Встановлення

1. Клонувати репозиторій
2. Створити віртуальне середовище:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\\Scripts\\activate     # Windows
```

3. Встановити залежності:
```bash
pip install -r requirements.txt
```

4. Виконати міграції:
```bash
python manage.py migrate
```

5. Створити тестові дані:
```bash
python manage.py populate_articles
```

6. Запустити сервер:
```bash
python manage.py runserver
```

## Доступ

- Блог: http://127.0.0.1:8000/
- Адмін-панель: http://127.0.0.1:8000/admin/
- Логін: adminuser
- Пароль: adminpass123

## Структура

- `posts/` - основний додаток
- `templates/` - HTML шаблони
- `static/` - CSS стилі