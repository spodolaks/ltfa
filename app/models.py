from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=255);
    content = models.TextField(blank=True);
    slug = models.SlugField(blank=True, unique=True);
    show_in_menu = models.BooleanField(default=False);
    is_home_page = models.BooleanField(default=False);
    layout = models.FilePathField(path='templates/app');
    def __str__(self):
        return self.title

class Text(models.Model):
    title = models.CharField(max_length=255);
    content = models.TextField(blank=True);
    slug = models.SlugField(blank=True, unique=True);
    def __str__(self):
        return self.title
