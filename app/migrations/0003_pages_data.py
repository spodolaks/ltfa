from __future__ import unicode_literals

from django.db import migrations
from ..models import Page

def create_pages(apps, schema_editor):
    Page(title='Galvena', slug='', is_home_page=True, layout='templates/app/home.html').save();
    Page(title='Jaunumi', slug='news', show_in_menu=True, layout='templates/app/news.html').save();
    Page(title='Turnīri', slug='tournaments', show_in_menu=True, layout='templates/app/tournaments.html').save();
    Page(title='Notikumi', slug='events', show_in_menu=True, layout='templates/app/events.html').save();
    doc = Page(title='Dokumenti', slug='documents', show_in_menu=True, layout='templates/app/documents.html');
    doc.save();
    Page(title='Dokumenti #1', slug='documents_1', parent=doc, content='<h6>LTFA SACENSĪBU REGLAMENTI:</h6><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><h6>Latvijas telpu futbola Virslīga:</h6><p><br /><a href="#">Reglaments</a></p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><h6>Latvijas telpu futbola 1.līga:</h6><p><br /><a href="#">Reglaments un pieteikuma forma</a></p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><h6>Latvijas telpu futbola kauss:</h6><p><br /><a href="#">Reglaments un pieteikuma forma</a></p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><h6>U-19 čempionāts:</h6><p><br /><a href="#">Reglaments un pieteikuma forma</a></p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><h6>Jaunatnes čempionāts (2005.dz.g un 2007.dz.g):</h6><p><br /><a href="#">Reglaments un pieteikuma forma</a></p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><h6>Veterānu čempionāts:</h6><p><br /><a href="#">Reglaments un pieteikuma forma</a><br /><br /><a href="#">Čempionāta kalendārs</a></p>').save();
    Page(title='Dokumenti #2', slug='documents_2', parent=doc, content='<h6>JOMA Jaungada kauss:</h6><p><br /><a href="#">Reglaments un pieteikuma forma</a></p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><h6>Skolu kauss telpu futbolā:</h6><p><br /><a href="#">Nolikums un pieteikuma veidlapa</a></p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><h6>Karsējmeiteņu sacensības:</h6><p><br /><a href="#">Nolikums un pieteikuma forma</a></p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><h6>Latvijas Universiāde telpu futbolā:</h6><p><br /><a href="#">Nolikums un pieteikuma forma</a></p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><h6>LTFA BIEDRI:</h6><p><br /><a href="#">LTFA Statūti</a><br /><br /><a href="#">LTFA Biedru reģistrācijas/pārreģistrācijas iesniegums</a><br /><br /><a href="#">LTFA Kongresa pieteikuma pilvara</a><br /><br /><a href="#">LTFA Biedrības gada pārskats</a><br /><br /><a href="#">LTFA Neatkarīgu revidentu ziņojums</a><br /><br /><a href="#">LTFA Kongresa materiāls: 2017. 2018</a><br /><br /><a href="#">LTFA Kongresa protokols: 2017. 2018</a><br /><br /><br />* nav publicēts</p>').save();
    Page(title='Par mums', slug='about_us', show_in_menu=True, layout='templates/app/aboutus.html').save();
    Page(title='E-veikals', slug='e_shop', show_in_menu=True, layout='templates/app/eshop.html').save();


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_page'),
    ]

    operations = [
        migrations.RunPython(create_pages)
    ]
