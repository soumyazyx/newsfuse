from django.contrib import admin
from home.models import Signup, Article, Category, Feed, Category_Feed

admin.site.register(Signup)
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Feed)
admin.site.register(Category_Feed)
