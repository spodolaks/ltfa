from __future__ import unicode_literals

from django.db import migrations
from django.core.files.images import ImageFile
from ..models import Page

def create_pages(apps, schema_editor):
    Page(title='Galvena', slug='', is_home_page=True, layout='templates/app/home.html').save();
    Page(title='Jaunumi', slug='news', show_in_menu=True, layout='templates/app/news.html').save();
    Page(title='Turnīri', slug='tournaments', show_in_menu=True, layout='templates/app/tournaments.html').save();
    Page(title='Notikumi', slug='events', show_in_menu=True, layout='templates/app/events.html').save();
    doc = Page(title='Dokumenti', slug='documents', show_in_menu=True, layout='templates/app/documents.html');
    doc.save();
    Page(
        title='Dokumenti #1',
        slug='documents_1',
        parent=doc,
        is_visible=False,
        content='<h6>LTFA SACENSĪBU REGLAMENTI:</h6><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><h6>Latvijas telpu futbola Virslīga:</h6><p><br /><a href="#">Reglaments</a></p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><h6>Latvijas telpu futbola 1.līga:</h6><p><br /><a href="#">Reglaments un pieteikuma forma</a></p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><h6>Latvijas telpu futbola kauss:</h6><p><br /><a href="#">Reglaments un pieteikuma forma</a></p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><h6>U-19 čempionāts:</h6><p><br /><a href="#">Reglaments un pieteikuma forma</a></p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><h6>Jaunatnes čempionāts (2005.dz.g un 2007.dz.g):</h6><p><br /><a href="#">Reglaments un pieteikuma forma</a></p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><h6>Veterānu čempionāts:</h6><p><br /><a href="#">Reglaments un pieteikuma forma</a><br /><br /><a href="#">Čempionāta kalendārs</a></p>'
    ).save();
    Page(
        title='Dokumenti #2',
        slug='documents_2',
        parent=doc,
        is_visible=False,
        content='<h6>JOMA Jaungada kauss:</h6><p><br /><a href="#">Reglaments un pieteikuma forma</a></p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><h6>Skolu kauss telpu futbolā:</h6><p><br /><a href="#">Nolikums un pieteikuma veidlapa</a></p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><h6>Karsējmeiteņu sacensības:</h6><p><br /><a href="#">Nolikums un pieteikuma forma</a></p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><h6>Latvijas Universiāde telpu futbolā:</h6><p><br /><a href="#">Nolikums un pieteikuma forma</a></p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><h6>LTFA BIEDRI:</h6><p><br /><a href="#">LTFA Statūti</a><br /><br /><a href="#">LTFA Biedru reģistrācijas/pārreģistrācijas iesniegums</a><br /><br /><a href="#">LTFA Kongresa pieteikuma pilvara</a><br /><br /><a href="#">LTFA Biedrības gada pārskats</a><br /><br /><a href="#">LTFA Neatkarīgu revidentu ziņojums</a><br /><br /><a href="#">LTFA Kongresa materiāls: 2017. 2018</a><br /><br /><a href="#">LTFA Kongresa protokols: 2017. 2018</a><br /><br /><br />* nav publicēts</p>'
    ).save();
    abus = Page(title='Par mums', slug='about_us', show_in_menu=True, layout='templates/app/aboutus.html');
    abus.save();
    Page(
        title='Vēsture',
        slug='vesture',
        parent=abus,
        is_visible=False,
        content='<p>Latvijas Telpu futbola asociācijas pirmsākumi ir meklējami 2014. gada 19. septembrī. notiekot dibinā&scaron;anas svinīgajai kopsapulcei Elektrum Olimpiskajā centrā. kurā piedalījās Latvijas telpu futbola klubu pārstāvji - Latvijas Futbola Federācijas biedri. biedru kandidāti. kā arī interesenti.</p><p>&nbsp;</p><p>Par organizācijas Valdes priek&scaron;sēdētāju asociācijas dibinā&scaron;anas brīdī tika apstiprināts tās izveides ieceres autors. ilggadējais Latvijas telpu futbola čempionu FK &quot;Nikars&quot; un valstsvienības spēlētājs Vadims Ļa&scaron;enko. Par LTFA Valdes locekļiem tika ievēlēti Anatolijs Romaņuks. Raimonds Valts. Arturs Gaidels. Eduards Borisevičs. Edgars Pukinsks. Artūrs &Scaron;ketovs. Maksims Koļu&scaron;kins un Andrejs Baumanis. 2015. gada 13. augustā tika apstiprināta Edgara Pukinska Optibet Virslīga izstā&scaron;anās no LTFA Valdes un kop&scaron; 2016. 30. septembra. kad notika tre&scaron;ais LTFA Kongress. LTFA Valdi papildināja Mārtiņ&scaron; Petrovs. Tajā pa&scaron;ā gadā par LTFA par izpilddirektoru kļuva Eduards Borisevičs. kur&scaron; vairs nevarēja pildīt valdes locekļa funkcijas. Vēl pēc gada pār LTFA valdes locekli kļuva treneris Guntis Spuņciema Sporta halle Apīnis. 2018. gada kongresā valdē tika ievēlēti Kiazo Leladze un Emīls Latkovskis. bet darbu valdē pabeidza Anatolijs Romaņuks un Maksims Koļu&scaron;kins. 2018. gada rudenī Boriseviču izpilddirektora amatā nomainīja Jānis Narti&scaron;s.</p><p>&nbsp;</p><p><img alt="" src="/static/images/about-us-people.png" style="height:527px; width:986px" /><br />&nbsp;</p>'
    ).save();
    Page(
        title='Sasniegumi',
        slug='sasniegumi',
        parent=abus,
        is_visible=False,
        content='<p>Uz &scaron;o dienu telpu futbols ir uzņēmis pareizo attīstības ceļu Latvijā un pamazām kļūst par pus profesionālu sporta veidu Latvijā. Pēdējo divu gadu laikā ir pieaudzis pus profesionālu klubu, spēlētāju, amatieru telpu futbolistu un komandu skaits. Ja līdz asociācijas izveido&scaron;anai bez Rīgas komandām augstākā līmeņa turnīros bija pārstāvētas vien Daugavpils un Ventspils, tad tagad Virslīgas, Pirmās līgas un Latvijas kausa turnīros atrodamas dalībnieces jau no 12 dažādiem reģioniem.</p><p>&nbsp;</p><p>Viens no asociācijas attīstības stūrakmeņiem, LTFA organizētais Skolu čempionāts, pērn ļāva piepulcināt &scaron;im sporta veidam vairāk nekā 300 jaunie&scaron;u, piesaistot aizvien jaunu dalībnieku, kā arī sadarbības partneru interesi, kas ļauj pieteikt &scaron;o turnīru kā nozīmīgu, ikgadēju telpu futbola notikumu LTFA kalendārā.</p>'
    ).save();
    kol = Page(title='LTFA Kolektivs', slug='ltfa_kolektivs', parent=abus, is_visible=False);
    kol.save()
    valde_1 = Page(title='LTFA Valde', slug='ltfa_valde', parent=kol, is_visible=False);
    valde_1.save();
    Page(title='Vadims Lasenko', slug='person_1', parent=valde_1, is_visible=False, image=ImageFile(open("static/images/board-member-1.png", "rb")), content='Valdes priekssedetajs').save();
    Page(title='Vadims Lasenko', slug='person_2', parent=valde_1, is_visible=False, image=ImageFile(open("static/images/board-member-1.png", "rb")), content='Valdes priekssedetajs').save();
    Page(title='Vadims Lasenko', slug='person_3', parent=valde_1, is_visible=False, image=ImageFile(open("static/images/board-member-1.png", "rb")), content='Valdes priekssedetajs').save();
    Page(title='Vadims Lasenko', slug='person_4', parent=valde_1, is_visible=False, image=ImageFile(open("static/images/board-member-1.png", "rb")), content='Valdes priekssedetajs').save();
    Page(title='Vadims Lasenko', slug='person_5', parent=valde_1, is_visible=False, image=ImageFile(open("static/images/board-member-1.png", "rb")), content='Valdes priekssedetajs').save();
    valde_2 = Page(title='LTFA Darbinieki', slug='ltfa_darbinieki', parent=kol, is_visible=False);
    valde_2.save();
    Page(title='Vadims Lasenko', slug='person_1', parent=valde_2, is_visible=False, image=ImageFile(open("static/images/board-member-1.png", "rb")), content='Valdes priekssedetajs').save();
    Page(title='Vadims Lasenko', slug='person_2', parent=valde_2, is_visible=False, image=ImageFile(open("static/images/board-member-1.png", "rb")), content='Valdes priekssedetajs').save();
    Page(title='Vadims Lasenko', slug='person_3', parent=valde_2, is_visible=False, image=ImageFile(open("static/images/board-member-1.png", "rb")), content='Valdes priekssedetajs').save();
    Page(title='E-veikals', slug='e_shop', show_in_menu=True, published=False, layout='templates/app/eshop.html').save();


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_page'),
    ]

    operations = [
        migrations.RunPython(create_pages)
    ]
