from django.db import models
from django.utils.safestring import mark_safe
import re
from ckeditor_uploader.fields import RichTextUploadingField
def getfirst(el):
    return el[0]

class Page(models.Model):
    title = models.CharField(max_length=255);
    parent = models.ForeignKey("self", blank=True, null=True, on_delete=models.CASCADE)
    content = RichTextUploadingField(blank=True);
    slug = models.SlugField(blank=True, unique=True);
    show_in_menu = models.BooleanField(default=False);
    is_home_page = models.BooleanField(default=False);
    layout = models.FilePathField(path='templates/app');
    published = models.BooleanField(default=True)
    order = models.IntegerField(default=-1)

    class Meta:
        ordering = ['order', 'title']

    @classmethod
    def reorder(cls):
        pages = list(cls.objects.filter(parent__isnull=True).order_by("order"))
        i = 0;
        for p in pages:
            p.order = i;
            i += 1;
            pages[i:i] = list(p.get_children())
        for i in range(len(pages)):
            super(Page, pages[i]).save()

    def save(self, reorder=True, *args, **kwargs):
        if self.order < 0:
            self.order = Page.objects.count()
        super(Page, self).save(*args, **kwargs)
        if reorder:
            self.reorder();

    @mark_safe
    def get_display_title(self,get_name=True):
        if self.parent:
            return u'%s|- %s' % (self.get_spaces(), self.title)
        else:
            return u'%s' % self.title

    get_display_title.allow_tags = True
    get_display_title.admin_order_field = 'order'
    get_display_title.short_description = 'Title'

    @mark_safe
    def order_buttons(self):
        return "<a href='order/dec/"+str(self.pk)+"'>&#9650;</a><a href='order/inc/"+str(self.pk)+"'>&#9660;</a>"
    order_buttons.short_description = 'Order'
    order_buttons.allow_tags = True

    def get_spaces(self):
        if self.parent:
            return u'%s.&#xa0;&#xa0;&#xa0;&#xa0;&#xa0;&#xa0;' % self.parent.get_spaces()
        return u''

    def get_children(self):
        return Page.objects.filter(parent=self.pk);

    def __str__(self):
        if self.parent:
            return u'%s -> %s' % (self.parent.__str__(), self.title)
        return u'%s' % (self.title)

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
