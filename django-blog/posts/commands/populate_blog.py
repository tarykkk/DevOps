from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from posts.models import Article


class Command(BaseCommand):
    help = 'Populate blog with sample Ukrainian articles'

    def handle(self, *args, **kwargs):
        # Create or get admin user
        admin_user, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@blogsite.com',
                'is_staff': True,
                'is_superuser': True
            }
        )
        
        if created:
            admin_user.set_password('admin123')
            admin_user.save()
            self.stdout.write(
                self.style.SUCCESS('✓ Created admin user (login: admin, password: admin123)')
            )

        # Sample articles data
        articles_data = [
            {
                'title': 'Вступ до Django',
                'slug': 'vstup-do-django',
                'content': '''Django - це високорівневий Python веб-фреймворк, який заохочує швидку розробку та чистий, прагматичний дизайн.

## Чому Django?

Django створений досвідченими розробниками і вирішує більшість проблем веб-розробки, тому ви можете зосередитись на написанні вашого застосунку без необхідності винаходити колесо. Це безкоштовно та з відкритим кодом.

## Основні переваги

- **Швидкість** - створений для швидкої розробки
- **Безпека** - захист від багатьох вразливостей
- **Масштабованість** - для проектів будь-якого розміру
- **Універсальність** - підходить для різних типів застосунків''',
                'status': Article.Status.PUBLISHED,
                'tags': ['django', 'python', 'framework', 'tutorial']
            },
            {
                'title': 'Моделі та бази даних у Django',
                'slug': 'modeli-ta-bazy-danych',
                'content': '''Модель - це єдине, остаточне джерело інформації про ваші дані. Вона містить поля та поведінку даних, які ви зберігаєте.

## ORM Django

Django надає потужний ORM (Object-Relational Mapping), який дозволяє працювати з базою даних використовуючи Python код замість SQL.

### Приклад моделі
```````python
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
```````

ORM автоматично перетворює ваші моделі у таблиці бази даних!''',
                'status': Article.Status.PUBLISHED,
                'tags': ['django', 'database', 'orm', 'models']
            },
            {
                'title': 'Views та Templates у Django',
                'slug': 'views-ta-templates',
                'content': '''Views обробляють логіку застосунку, а templates відповідають за представлення.

## Функції view

View - це Python функція, яка приймає веб-запит і повертає веб-відповідь. Ця відповідь може бути HTML-контентом веб-сторінки, перенаправленням, помилкою 404, XML-документом, зображенням тощо.

## Django Template Language

Django має власну мову шаблонів, яка дозволяє вставляти Python-подібний код безпосередньо в HTML.
```````html
{% for article in articles %}
    <h2>{{ article.title }}</h2>
{% endfor %}
``````''',
                'status': Article.Status.PUBLISHED,
                'tags': ['django', 'views', 'templates', 'frontend']
            },
            {
                'title': 'Форми Django та валідація',
                'slug': 'formy-django-validatsiya',
                'content': '''Django надає потужний механізм для роботи з HTML-формами.

## ModelForm

Найпростіший спосіб створення форми - використовувати ModelForm:
`````python
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']
`````

## Валідація

Django автоматично валідує дані форм і показує помилки користувачу. Ви також можете додавати власні правила валідації.

### CSRF захист

Всі форми Django автоматично захищені від CSRF-атак!''',
                'status': Article.Status.PUBLISHED,
                'tags': ['django', 'forms', 'validation', 'security']
            },
            {
                'title': 'Аутентифікація користувачів',
                'slug': 'autentyfikatsiya-korystuvachiv',
                'content': '''Django має вбудовану систему аутентифікації, яка обробляє облікові записи користувачів, групи, дозволи та сесії на основі cookies.

## User model

Django надає готову модель User з усіма необхідними полями та методами.

## Permissions

Система дозволів Django дозволяє призначати права доступу конкретним користувачам і групам користувачів.
`````python
@login_required
def my_view(request):
    # Тільки для авторизованих користувачів
    pass
````''',
                'status': Article.Status.PUBLISHED,
                'tags': ['django', 'auth', 'security', 'users']
            },
            {
                'title': 'Майбутня стаття про тестування (чернетка)',
                'slug': 'maybutnya-stattya-testuvannya',
                'content': '''Ця стаття ще в розробці...

## Заплановані розділи

- Unit тестування
- Integration тестування
- Test fixtures
- Coverage аналіз
- Best practices''',
                'status': Article.Status.DRAFT,
                'tags': ['django', 'testing', 'draft']
            }
        ]

        # Create articles
        for article_data in articles_data:
            tags_list = article_data.pop('tags', [])
            
            article, created = Article.objects.get_or_create(
                slug=article_data['slug'],
                defaults={
                    'title': article_data['title'],
                    'content': article_data['content'],
                    'author': admin_user,
                    'status': article_data['status'],
                    'published_at': timezone.now()
                }
            )
            
            if created:
                article.tags.add(*tags_list)
                status_icon = '✓' if article.status == Article.Status.PUBLISHED else '○'
                self.stdout.write(
                    self.style.SUCCESS(
                        f'{status_icon} Created: {article.title} (tags: {", ".join(tags_list)})'
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'○ Already exists: {article.title}')
                )
        
        self.stdout.write(self.style.SUCCESS('\n=== Blog populated successfully! ==='))
        self.stdout.write('Run server: python manage.py runserver')
        self.stdout.write('Admin panel: http://127.0.0.1:8000/admin/')
        self.stdout.write('Credentials: admin / admin123')

### 9. Documentation
