from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['heading', 'slug', 'writer', 'publication_date', 'status']
    list_filter = ['status', 'created_at', 'publication_date', 'writer']
    search_fields = ['heading', 'content']
    prepopulated_fields = {'slug': ('heading',)}
    raw_id_fields = ['writer']
    date_hierarchy = 'publication_date'
    ordering = ['status', 'publication_date']
    list_per_page = 20