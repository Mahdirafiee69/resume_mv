from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
    path('book_detail/<slug:slug>/', views.book_detail, name='book_detail'),
    path('article_detail/<slug:slug>/', views.article_detail, name='article_detail'),

]
