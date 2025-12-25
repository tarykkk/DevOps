from django.contrib import admin
from .models import Article, Feedback


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'published_at', 'status']
    list_filter = ['status', 'created_at', 'published_at', 'author']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'published_at'
    ordering = ['status', '-published_at']
    list_per_page = 20


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['author_name', 'author_email', 'article', 'created_at', 'is_approved']
    list_filter = ['is_approved', 'created_at', 'updated_at']
    search_fields = ['author_name', 'author_email', 'content']
    list_editable = ['is_approved']
    date_hierarchy = 'created_at'