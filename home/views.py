from django.shortcuts import render
from django.http import HttpResponse
from .models import Signup, Article
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

def nasa(request):

    email_list = Signup.objects.all()

    if request.method == 'POST':
        email = request.POST['email']
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()

    feed = feedparser.parse('https://www.nasa.gov/rss/dyn/breaking_news.rss')
    for entry in feed.entries:
        new_article = Article()
        new_article.link = entry['link']
        new_article.title = entry['title']
        new_article.author = feed['feed']['author']
        new_article.summary = entry['summary']
        new_article.published = entry['published']
        new_article.article_id = entry['dc_identifier']
        new_article.author_img_url = ''
        new_article.article_img_url = entry['links'][1]['href']
        new_article.save()

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
