# BlogSite - Платформа блогу на Django

Сучасний блоговий додаток, побудований на фреймворку Django для практичної роботи з DevOps.

[Перейти до репозиторію](https://github.com/tarykkk/DevOps/tree/main/django-blog)

## Функціональність

### Основний функціонал
- Керування статтями з підтримкою Markdown
- Система тегів для організації контенту
- Система відгуків/коментарів користувачів
- Можливість надсилання статей електронною поштою
- Пагінація (3 статті на сторінку)
- Фільтрація за тегами

### Розширений функціонал
- RSS-стрічка останніх статей
- XML-карта сайту для SEO
- Користувацькі шаблонні теги та фільтри
- Блок популярних статей
- Рекомендації пов’язаних статей
- Підтримка рендерингу Markdown

## Вимоги

- Python 3.10+
- PostgreSQL 14+
- Django 5.0+

## Встановлення

### 1. Клонування репозиторію
```bash
git clone <repository-url>
cd blogsite
```

### 2. Створення віртуального середовища
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3. Встановлення залежностей
```bash
pip install -r requirements.txt
```

### 4. Налаштування бази даних
Редагуйте `blogsite/settings.py` та оновіть дані підключення:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blog',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Застосування міграцій
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Створення тестових даних
```bash
python manage.py populate_blog
```

Це створює адміністративного користувача:
- Логін: `admin`
- Пароль: `admin123`

### 7. Запуск сервера розробки
```bash
python manage.py runserver
```

##  URL-адреси

- **Головна сторінка**: http://127.0.0.1:8000/
- **Адмін-панель**: http://127.0.0.1:8000/admin/
- **RSS-стрічка**: http://127.0.0.1:8000/rss/
- **Карта сайту**: http://127.0.0.1:8000/sitemap.xml
- **Фільтр за тегом**: http://127.0.0.1:8000/tag/<tag-slug>/

##  Структура проекту
```bash
blogsite/
├── posts/ # Основний додаток блогу
│ ├── management/ # Команди управління
│ │ └── commands/
│ │ └── populate_blog.py
│ ├── migrations/ # Міграції бази даних
│ ├── templatetags/ # Користувацькі теги шаблонів
│ │ └── post_extras.py
│ ├── admin.py # Налаштування адмінки
│ ├── feeds.py # RSS-стрічка
│ ├── forms.py # Форми
│ ├── models.py # Моделі даних
│ ├── sitemaps.py # Налаштування карти сайту
│ ├── urls.py # URL-маршрути
│ └── views.py # Представлення
├── blogsite/ # Налаштування проекту
│ ├── settings.py # Конфігурація
│ └── urls.py # Кореневі URL
├── templates/ # HTML-шаблони
│ └── posts/
│ ├── base.html
│ ├── article_list.html
│ ├── article_detail.html
│ └── components/
├── static/ # Статичні файли
│ └── styles/
│ └── main.css
├── manage.py
└── requirements.txt

markdown
Копировать код
`````
## Використання

### Додавання тегів до статей

1. Перейдіть в адмін-панель: http://127.0.0.1:8000/admin/
2. Виберіть "Articles"
3. Створіть або відредагуйте статтю
4. Додайте теги через кому: `django, python, tutorial`
5. Збережіть

### Перегляд статей за тегом

Клацніть на будь-який тег у списку статей або перейдіть за адресою:
`http://127.0.0.1:8000/tag/<tag-slug>/`


[Посилання](https://example.com)