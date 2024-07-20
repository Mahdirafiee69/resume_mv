from django.shortcuts import render, get_object_or_404
from .forms import CommentForm
from .models import *
from django.views.generic import ListView
import json


# Create your views here

def home(request):
    articles = Articles.objects.all()
    books = Books.objects.all()
    research = Research.objects.all()
    context = {'articles': articles, 'books': books, 'research': research}
    return render(request, 'home/home.html', context)


def book_detail(request, slug=None):
    books = get_object_or_404(Books, slug=slug)
    books_1 = Books.objects.all()
    comments = Comment.objects.filter(post=books, reply=None)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            content = request.POST.get('content')
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            reply_id = request.POST.get('comment_id')
            comment_qs = None
            if reply_id:
                comment_qs = Comment.objects.get(id=reply_id)
            comment = Comment.objects.create(post=books, content=content, name=name, phone=phone, reply=comment_qs)
            comment.save()
            context = {'books': books, 'books_1': books_1, 'comments': comments, 'comment_form': comment_form}
            return render(request, 'home/book_detail.html', context)
    else:
        comment_form = CommentForm()

    context = {'books': books, 'books_1': books_1, 'comments': comments, 'comment_form': comment_form}
    return render(request, 'home/book_detail.html', context)


def article_detail(request, slug=None):
    r_detail = get_object_or_404(Research, slug=slug)
    r_detail_1 = Research.objects.all()
    comments = Commenta.objects.filter(post=r_detail, reply=None)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            content = request.POST.get('content')
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            reply_id = request.POST.get('comment_id')
            comment_qs = None
            if reply_id:
                comment_qs = Commenta.objects.get(id=reply_id)
            comment = Commenta.objects.create(post=r_detail, content=content, name=name, phone=phone, reply=comment_qs)
            comment.save()
            context = {'r_detail': r_detail, 'r_detail_1': r_detail_1, 'comments': comments,
                       'comment_form': comment_form}
            return render(request, 'home/article_detail.html', context)
    else:
        comment_form = CommentForm()
    context = {'r_detail': r_detail, 'r_detail_1': r_detail_1, 'comments': comments, 'comment_form': comment_form}
    return render(request, 'home/article_detail.html', context)


class books(ListView):
    model = Books
    template_name = 'home/books.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs_json"] = json.dumps(list(Books.objects.values()))
        return context



def articles(request):
    all_articles = Research.objects.all()
    context = {'all_articles': all_articles}
    return render(request, 'home/articles.html', context)



