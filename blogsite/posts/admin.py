from django.contrib import admin
from .models import Article, Feedback


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published_at', 'status', 'is_published']
    list_filter = ['status', 'is_published', 'created_at', 'published_at', 'author']
    search_fields = ['title', 'content', 'excerpt']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'published_at'
    ordering = ['-published_at', 'status']
    list_editable = ['status', 'is_published']
    
    fieldsets = (
        ('Основна інформація', {
            'fields': ('title', 'slug', 'author', 'excerpt')
        }),
        ('Контент', {
            'fields': ('content',)
        }),
        ('Публікація', {
            'fields': ('status', 'is_published', 'published_at')
        }),
    )


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['author_name', 'author_email', 'article', 'created_at', 'is_approved']
    list_filter = ['is_approved', 'created_at', 'modified_at']
    search_fields = ['author_name', 'author_email', 'content']
    list_editable = ['is_approved']
    raw_id_fields = ['article']
    date_hierarchy = 'created_at'
    
    readonly_fields = ['created_at', 'modified_at']