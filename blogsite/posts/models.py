from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class ActiveManager(models.Manager):
    """Custom manager for published articles"""
    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)


class Article(models.Model):
    """Blog article model"""
    
    STATUS_CHOICES = [
        ('draft', 'Чернетка'),
        ('published', 'Опубліковано'),
    ]
    
    title = models.CharField('Заголовок', max_length=255)
    slug = models.SlugField('URL-адреса', max_length=255, unique_for_date='published_at')
    content = models.TextField('Контент')
    excerpt = models.TextField('Короткий опис', max_length=500, blank=True)
    published_at = models.DateTimeField('Дата публікації', default=timezone.now)
    created_at = models.DateTimeField('Дата створення', auto_now_add=True)
    modified_at = models.DateTimeField('Дата оновлення', auto_now=True)
    is_published = models.BooleanField('Опубліковано', default=False)
    status = models.CharField('Статус', max_length=10, choices=STATUS_CHOICES, default='draft')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='articles',
        verbose_name='Автор'
    )
    
    objects = models.Manager()
    published_objects = ActiveManager()
    
    class Meta:
        ordering = ['-published_at']
        verbose_name = 'Стаття'
        verbose_name_plural = 'Статті'
        indexes = [
            models.Index(fields=['-published_at']),
            models.Index(fields=['slug']),
        ]
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('posts:article_detail',
                      kwargs={
                          'year': self.published_at.year,
                          'month': self.published_at.month,
                          'day': self.published_at.day,
                          'slug': self.slug
                      })
    
    def save(self, *args, **kwargs):
        if self.status == 'published':
            self.is_published = True
        super().save(*args, **kwargs)


class Feedback(models.Model):
    """Comment/Feedback model for articles"""
    
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='feedbacks',
        verbose_name='Стаття'
    )
    author_name = models.CharField('Ім\\'я автора', max_length=100)
    author_email = models.EmailField('Email автора')
    content = models.TextField('Текст коментаря')
    created_at = models.DateTimeField('Дата створення', auto_now_add=True)
    modified_at = models.DateTimeField('Дата оновлення', auto_now=True)
    is_approved = models.BooleanField('Схвалено', default=True)
    
    class Meta:
        ordering = ['created_at']
        verbose_name = 'Коментар'
        verbose_name_plural = 'Коментарі'
        indexes = [
            models.Index(fields=['created_at']),
            models.Index(fields=['is_approved']),
        ]
    
    def __str__(self):
        return f 'Коментар від {self.author_name} до {self.article.title}'