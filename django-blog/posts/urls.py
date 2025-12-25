from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.article_list_view, name='article_list'),
    path('tag/<slug:tag_slug>/', views.article_list_view, name='articles_by_tag'),
    path(
        '<int:year>/<int:month>/<int:day>/<slug:slug>/',
        views.article_detail_view,
        name='article_detail'
    ),
    path('share/<int:article_id>/', views.share_article_view, name='share_article'),
    path('feedback/<int:article_id>/', views.submit_feedback_view, name='submit_feedback'),
]