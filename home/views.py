from django.shortcuts import render
from django.http import HttpResponse
from .models import Signup

import feedparser


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
