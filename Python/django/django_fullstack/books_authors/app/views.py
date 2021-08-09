#import django commands to allow us to use render/redirect when needed in views.py
from django.shortcuts import render, redirect
#import models.py allows us to link model keys when needed in views.py
from .models import Author, Book

# Create your views here.

def index(request):
    context = {
        #remember context syntax: 'keys' = "value"
        #{{ keys }} in html template will get the value to display on our browser
        'authors': Author.objects.all(),
        'books': Book.objects.all()
    }
    return render (request, 'index.html', context)