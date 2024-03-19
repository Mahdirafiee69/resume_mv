from django.shortcuts import render
from .models import *


# Create your views here

def home(request):
    articles = Articles.objects.all()
    books = Books.objects.all()
    research = Research.objects.all()
    context = {'articles': articles, 'books': books ,'research':research}
    return render(request, 'home/home.html', context)


def book_detail(request, slug=None):
    detail = Books.objects.get(slug=slug)
    detail_1 = Books.objects.all()
    context = {'detail': detail, 'detail_1': detail_1}
    return render(request, 'home/book_detail.html', context)


def article_detail(request, slug=None):
    r_detail = Research.objects.get(slug=slug)
    context = {'r_detail': r_detail}
    return render(request, 'home/article_detail.html', context)


