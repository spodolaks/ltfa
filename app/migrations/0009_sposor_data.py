from __future__ import unicode_literals

from django.db import migrations
from django.core.files.images import ImageFile
from ..models import Sponsor

def create_sponsor(apps, schema_editor):
    Sponsor(title='LFF.lv', url='https://lff.lv/', image=ImageFile(open("static/images/sponsor-1.jpg", "rb"))).save();
    Sponsor(title='Fédération Internationale de Football Association', url='http://www.fifa.com/futsal/index.html', image=ImageFile(open("static/images/sponsor-2.jpg", "rb"))).save();
    Sponsor(title='JOMA', url='http://www.joma-sport.lv/', image=ImageFile(open("static/images/sponsor-3.jpg", "rb"))).save();
    Sponsor(title='OPTIBET', url='http://optibet.lv', image=ImageFile(open("static/images/sponsor-4.jpg", "rb"))).save();
    Sponsor(title='UEFA', url='http://www.uefa.com/futsalcup/index.html', image=ImageFile(open("static/images/sponsor-5.jpg", "rb"))).save();
    Sponsor(title='Evolution Gaming', url='https://www.evolutiongaming.com/', image=ImageFile(open("static/images/sponsor-6.jpg", "rb"))).save();
    Sponsor(title='Futsal Planet', url='http://www.futsalplanet.com', image=ImageFile(open("static/images/sponsor-7.jpg", "rb"))).save();
    Sponsor(title='Sportacentrs', url='http://sportacentrs.com/futzals/', image=ImageFile(open("static/images/sponsor-8.jpg", "rb"))).save();
    Sponsor(title='Memory Water', url='http://www.memorywater.com', image=ImageFile(open("static/images/sponsor-9.jpg", "rb"))).save();
    Sponsor(title='Sportlex', url='https://www.sportlex.lv/lv/', image=ImageFile(open("static/images/sponsor-10.jpg", "rb"))).save();
    Sponsor(title='XL Print', url='http://www.xlprint.lv/', image=ImageFile(open("static/images/sponsor-11.jpg", "rb"))).save();
    Sponsor(title='Restorāns Armenia ', url='http://www.restoranarmenia.lv/', image=ImageFile(open("static/images/sponsor-12.jpg", "rb"))).save();
    Sponsor(title='Midland oil', url='http://www.midlandoil.lv/index.php?lng=lv&part=start&part2=&part3=&part4=', image=ImageFile(open("static/images/sponsor-13.jpg", "rb"))).save();
    Sponsor(title='RISEBA', url='http://www.riseba.lv/lv/', image=ImageFile(open("static/images/sponsor-14.jpg", "rb"))).save();
    Sponsor(title='Rīgas Futbola federācija', url='http://riga.lff.lv/', image=ImageFile(open("static/images/sponsor-15.jpg", "rb"))).save();
    Sponsor(title='Ghetto Games', url='https://www.ghetto.lv/', image=ImageFile(open("static/images/sponsor-16.jpg", "rb"))).save();
    Sponsor(title='Mercure Hotel Riga', url='http://www.mercureriga.lv/', image=ImageFile(open("static/images/sponsor-17.jpg", "rb"))).save();


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0008_sponsor'),
    ]

    operations = [
        migrations.RunPython(create_sponsor)
    ]
