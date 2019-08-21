from __future__ import unicode_literals

from django.db import migrations
from ..models import Social

def create_social(apps, schema_editor):
    Social(title='Facebook', url='https://www.facebook.com/LTFA.LV/', icon='fb').save();
    Social(title='Instagram', url='https://www.instagram.com/ltfa_futsal.official/', icon='instagram').save();
    Social(title='Tweeter', url='https://twitter.com/ltfa_futsal', icon='tweeter').save();
    Social(title='Youtube', url='https://www.youtube.com/channel/UCen2zwEsmQVH2TzMm-SjMAQ', icon='youtube').save();


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_social'),
    ]

    operations = [
        migrations.RunPython(create_social)
    ]
