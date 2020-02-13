# Generated by Django 2.2.7 on 2020-02-13 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_img_url',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='author_img_url',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
