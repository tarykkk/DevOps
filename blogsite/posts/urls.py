from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article_list'),
    path(
        '<int:year>/<int:month>/<int:day>/<slug:slug>/',
        views.article_detail_view,
        name='article_detail'
    ),
    path('share/<int:article_id>/', views.share_article_view, name='share_article'),
    path('<int:article_id>/feedback/', views.submit_feedback_view, name='submit_feedback'),
]