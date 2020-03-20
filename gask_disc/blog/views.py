from django.shortcuts import render
from django.views.generic import ListView
from .models import Posts


def home(request):
    context = {
        'posts': Posts.objects.all()
    }
    return render(request, 'blog/home.html', context)


class Pos


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
