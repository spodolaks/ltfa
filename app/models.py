from django.db import models
import re
from ckeditor_uploader.fields import RichTextUploadingField


class Page(models.Model):
    title = models.CharField(max_length=255);
    content = RichTextUploadingField(blank=True);
    slug = models.SlugField(blank=True, unique=True);
    show_in_menu = models.BooleanField(default=False);
    is_home_page = models.BooleanField(default=False);
    layout = models.FilePathField(path='templates/app');
    order = models.IntegerField(default=1)
    def __str__(self):
        return self.title

class Text(models.Model):
    title = models.CharField(max_length=255);
    content = RichTextUploadingField(blank=True);
    slug = models.SlugField(blank=True, unique=True);
    def __str__(self):
        return self.title

class Social(models.Model):
    title = models.CharField(max_length=255);
    url = models.URLField();
    ICON_CHOICES = [
        ('fb', 'Facebook'),
        ('instagram', 'Instagram'),
        ('tweeter', 'Tweeter'),
        ('youtube', 'Youtube'),
    ]
    icon = models.CharField(
        max_length=10,
        choices=ICON_CHOICES,
        default='fb',
    )
    def __str__(self):
        return self.title

class Sponsor(models.Model):
    title = models.CharField(max_length=255);
    url = models.URLField(blank=True);
    image = models.ImageField();
    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=255);
    slug = models.SlugField(unique=True);
    date = models.DateTimeField(auto_now=True);
    content = RichTextUploadingField(blank=True);
    image = models.ImageField(blank=True);
    class Meta:
        verbose_name_plural = "News"
    def __str__(self):
        return self.title
    def excerpt(self, size=200):
        result = re.sub(re.compile('<.*?>'), '', self.content)
        return result[0:size];
    def datpublished(self):
        return self.date.strftime('%d.%m.%Y')
