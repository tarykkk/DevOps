from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager


class PublishedArticlesManager(models.Manager):
    """Manager for retrieving only published articles"""
    
    def get_queryset(self):
        return super().get_queryset().filter(status=Article.Status.PUBLISHED)


class Article(models.Model):
    """Main blog article model"""
    
    class Status(models.TextChoices):
        DRAFT = 'DR', 'Draft'
        PUBLISHED = 'PU', 'Published'
    
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    slug = models.SlugField(max_length=250, unique_for_date='published_at', verbose_name='URL')
    content = models.TextField(verbose_name='Контент')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='articles',
        verbose_name='Автор'
    )
    published_at = models.DateTimeField(default=timezone.now, verbose_name='Дата публікації')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Створено')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Оновлено')
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.DRAFT,
        verbose_name='Статус'
    )
    
    # Tagging functionality
    tags = TaggableManager(verbose_name='Теги')
    
    # Managers
    objects = models.Manager()
    published = PublishedArticlesManager()
    
    class Meta:
        ordering = ['-published_at']
        indexes = [
            models.Index(fields=['-published_at']),
        ]
        verbose_name = 'Стаття'
        verbose_name_plural = 'Статті'
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('posts:article_detail',
                      args=[
                          self.published_at.year,
                          self.published_at.month,
                          self.published_at.day,
                          self.slug
                      ])


class Feedback(models.Model):
    """User feedback/comments on articles"""
    
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='feedbacks',
        verbose_name='Стаття'
    )
    author_name = models.CharField(max_length=80, verbose_name="Ім'я")
    author_email = models.EmailField(verbose_name='Email')
    content = models.TextField(verbose_name='Коментар')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Створено')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Оновлено')
    is_approved = models.BooleanField(default=True, verbose_name='Схвалено')
    
    class Meta:
        ordering = ['created_at']
        indexes = [
            models.Index(fields=['created_at']),
        ]
        verbose_name = 'Відгук'
        verbose_name_plural = 'Відгуки'
    
    def __str__(self):
        return f'Feedback by {self.author_name} on {self.article}'