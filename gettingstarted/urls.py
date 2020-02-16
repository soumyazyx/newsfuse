from django.conf import settings 
from django.conf.urls.static import static 
from django.urls import path, include
from django.contrib import admin
import home.views
admin.autodiscover()

urlpatterns = [
    path("", home.views.index, name="home-index"),
    path('', include('allauth.urls')),
    path("admin/", admin.site.urls),
    path("NASA/", home.views.nasa),
    path("ESA/", home.views.esa),
]
