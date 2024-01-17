from . import views
from django.urls import path

urlpatterns = [
    path('', views.news, name='news'),
    path('<int:news_id>/', views.one_news_item, name='news_item'),
]
