from django.urls import path, include
from django.contrib import admin

admin.autodiscover()

import home.views

urlpatterns = [
    path("", home.views.index, name="home-index"),
    path("admin/", admin.site.urls),
]
