from __future__ import unicode_literals

from django.db import migrations
from django.contrib.auth.admin import User
import datetime

def create_superuser(apps, schema_editor):
    superuser = User()
    superuser.is_active = True
    superuser.is_superuser = True
    superuser.is_staff = True
    superuser.username = 'admin'
    superuser.email = 'admin@ltfa.lv'
    superuser.last_login = datetime.datetime.now()
    superuser.set_password('nimda')
    superuser.save()


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.RunPython(create_superuser)
    ]
