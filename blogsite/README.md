# BlogSite - Сучасний Django Blog

[Перейти до репозиторію](https://github.com/tarykkk/DevOps/tree/main/blogsite)

Повнофункціональний блог створений на Django framework як частина практичної роботи з DevOps.

##  Основні можливості

- Список статей з пагінацією (3 статті на сторінку)
- Детальний перегляд статей
- SEO-оптимізовані URL з датою та slug
- Система коментарів з модерацією
- Відправка статей через email
- Адмін-панель для управління контентом
- Розділення статей на чернетки та опубліковані
- Сучасний респонсивний дизайн

##  Вимоги

- Python 3.8+
- Django 5.0+
- python-dotenv

##  Встановлення

### 1. Клонування репозиторію
```bash
git clone <your-repository-url>
cd blogsite
```

### 2. Створення віртуального середовища
```bash
python -m venv venv

# Windows
venv\\Scripts\\activate

# Linux/Mac
source venv/bin/activate
```

### 3. Встановлення залежностей
```bash
pip install -r requirements.txt
```

### 4. Налаштування змінних середовища

Створіть файл `.env` в корені проекту:
```env
SECRET_KEY=your-super-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
```

### 5. Виконання міграцій
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Створення тестових даних
```bash
python manage.py populate_blog
```

Ця команда створить:
- Адміністратора з логіном `admin` та паролем `admin123`
- 5 опублікованих статей
- 1 чернетку статті

### 7. Запуск сервера розробки
```bash
python manage.py runserver
```

Відкрийте браузер:
- **Головна сторінка**: http://127.0.0.1:8000/
- **Адмін-панель**: http://127.0.0.1:8000/admin/

##  Структура проекту
```
blogsite/
├── blogsite/                  # Конфігурація проекту
│   ├── settings.py           # Налаштування Django
│   ├── urls.py               # Головні маршрути
│   └── wsgi.py               # WSGI конфігурація
├── posts/                    # Додаток блогу
│   ├── management/           # Команди управління
│   │   └── commands/
│   │       └── populate_blog.py
│   ├── migrations/           # Міграції БД
│   ├── admin.py             # Налаштування адмін-панелі
│   ├── forms.py             # Форми
│   ├── models.py            # Моделі даних
│   ├── urls.py              # URL маршрути додатку
│   └── views.py             # Представлення
├── frontend/                # Frontend ресурси
│   ├── templates/           # HTML шаблони
│   │   ├── base.html       # Базовий шаблон
│   │   └── posts/          # Шаблони статей
│   └── static/             # Статичні файли
│       └── css/
│           └── main.css    # Стилі
├── .env.example            # Приклад змінних середовища
├── .gitignore              # Git ignore файл
├── manage.py               # Django CLI
├── requirements.txt        # Python залежності
└── README.md              # Ця документація
```

##  Функціонал

### Для користувачів

- **Перегляд статей**: Список всіх опублікованих статей з пагінацією
- **Читання**: Повний перегляд статті з метаданими автора
- **Коментування**: Можливість залишати коментарі до статей
- **Розповсюдження**: Відправка статей друзям через email

### Для адміністраторів

- **Управління статтями**: Створення, редагування, видалення
- **Модерація коментарів**: Схвалення/відхилення коментарів
- **Статуси**: Чернетки та опубліковані статті
- **Пошук та фільтрація**: Зручні інструменти в адмін-панелі

##  Команди
```bash
# Створити суперкористувача
python manage.py createsuperuser

# Заповнити БД тестовими даними
python manage.py populate_blog

# Створити міграції
python manage.py makemigrations

# Застосувати міграції
python manage.py migrate

# Запустити сервер
python manage.py runserver

# Відкрити Django shell
python manage.py shell

# Зібрати статичні файли (production)
python manage.py collectstatic
```

##  Налаштування Email

У режимі розробки email виводяться в консоль.

Для production в `.env` додайте:
```env
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
```

Для Gmail використовуйте [App Password](https://support.google.com/accounts/answer/185833).

##  Налаштування

### Debug режим

Для production встановіть в `.env`:
```env
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

### База даних

За замовчуванням використовується SQLite. Для production рекомендується PostgreSQL.

##  Тестування
```bash
# Запустити всі тести
python manage.py test

# Запустити тести конкретного додатку
python manage.py test posts

# З coverage
coverage run --source='.' manage.py test
coverage report
```

##  Модель даних

### Article (Стаття)
- title - заголовок
- slug - URL-адреса
- content - контент
- excerpt - короткий опис
- published_at - дата публікації
- status - статус (draft/published)
- author - автор (ForeignKey to User)

### Feedback (Коментар)
- article - стаття (ForeignKey to Article)
- author_name - ім'я автора
- author_email - email автора
- content - текст коментаря
- is_approved - схвалено модератором


## Автор

Тарасюк Максим