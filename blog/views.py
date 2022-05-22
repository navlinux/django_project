from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author' : 'Navneet Raj',
        'title' : 'Blog Post 1',
        'content' : 'First post content',
        'date_posted' : 'May 22, 2022'
    },
    {
        'author' : 'Amay Raj',
        'title' : 'Blog Post 2',
        'content' : 'Second post content',
        'date_posted' : 'May 23, 2022'
    }
]


def home(request):
    context = {
        'posts' : posts,
        'title' : 'Home'
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title' : 'About'})