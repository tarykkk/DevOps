from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.views.decorators.http import require_POST
from django.db.models import Count
from taggit.models import Tag

from .models import Article, Feedback
from .forms import ShareArticleForm, FeedbackForm, ArticleSearchForm


def article_list_view(request, tag_slug=None):
    """Display list of articles with optional tag filtering"""
    
    articles_queryset = Article.published.all()
    selected_tag = None
    
    # Filter by tag if provided
    if tag_slug:
        selected_tag = get_object_or_404(Tag, slug=tag_slug)
        articles_queryset = articles_queryset.filter(tags__in=[selected_tag])
    
    # Pagination - 3 articles per page
    paginator = Paginator(articles_queryset, 3)
    page_number = request.GET.get('page', 1)
    
    try:
        articles = paginator.page(page_number)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    
    context = {
        'articles': articles,
        'selected_tag': selected_tag
    }
    return render(request, 'posts/article_list.html', context)


def article_detail_view(request, year, month, day, slug):
    """Display single article with feedbacks and related articles"""
    
    article = get_object_or_404(
        Article,
        status=Article.Status.PUBLISHED,
        slug=slug,
        published_at__year=year,
        published_at__month=month,
        published_at__day=day
    )
    
    # Get approved feedbacks
    approved_feedbacks = article.feedbacks.filter(is_approved=True)
    
    # Feedback form
    feedback_form = FeedbackForm()
    
    # Find related articles by tags
    article_tag_ids = article.tags.values_list('id', flat=True)
    related_articles = Article.published.filter(tags__in=article_tag_ids).exclude(id=article.id)
    related_articles = related_articles.annotate(
        common_tags=Count('tags')
    ).order_by('-common_tags', '-published_at')[:4]
    
    context = {
        'article': article,
        'feedbacks': approved_feedbacks,
        'feedback_form': feedback_form,
        'related_articles': related_articles
    }
    return render(request, 'posts/article_detail.html', context)


def share_article_view(request, article_id):
    """Handle article sharing via email"""
    
    article = get_object_or_404(
        Article,
        id=article_id,
        status=Article.Status.PUBLISHED
    )
    email_sent = False
    
    if request.method == 'POST':
        form = ShareArticleForm(request.POST)
        if form.is_valid():
            cleaned = form.cleaned_data
            article_url = request.build_absolute_uri(article.get_absolute_url())
            
            subject = f"{cleaned['sender_name']} рекомендує прочитати: {article.title}"
            message = (
                f"Прочитайте статтю '{article.title}' за посиланням:\n"
                f"{article_url}\n\n"
                f"Коментар від {cleaned['sender_name']}:\n"
                f"{cleaned['message']}"
            )
            
            send_mail(
                subject,
                message,
                'noreply@blogsite.com',
                [cleaned['recipient_email']]
            )
            email_sent = True
    else:
        form = ShareArticleForm()
    
    context = {
        'article': article,
        'form': form,
        'email_sent': email_sent
    }
    return render(request, 'posts/share_article.html', context)


@require_POST
def submit_feedback_view(request, article_id):
    """Handle feedback submission"""
    
    article = get_object_or_404(
        Article,
        id=article_id,
        status=Article.Status.PUBLISHED
    )
    
    feedback_instance = None
    form = FeedbackForm(data=request.POST)
    
    if form.is_valid():
        feedback_instance = form.save(commit=False)
        feedback_instance.article = article
        feedback_instance.save()
    
    context = {
        'article': article,
        'form': form,
        'feedback': feedback_instance
    }
    return render(request, 'posts/feedback_submitted.html', context)