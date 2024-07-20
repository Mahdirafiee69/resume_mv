from django.urls import path, include
from . import views
from home.views import books
app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
    path('books/', books.as_view(), name='books'),
    path('articles/', views.articles, name='articles'),
    path('book_detail/<slug:slug>/', views.book_detail, name='book_detail'),
    path('article_detail/<slug:slug>/', views.article_detail, name='article_detail'),


]
