from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.articles_list, name='articles_list'),
    path('article/<int:article_id>/', views.article_details, name='article_details'),
]