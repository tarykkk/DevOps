from django.shortcuts import render, get_object_or_404
from .models import Article


def articles_list(request):
    """Display all published articles"""
    articles = Article.active.all()
    context = {'articles': articles}
    return render(request, 'posts/article/listing.html', context)


def article_details(request, article_id):
    """Display single article details"""
    article = get_object_or_404(
        Article,
        id=article_id,
        status=Article.Status.ACTIVE
    )
    context = {'article': article}
    return render(request, 'posts/article/details.html', context)