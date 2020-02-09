from django.urls import path, include
from django.contrib import admin
import home.views
admin.autodiscover()

urlpatterns = [
    path("", home.views.index, name="home-index"),
    path("admin/", admin.site.urls),
]
