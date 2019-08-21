from __future__ import unicode_literals

from django.db import migrations
from ..models import Page

def create_pages(apps, schema_editor):
    Page(title='Galvena', slug='', is_home_page=True, layout='templates/app/home.html').save();
    Page(title='Jaunumi', slug='news', show_in_menu=True, layout='templates/app/news.html').save();
    Page(title='Turnīri', slug='tournaments', show_in_menu=True, layout='templates/app/tournaments.html').save();
    Page(title='Notikumi', slug='events', show_in_menu=True, layout='templates/app/events.html').save();
    Page(title='Dokumenti', slug='documents', show_in_menu=True, layout='templates/app/documents.html').save();
    Page(title='Par mums', slug='about_us', show_in_menu=True, layout='templates/app/aboutus.html').save();
    Page(title='E-veikals', slug='e_shop', show_in_menu=True, layout='templates/app/eshop.html').save();


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_page'),
    ]

    operations = [
        migrations.RunPython(create_pages)
    ]
