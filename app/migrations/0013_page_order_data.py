from __future__ import unicode_literals

from django.db import migrations
from django.core.files.images import ImageFile
from ..models import Page

def create_order(apps, schema_editor):
    pages = Page.objects.all();
    for index, page in enumerate(pages):
        page.order = index;
        page.save();

class Migration(migrations.Migration):
    dependencies = [
        ('app', '0012_page_order'),
    ]

    operations = [
        migrations.RunPython(create_order)
    ]
