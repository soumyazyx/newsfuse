from django.db import models


class Signup(models.Model):
    email = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Article(models.Model):

    link = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=200, null=True, blank=True)
    summary = models.TextField()
    added_ts = models.DateTimeField(auto_now_add=True)
    published = models.CharField(max_length=255)
    article_id = models.CharField(max_length=255)
    author_img_url = models.CharField(max_length=255, null=True, blank=True)
    article_img_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=255)    
    added_ts = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"


class Feed(models.Model):
    title = models.CharField(max_length=255)
    rss_url = models.TextField()
    added_ts = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Feeds'


class Category_Feed(models.Model):
    feed_id = models.ForeignKey(Feed, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return "{}-{}".format(self.category_id, self.feed_id)