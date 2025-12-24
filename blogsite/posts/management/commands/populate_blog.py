from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from posts.models import Article
from django.utils import timezone
from django.utils.text import slugify


class Command(BaseCommand):
    help = 'Populate blog with sample Ukrainian articles'

    def handle(self, *args, **kwargs):
        # Create or get admin user
        admin_user, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@blogsite.com',
                'is_staff': True,
                'is_superuser': True,
                'first_name': 'Адміністратор',
                'last_name': 'Сайту'
            }
        )
        
        if created:
            admin_user.set_password('admin123')
            admin_user.save()
            self.stdout.write(
                self.style.SUCCESS('✓ Створено адміністратора (admin / admin123)')
            )

        # Sample articles data
        articles_data = [
            {
                'title': 'Введення в Django Framework',
                'content': '''Django - це високорівневий Python веб-фреймворк, який заохочує швидку розробку та чистий, прагматичний дизайн.

**Основні переваги Django:**

**Швидка розробка**
Django розроблено для того, щоб допомогти розробникам якомога швидше перейти від концепції до завершення застосунку.

**Безпека**
Django серйозно ставиться до безпеки і допомагає розробникам уникати багатьох поширених помилок безпеки.

**Масштабованість**
Django використовують деякі найпопулярніші сайти в Інтернеті для обробки величезних обсягів трафіку.

**Універсальність**
Django підходить для створення практично будь-якого типу веб-сайту - від систем управління контентом до соціальних мереж.''',
                'excerpt': 'Огляд можливостей Django framework для швидкої веб-розробки',
                'status': 'published'
            },
            {
                'title': 'Робота з моделями в Django ORM',
                'content': '''Django ORM (Object-Relational Mapping) - це потужний інструмент для роботи з базами даних.

**Що таке ORM?**

ORM дозволяє працювати з базою даних використовуючи Python об'єкти замість SQL запитів.

**Основні можливості:**

**Визначення моделей**
Моделі визначаються як Python класи, які успадковують від models.Model.

**Міграції**
Django автоматично генерує міграції для змін в моделях.

**QuerySet API**
Потужний API для вибірки та фільтрації даних з бази.

**Зв'язки між моделями**
Підтримка ForeignKey, ManyToMany та OneToOne зв'язків.

Django ORM робить роботу з базами даних простою та інтуїтивною!''',
                'excerpt': 'Як ефективно використовувати Django ORM для роботи з базами даних',
                'status': 'published'
            },
            {
                'title': 'Створення RESTful API з Django',
                'content': '''Django REST framework - це потужний та гнучкий інструментарій для створення Web APIs.

**Чому Django REST Framework?**

**Веб-переглядач API**
Автоматично генерована документація та тестування API прямо в браузері.

**Автентифікація**
Підтримка різних схем автентифікації включаючи OAuth1, OAuth2, та JWT.

**Серіалізація**
Потужна система серіалізації підтримує як ORM так і не-ORM джерела даних.

**Кастомізація**
Всі компоненти можуть бути легко налаштовані та розширені.

**Тестування**
Включає інструменти для тестування API.

DRF робить створення API швидким та приємним процесом!''',
                'excerpt': 'Практичний посібник зі створення REST API використовуючи Django',
                'status': 'published'
            },
            {
                'title': 'Оптимізація продуктивності Django',
                'content': '''Коли ваш Django проект росте, важливо звертати увагу на продуктивність.

**Основні техніки оптимізації:**

**Кешування**
Використовуйте Django cache framework для зберігання дорогих обчислень.

**Оптимізація запитів**
Використовуйте select_related() та prefetch_related() для зменшення кількості запитів до БД.

**Індекси бази даних**
Додавайте індекси до часто використовуваних полів для прискорення запитів.

**Pagination**
Впроваджуйте пагінацію для великих списків даних.

**Асинхронність**
Django 3.0+ підтримує асинхронні views для обробки багатьох запитів.

Правильна оптимізація може значно покращити швидкість вашого застосунку!''',
                'excerpt': 'Кращі практики оптимізації продуктивності Django застосунків',
                'status': 'published'
            },
            {
                'title': 'Тестування Django застосунків',
                'content': '''Тестування - критична частина розробки надійних веб-застосунків.

**Види тестів у Django:**

**Unit тести**
Тестування окремих компонентів вашого коду в ізоляції.

**Integration тести**
Перевірка взаємодії між різними частинами системи.

**Функціональні тести**
Тестування повного функціоналу з точки зору користувача.

**Django TestCase**
Базовий клас для написання тестів з автоматичним створенням тестової БД.

**Coverage аналіз**
Використовуйте coverage.py для визначення покриття коду тестами.

Якісні тести - запорука стабільного продукту!''',
                'excerpt': 'Комплексний підхід до тестування Django проектів',
                'status': 'published'
            },
            {
                'title': 'Майбутня стаття про Docker (чернетка)',
                'content': '''Ця стаття зараз в розробці. Скоро тут з'явиться детальний гайд по контейнеризації Django застосунків.

**Плановані теми:**

- Створення Dockerfile для Django
- Docker Compose для мультиконтейнерних застосунків
- Налаштування Nginx та Gunicorn
- CI/CD з Docker
- Кращі практики для production''',
                'excerpt': 'Контейнеризація Django застосунків за допомогою Docker',
                'status': 'draft'
            }
        ]

        # Create articles
        for data in articles_data:
            slug = slugify(data['title'])
            article, created = Article.objects.get_or_create(
                slug=slug,
                defaults={
                    'title': data['title'],
                    'content': data['content'],
                    'excerpt': data['excerpt'],
                    'status': data['status'],
                    'is_published': data['status'] == 'published',
                    'author': admin_user,
                    'published_at': timezone.now()
                }
            )
            
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'✓ Створено статтю: {article.title}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'○ Стаття вже існує: {article.title}')
                )
        
        self.stdout.write(self.style.SUCCESS('\\n=== Налаштування завершено ==='))
        self.stdout.write('Запуск сервера: python manage.py runserver')
        self.stdout.write('Адмін панель: http://127.0.0.1:8000/admin/')
        self.stdout.write('Логін: admin / admin123')