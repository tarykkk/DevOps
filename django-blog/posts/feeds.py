import markdown
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords_html
from django.urls import reverse_lazy
from .models import Article


class RecentArticlesFeed(Feed):
    """RSS feed for recent blog articles"""
    
    title = "BlogSite - Останні статті"
    link = reverse_lazy('posts:article_list')
    description = 'Нові статті нашого блогу'
    
    def items(self):
        return Article.published.all()[:5]
    
    def item_title(self, item):
        return item.title
    
    def item_description(self, item):
        markdown_html = markdown.markdown(item.content)
        return truncatewords_html(markdown_html, 30)
    
    def item_pubdate(self, item):
        return item.published_at