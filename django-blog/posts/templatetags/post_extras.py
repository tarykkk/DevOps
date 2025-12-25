from django import template
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown as md

from ..models import Article

register = template.Library()


@register.simple_tag
def count_published_articles():
    """Return total count of published articles"""
    return Article.published.count()


@register.inclusion_tag('posts/components/recent_articles.html')
def display_recent_articles(limit=5):
    """Display recent published articles"""
    recent = Article.published.order_by('-published_at')[:limit]
    return {'recent_articles': recent}


@register.simple_tag
def fetch_popular_articles(limit=5):
    """Get articles with most feedbacks"""
    popular = Article.published.annotate(
        feedback_count=Count('feedbacks')
    ).order_by('-feedback_count')[:limit]
    return popular


@register.filter(name='render_markdown')
def render_markdown(text):
    """Convert markdown text to HTML"""
    return mark_safe(md.markdown(text))