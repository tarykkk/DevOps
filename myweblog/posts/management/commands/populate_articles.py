from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from posts.models import Article
from django.utils import timezone


class Command(BaseCommand):
    help = 'Populate database with sample articles'

    def handle(self, *args, **options):
        # Get or create admin user
        admin_user, created = User.objects.get_or_create(
            username='adminuser',
            defaults={
                'email': 'admin@myblog.com',
                'is_staff': True,
                'is_superuser': True
            }
        )
        
        if created:
            admin_user.set_password('adminpass123')
            admin_user.save()
            self.stdout.write(
                self.style.SUCCESS('Admin user created successfully')
            )

        # Sample articles data
        sample_articles = [
            {
                'heading': 'Знайомство зі мною',
                'slug': 'znakomstvo-zi-mnoyu',
                'content': '''Привіт! Мене звати [Ім'я студента], і це мій особистий веб-блог.

Я навчаюся на факультеті інформаційних технологій і захоплююсь веб-розробкою. 
Цей блог створено в рамках вивчення фреймворку Django.

Тут я планую ділитися своїми думками про програмування, новими знахідками 
у світі IT та цікавими проектами, над якими працюю.

Сподіваюся, мій досвід буде корисним!''',
                'status': Article.Status.ACTIVE
            },
            {
                'heading': 'Секрети ефективного онлайн-навчання',
                'slug': 'sekrety-efektyvnoho-onlayn-navchannya',
                'content': '''Онлайн-навчання стає нормою сучасної освіти, але має свої особливості.

**Мої поради для успіху:**

→ Плануйте свій день і створіть чіткий розклад
→ Оформіть комфортне робоче місце без відволікаючих факторів
→ Робіть перерви кожні 45-50 хвилин
→ Активно берніть участь у дискусіях та форумах
→ Ставте запитання викладачам і одногрупникам

Найважливіше - знайти баланс між навчанням та відпочинком, 
щоб уникнути вигорання.''',
                'status': Article.Status.ACTIVE
            },
            {
                'heading': 'Django для початківців: мій досвід',
                'slug': 'django-dlya-pochatkivtsiv',
                'content': '''Django - це потужний Python-фреймворк, який робить веб-розробку простою.

**Що я вивчив про Django:**

- Архітектура MVT (Model-View-Template)
- ORM для роботи з базами даних
- Вбудована адмін-панель
- Система шаблонів
- Маршрутизація URL

Django має чудову документацію та велику спільноту розробників, 
що робить навчання набагато легшим. Рекомендую!''',
                'status': Article.Status.ACTIVE
            },
            {
                'heading': 'Чернетка майбутньої статті',
                'slug': 'chernetka-maybutnoi-statti',
                'content': 'Ця стаття ще в процесі написання...',
                'status': Article.Status.DRAFT
            }
        ]

        for article_data in sample_articles:
            article, created = Article.objects.get_or_create(
                slug=article_data['slug'],
                defaults={
                    'heading': article_data['heading'],
                    'writer': admin_user,
                    'content': article_data['content'],
                    'status': article_data['status'],
                    'publication_date': timezone.now()
                }
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'✓ Created: {article.heading}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Already exists: {article.heading}')
                )
        
        self.stdout.write(
            self.style.SUCCESS('\\nDatabase populated successfully!')
        )