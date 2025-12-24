from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.core.mail import send_mail
from django.views.decorators.http import require_POST
from django.conf import settings
from .models import Article, Feedback
from .forms import ShareArticleForm, FeedbackForm


class ArticleListView(ListView):
    """Class-based view for listing articles"""
    queryset = Article.published_objects.all()
    context_object_name = 'articles'
    paginate_by = 3
    template_name = 'posts/article_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Всі статті'
        return context


def article_detail_view(request, year, month, day, slug):
    """Function-based view for article details"""
    article = get_object_or_404(
        Article,
        is_published=True,
        slug=slug,
        published_at__year=year,
        published_at__month=month,
        published_at__day=day
    )
    
    # Get approved feedbacks
    approved_feedbacks = article.feedbacks.filter(is_approved=True)
    
    # Initialize feedback form
    feedback_form = FeedbackForm()
    
    context = {
        'article': article,
        'feedbacks': approved_feedbacks,
        'feedback_form': feedback_form,
        'page_title': article.title
    }
    
    return render(request, 'posts/article_detail.html', context)


def share_article_view(request, article_id):
    """View for sharing article via email"""
    article = get_object_or_404(Article, id=article_id, is_published=True)
    email_sent = False
    
    if request.method == 'POST':
        form = ShareArticleForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            article_url = request.build_absolute_uri(article.get_absolute_url())
            
            subject = f"{data['sender_name']} рекомендує прочитати: {article.title}"
            
            message_body = (
                f"Вітаю!\\n\\n"
                f"{data['sender_name']} ({data['sender_email']}) рекомендує вам прочитати цю статтю:\\n\\n"
                f"Назва: {article.title}\\n"
                f"Посилання: {article_url}\\n\\n"
            )
            
            if data['message']:
                message_body += f"Особисте повідомлення:\\n{data['message']}\\n\\n"
            
            message_body += "Приємного читання!"
            
            send_mail(
                subject=subject,
                message=message_body,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[data['recipient_email']],
                fail_silently=False
            )
            email_sent = True
    else:
        form = ShareArticleForm()
    
    context = {
        'article': article,
        'form': form,
        'email_sent': email_sent,
        'page_title': f'Поділитися: {article.title}'
    }
    
    return render(request, 'posts/share_article.html', context)


@require_POST
def submit_feedback_view(request, article_id):
    """View for submitting feedback"""
    article = get_object_or_404(Article, id=article_id, is_published=True)
    feedback_instance = None
    form = FeedbackForm(data=request.POST)
    
    if form.is_valid():
        feedback_instance = form.save(commit=False)
        feedback_instance.article = article
        feedback_instance.save()
    
    context = {
        'article': article,
        'form': form,
        'feedback': feedback_instance,
        'page_title': 'Додати коментар'
    }
    
    return render(request, 'posts/feedback_submitted.html', context)