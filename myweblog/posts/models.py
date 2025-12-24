from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class ActiveManager(models.Manager):
    """Custom manager for retrieving only published articles"""
    def get_queryset(self):
        return super().get_queryset().filter(status=Article.Status.ACTIVE)


class Article(models.Model):
    """Blog article model"""
    
    class Status(models.TextChoices):
        DRAFT = 'DR', 'Draft'
        ACTIVE = 'AC', 'Active'
    
    heading = models.CharField(max_length=250, verbose_name='Заголовок')
    slug = models.SlugField(max_length=250, unique=True, verbose_name='URL-слаг')
    writer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='articles',
        verbose_name='Автор'
    )
    content = models.TextField(verbose_name='Зміст')
    publication_date = models.DateTimeField(
        default=timezone.now,
        verbose_name='Дата публікації'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Створено')
    modified_at = models.DateTimeField(auto_now=True, verbose_name='Оновлено')
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.DRAFT,
        verbose_name='Статус'
    )
    
    # Managers
    everything = models.Manager()
    active = ActiveManager()
    
    class Meta:
        ordering = ['-publication_date']
        indexes = [
            models.Index(fields=['-publication_date']),
        ]
        verbose_name = 'Стаття'
        verbose_name_plural = 'Статті'
    
    def __str__(self):
        return self.heading