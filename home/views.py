from django.shortcuts import render
from django.http import HttpResponse
import feedparser


def index(request):
    feed = feedparser.parse('https://www.nasa.gov/rss/dyn/breaking_news.rss')
    context = {
        'feed': feed
    }
    return render(request, "index.html", context)
