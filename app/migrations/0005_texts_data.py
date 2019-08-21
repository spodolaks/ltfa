from __future__ import unicode_literals

from django.db import migrations
from ..models import Text

def create_texts(apps, schema_editor):
    Text(title='Sazināties ar mums', slug='footer_1', content='<a href="tel:+371 245 03 553">+371 245 03 553</a><br/><a href="mailto:office@ltfa.lv">office@ltfa.lv</a>').save();
    Text(title='Mūsu rekvizīti', slug='footer_2', content='Biedrība „Latvijas Telpu futbola asociācija”<br/>Reģ.Nr.:40008228829<br/>Grostonas 6b, Rīga, Latvija, LV-1013<br/>Nor. konts : LV32PARX0016341480001<br/>AS „Citadele banka”<br/>Kods: PARXLV22').save();
    Text(title='Apmeklējiet mūs', slug='footer_3', content='Grostonas 6b, 1 - 412, 4.stāvs<br/>Rīga, Latvija<br/>LV-1013').save();
    Text(title='Darba laiks', slug='footer_4', content='I-V: 09.00 - 14.00<br/>VI-VII: brīvdienas').save();


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_text'),
    ]

    operations = [
        migrations.RunPython(create_texts)
    ]
