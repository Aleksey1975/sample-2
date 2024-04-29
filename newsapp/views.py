from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.db.models import Avg, Case, Count, F, Max, Min, Prefetch, Q, Sum, When
from .models import *



def index(request):
    authors = Author.objects.all()
    posts = Post.objects.all()

    context = {
     'title':'newapp',
     'authors': authors,
     'posts': posts,

    }
    return render(request, 'newsapp/index.html', context=context)


# def shell(request):
#     aleks = get_object_or_404(Author, pk=1)
#     Post.objects.create(title='title1', author=aleks, type_of=Post.article, content='content1')
#
#     context = {
#         'done':'DONE!',
#         'title': 'shell',
#
#     }
#     return render(request, 'newsapp/index.html', context=context)
