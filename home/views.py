from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Signup, Article
import feedparser
import requests


def index(request):

    email_list = Signup.objects.all()
    if request.method == 'POST':
        email = request.POST['email']
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()

    feed = feedparser.parse('https://www.nasa.gov/rss/dyn/breaking_news.rss')
    context = {
        'feed': feed,
        'email_list': email_list
    }
    return render(request, "index.html", context)


def nasa(request):

    email_list = Signup.objects.all()

    if request.method == 'POST':
        email = request.POST['email']
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()

    r = requests.get('https://getmefeed.herokuapp.com/NASA/')
    feed = r.json()
    context = {
        'feed': feed,
        'email_list': email_list
    }
    return render(request, "index.html", context)


def esa(request):

    email_list = Signup.objects.all()
    if request.method == 'POST':
        email = request.POST['email']
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()

    feed = feedparser.parse('https://www.nasa.gov/rss/dyn/breaking_news.rss')
    context = {
        'feed': feed,
        'email_list': email_list
    }
    return render(request, "post.html", context)
