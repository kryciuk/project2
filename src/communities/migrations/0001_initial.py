# Generated by Django 5.0.7 on 2024-08-10 08:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, null=True)),
                ('city', models.CharField(choices=[('Aleksandrów Kujawski', 'Aleksandrów Kujawski'), ('Andrychów', 'Andrychów'), ('Aleksandrów Łódzki', 'Aleksandrów Łódzki'), ('Annopol', 'Annopol'), ('Alwernia', 'Alwernia'), ('Augustów', 'Augustów'), ('Babimost', 'Babimost'), ('Barczewo', 'Barczewo'), ('Barwice', 'Barwice'), ('Baborów', 'Baborów'), ('Bardo', 'Bardo'), ('Bełchatów', 'Bełchatów'), ('Baranów Sandomierski', 'Baranów Sandomierski'), ('Barlinek', 'Barlinek'), ('Bełżyce', 'Bełżyce'), ('Barcin', 'Barcin'), ('Bartoszyce', 'Bartoszyce'), ('Będzin', 'Będzin'), ('Biała', 'Biała'), ('Biecz', 'Biecz'), ('Bieżuń', 'Bieżuń'), ('Biała Piska', 'Biała Piska'), ('Bielawa', 'Bielawa'), ('Biłgoraj', 'Biłgoraj'), ('Biała Podlaska', 'Biała Podlaska'), ('Bielsk Podlaski', 'Bielsk Podlaski'), ('Biskupiec', 'Biskupiec'), ('Biała Rawska', 'Biała Rawska'), ('Bielsko-Biała', 'Bielsko-Biała'), ('Bisztynek', 'Bisztynek'), ('Białobrzegi', 'Białobrzegi'), ('Bieruń', 'Bieruń'), ('Blachownia', 'Blachownia'), ('Białogard', 'Białogard'), ('Bierutów', 'Bierutów'), ('Błaszki', 'Błaszki'), ('Biały Bór', 'Biały Bór'), ('Błażowa', 'Błażowa'), ('Białystok', 'Białystok'), ('Błonie', 'Błonie'), ('Bobolice', 'Bobolice'), ('Bolków', 'Bolków'), ('Brzeg', 'Brzeg'), ('Bobowa', 'Bobowa'), ('Borek Wielkopolski', 'Borek Wielkopolski'), ('Brzeg Dolny', 'Brzeg Dolny'), ('Bochnia', 'Bochnia'), ('Borne Sulinowo', 'Borne Sulinowo'), ('Brzesko', 'Brzesko'), ('Bodzentyn', 'Bodzentyn'), ('Braniewo', 'Braniewo'), ('Brzeszcze', 'Brzeszcze'), ('Bogatynia', 'Bogatynia'), ('Brańsk', 'Brańsk'), ('Brześć Kujawski', 'Brześć Kujawski'), ('Boguchwała', 'Boguchwała'), ('Brodnica', 'Brodnica'), ('Brzeziny', 'Brzeziny'), ('Boguszów-Gorce', 'Boguszów-Gorce'), ('Brok', 'Brok'), ('Brzostek', 'Brzostek'), ('Bojanowo', 'Bojanowo'), ('Brusy', 'Brusy'), ('Brzozów', 'Brzozów'), ('Bolesławiec', 'Bolesławiec'), ('Brwinów', 'Brwinów'), ('Buk', 'Buk'), ('Bydgoszcz', 'Bydgoszcz'), ('Bukowno', 'Bukowno'), ('Bystrzyca Kłodzka', 'Bystrzyca Kłodzka'), ('Busko Zdrój', 'Busko Zdrój'), ('Bytom', 'Bytom'), ('Bychawa', 'Bychawa'), ('Bytom Odrzański', 'Bytom Odrzański'), ('Byczyna', 'Byczyna'), ('Bytów', 'Bytów'), ('Cedynia', 'Cedynia'), ('Chocianów', 'Chocianów'), ('Chojnów', 'Chojnów'), ('Chełm', 'Chełm'), ('Chociwel', 'Chociwel'), ('Choroszcz', 'Choroszcz'), ('Chełmek', 'Chełmek'), ('Chocz', 'Chocz'), ('Chorzele', 'Chorzele'), ('Chełmno', 'Chełmno'), ('Chodecz', 'Chodecz'), ('Chorzów', 'Chorzów'), ('Chełmża', 'Chełmża'), ('Chodzież', 'Chodzież'), ('Choszczno', 'Choszczno'), ('Chęciny', 'Chęciny'), ('Chojna', 'Chojna'), ('Chrzanów', 'Chrzanów'), ('Chmielnik', 'Chmielnik'), ('Chojnice', 'Chojnice'), ('Ciechanowiec', 'Ciechanowiec'), ('Czarna Białostocka', 'Czarna Białostocka'), ('Czerniejewo', 'Czerniejewo'), ('Ciechanów', 'Ciechanów'), ('Czarna Woda', 'Czarna Woda'), ('Czersk', 'Czersk'), ('Ciechocinek', 'Ciechocinek'), ('Czarne', 'Czarne'), ('Czerwieńsk', 'Czerwieńsk'), ('Cieszanów', 'Cieszanów'), ('Czarnków', 'Czarnków'), ('Czerwionka-Leszczyny', 'Czerwionka-Leszczyny'), ('Cieszyn', 'Cieszyn'), ('Czchów', 'Czchów'), ('Częstochowa', 'Częstochowa'), ('Ciężkowice', 'Ciężkowice'), ('Czechowice-Dziedzice', 'Czechowice-Dziedzice'), ('Człopa', 'Człopa'), ('Cybinka', 'Cybinka'), ('Czeladź', 'Czeladź'), ('Człuchów', 'Człuchów'), ('Czaplinek', 'Czaplinek'), ('Czempiń', 'Czempiń'), ('Czyżew', 'Czyżew'), ('Daleszyce', 'Daleszyce'), ('Debrzno', 'Debrzno'), ('Dobra (Turek County)', 'Dobra (Turek County)'), ('Darłowo', 'Darłowo'), ('Dębica', 'Dębica'), ('Dobre Miasto', 'Dobre Miasto'), ('Dąbie', 'Dąbie'), ('Dęblin', 'Dęblin'), ('Dobrodzień', 'Dobrodzień'), ('Dąbrowa Białostocka', 'Dąbrowa Białostocka'), ('Dębno', 'Dębno'), ('Dobrzany', 'Dobrzany'), ('Dąbrowa Górnicza', 'Dąbrowa Górnicza'), ('Dobczyce', 'Dobczyce'), ('Dobrzyca', 'Dobrzyca'), ('Dąbrowa Tarnowska', 'Dąbrowa Tarnowska'), ('Dobiegniew', 'Dobiegniew'), ('Dobrzyń nad Wisłą', 'Dobrzyń nad Wisłą'), ('Dąbrowa Tarnowska', 'Dąbrowa Tarnowska'), ('Dobra (Łobez County)', 'Dobra (Łobez County)'), ('Dolsk', 'Dolsk'), ('Drawno', 'Drawno'), ('Drzewica', 'Drzewica'), ('Działoszyce', 'Działoszyce'), ('Drawsko Pomorskie', 'Drawsko Pomorskie'), ('Dukla', 'Dukla'), ('Działoszyn', 'Działoszyn'), ('Drezdenko', 'Drezdenko'), ('Duszniki Zdrój', 'Duszniki Zdrój'), ('Dzierzgoń', 'Dzierzgoń'), ('Drobin', 'Drobin'), ('Dynów', 'Dynów'), ('Dzierżoniów', 'Dzierżoniów'), ('Drohiczyn', 'Drohiczyn'), ('Działdowo', 'Działdowo'), ('Dziwnów', 'Dziwnów'), ('Elbląg', 'Elbląg'), ('Ełk', 'Ełk'), ('Frampol', 'Frampol'), ('Frombork', 'Frombork'), ('Garwolin', 'Garwolin'), ('Gliwice', 'Gliwice'), ('Głuchołazy', 'Głuchołazy'), ('Gąbin', 'Gąbin'), ('Głogów', 'Głogów'), ('Głuszyca', 'Głuszyca'), ('Gdańsk', 'Gdańsk'), ('Głogów Małopolski', 'Głogów Małopolski'), ('Gniew', 'Gniew'), ('Gdynia', 'Gdynia'), ('Głogówek', 'Głogówek'), ('Gniewkowo', 'Gniewkowo'), ('Giżycko', 'Giżycko'), ('Głowno', 'Głowno'), ('Gniezno', 'Gniezno'), ('Glinojeck', 'Glinojeck'), ('Głubczyce', 'Głubczyce'), ('Gniewkowo', 'Gniewkowo'), ('Gogolin', 'Gogolin'), ('Goniądz', 'Goniądz'), ('Gostyń', 'Gostyń'), ('Golczewo', 'Golczewo'), ('Gorlice', 'Gorlice'), ('Gozdnica', 'Gozdnica'), ('Goleniów', 'Goleniów'), ('Gorzów Śląski', 'Gorzów Śląski'), ('Góra', 'Góra'), ('Golina', 'Golina'), ('Gorzów Wielkopolski', 'Gorzów Wielkopolski'), ('Góra Kalwaria', 'Góra Kalwaria'), ('Gołańcz', 'Gołańcz'), ('Gostynin', 'Gostynin'), ('Górzno', 'Górzno'), ('Gołdap', 'Gołdap'), ('Grabów nad Prosną', 'Grabów nad Prosną'), ('Grodzisk Wielkopolski', 'Grodzisk Wielkopolski'), ('Gryfice', 'Gryfice'), ('Grajewo', 'Grajewo'), ('Grójec', 'Grójec'), ('Gryfino', 'Gryfino'), ('Grodków', 'Grodków'), ('Grudziądz', 'Grudziądz'), ('Gryfów Śląski', 'Gryfów Śląski'), ('Grodzisk Mazowiecki', 'Grodzisk Mazowiecki'), ('Grybów', 'Grybów'), ('Gubin', 'Gubin'), ('Hajnówka', 'Hajnówka'), ('Halinów', 'Halinów'), ('Hel', 'Hel'), ('Hrubieszów', 'Hrubieszów'), ('Iława', 'Iława'), ('Inowrocław', 'Inowrocław'), ('Iłowa', 'Iłowa'), ('Ińsko', 'Ińsko'), ('Iłża', 'Iłża'), ('Iwonicz Zdrój', 'Iwonicz Zdrój'), ('Imielin', 'Imielin'), ('Izbica Kujawska', 'Izbica Kujawska'), ('Jabłonowo Pomorskie', 'Jabłonowo Pomorskie'), ('Jastrowie', 'Jastrowie'), ('Jelcz-Laskowice', 'Jelcz-Laskowice'), ('Janikowo', 'Janikowo'), ('Jastrzębie Zdrój', 'Jastrzębie Zdrój'), ('Jelenia Góra', 'Jelenia Góra'), ('Janowiec Wielkopolski', 'Janowiec Wielkopolski'), ('Jawor', 'Jawor'), ('Jeziorany', 'Jeziorany'), ('Janów Lubelski', 'Janów Lubelski'), ('Jaworzno', 'Jaworzno'), ('Jędrzejów', 'Jędrzejów'), ('Jaraczewo', 'Jaraczewo'), ('Jaworzyna Śląska', 'Jaworzyna Śląska'), ('Jordanów', 'Jordanów'), ('Jarocin', 'Jarocin'), ('Jedlicze', 'Jedlicze'), ('Józefów', 'Józefów'), ('Jarosław', 'Jarosław'), ('Jedlina Zdrój', 'Jedlina Zdrój'), ('Józefów (Biłgoraj County)', 'Józefów (Biłgoraj County)'), ('Jasień', 'Jasień'), ('Jedwabne', 'Jedwabne'), ('Józefów nad Wisłą', 'Józefów nad Wisłą'), ('Jasło', 'Jasło'), ('Jutrosin', 'Jutrosin'), ('Jastarnia', 'Jastarnia'), ('Kalety', 'Kalety'), ('Kamień Pomorski', 'Kamień Pomorski'), ('Kartuzy', 'Kartuzy'), ('Kalisz', 'Kalisz'), ('Kamieńsk', 'Kamieńsk'), ('Katowice', 'Katowice'), ('Kalisz Pomorski', 'Kalisz Pomorski'), ('Kańczuga', 'Kańczuga'), ('Kazimierz Dolny', 'Kazimierz Dolny'), ('Kalwaria Zebrzydowska', 'Kalwaria Zebrzydowska'), ('Karczew', 'Karczew'), ('Kazimierza Wielka', 'Kazimierza Wielka'), ('Kałuszyn', 'Kałuszyn'), ('Kargowa', 'Kargowa'), ('Kąty Wrocławskie', 'Kąty Wrocławskie'), ('Kamienna Góra', 'Kamienna Góra'), ('Karlino', 'Karlino'), ('Kcynia', 'Kcynia'), ('Kamień Krajeński', 'Kamień Krajeński'), ('Karpacz', 'Karpacz'), ('Kędzierzyn-Koźle', 'Kędzierzyn-Koźle'), ('Kietrz', 'Kietrz'), ('Kłobuck', 'Kłobuck'), ('Kępice', 'Kępice'), ('Kisielice', 'Kisielice'), ('Kłodawa', 'Kłodawa'), ('Kępno', 'Kępno'), ('Kleczew', 'Kleczew'), ('Kłodzko', 'Kłodzko'), ('Kętrzyn', 'Kętrzyn'), ('Kleszczele', 'Kleszczele'), ('Knurów', 'Knurów'), ('Kęty', 'Kęty'), ('Kluczbork', 'Kluczbork'), ('Knyszyn', 'Knyszyn'), ('Kielce', 'Kielce'), ('Kłecko', 'Kłecko'), ('Kobylin', 'Kobylin'), ('Konin', 'Konin'), ('Koszalin', 'Koszalin'), ('Kobyłka', 'Kobyłka'), ('Konstancin-Jeziorna', 'Konstancin-Jeziorna'), ('Kościan', 'Kościan'), ('Kock', 'Kock'), ('Konstantynów Łódzki', 'Konstantynów Łódzki'), ('Kościerzyna', 'Kościerzyna'), ('Kolbuszowa', 'Kolbuszowa'), ('Końskie', 'Końskie'), ('Kowal', 'Kowal'), ('Kolno', 'Kolno'), ('Koprzywnica', 'Koprzywnica'), ('Kowalewo Pomorskie', 'Kowalewo Pomorskie'), ('Kolonowskie', 'Kolonowskie'), ('Korfantów', 'Korfantów'), ('Kowary', 'Kowary'), ('Koło', 'Koło'), ('Koziegłowy', 'Koziegłowy'), ('Kraśnik', 'Kraśnik'), ('Krasnystaw', 'Krasnystaw'), ('Krosno', 'Krosno'), ('Krasnobród', 'Krasnobród'), ('Krosno Odrzańskie', 'Krosno Odrzańskie'), ('Krupe', 'Krupe'), ('Krotoszyn', 'Krotoszyn'), ('Krzemienica', 'Krzemienica'), ('Kruszwica', 'Kruszwica'), ('Kruszyn', 'Kruszyn'), ('Krynki', 'Krynki'), ('Krzemionki', 'Krzemionki'), ('Kruszyna', 'Kruszyna'), ('Krynice', 'Krynice'), ('Krzyż Wielkopolski', 'Krzyż Wielkopolski'), ('Kwidzyn', 'Kwidzyn'), ('Lądek-Zdrój', 'Lądek-Zdrój'), ('Laskowa', 'Laskowa'), ('Leba', 'Leba'), ('Lębork', 'Lębork'), ('Lublin', 'Lublin'), ('Lubartów', 'Lubartów'), ('Lubań', 'Lubań'), ('Lubin', 'Lubin'), ('Lubiniec', 'Lubiniec'), ('Lutowiska', 'Lutowiska'), ('Lwówek Śląski', 'Lwówek Śląski'), ('Łapy', 'Łapy'), ('Łask', 'Łask'), ('Łęczna', 'Łęczna'), ('Łomża', 'Łomża'), ('Łowicz', 'Łowicz'), ('Łódź', 'Łódź'), ('Łuków', 'Łuków'), ('Łuków (Rawski County)', 'Łuków (Rawski County)'), ('Miejska Górka', 'Miejska Górka'), ('Mielec', 'Mielec'), ('Mikołów', 'Mikołów'), ('Miejsce Piastowe', 'Miejsce Piastowe'), ('Międzyrzec Podlaski', 'Międzyrzec Podlaski'), ('Mogilno', 'Mogilno'), ('Miechów', 'Miechów'), ('Międzychód', 'Międzychód'), ('Mońki', 'Mońki'), ('Milanówek', 'Milanówek'), ('Mława', 'Mława'), ('Morąg', 'Morąg'), ('Milicz', 'Milicz'), ('Młynary', 'Młynary'), ('Mrągowo', 'Mrągowo'), ('Miłakowo', 'Miłakowo'), ('Mściwojów', 'Mściwojów'), ('Miłomłyn', 'Miłomłyn'), ('Mińsk Mazowiecki', 'Mińsk Mazowiecki'), ('Mysłowice', 'Mysłowice'), ('Nadziejewo', 'Nadziejewo'), ('Nowe Miasteczko', 'Nowe Miasteczko'), ('Nowa Ruda', 'Nowa Ruda'), ('Nidzica', 'Nidzica'), ('Nowe Miasto Lubawskie', 'Nowe Miasto Lubawskie'), ('Nowa Sól', 'Nowa Sól'), ('Niegowa', 'Niegowa'), ('Nowe Skalmierzyce', 'Nowe Skalmierzyce'), ('Nowogard', 'Nowogard'), ('Niemodlin', 'Niemodlin'), ('Nowy Dwór Mazowiecki', 'Nowy Dwór Mazowiecki'), ('Nowy Targ', 'Nowy Targ'), ('Nisko', 'Nisko'), ('Nowy Dwór Gdański', 'Nowy Dwór Gdański'), ('Nowy Wiśnicz', 'Nowy Wiśnicz'), ('Niwki', 'Niwki'), ('Nysa', 'Nysa'), ('Nowa Dęba', 'Nowa Dęba'), ('Oborniki', 'Oborniki'), ('Olsztyn', 'Olsztyn'), ('Oleśnica', 'Oleśnica'), ('Oborniki Śląskie', 'Oborniki Śląskie'), ('Olechów', 'Olechów'), ('Oławka', 'Oławka'), ('Ostróda', 'Ostróda'), ('Ostrów Mazowiecka', 'Ostrów Mazowiecka'), ('Ostrowiec Świętokrzyski', 'Ostrowiec Świętokrzyski'), ('Ostrów Wielkopolski', 'Ostrów Wielkopolski'), ('Ostrzeszów', 'Ostrzeszów'), ('Ostrołęka', 'Ostrołęka'), ('Pabianice', 'Pabianice'), ('Płock', 'Płock'), ('Polanica-Zdrój', 'Polanica-Zdrój'), ('Poznań', 'Poznań'), ('Pakość', 'Pakość'), ('Pruszcz Gdański', 'Pruszcz Gdański'), ('Pruszków', 'Pruszków'), ('Paniec', 'Paniec'), ('Przemyśl', 'Przemyśl'), ('Przygodzice', 'Przygodzice'), ('Puławy', 'Puławy'), ('Puszczykowo', 'Puszczykowo'), ('Piaseczno', 'Piaseczno'), ('Pyrzyce', 'Pyrzyce'), ('Radom', 'Radom'), ('Racibórz', 'Racibórz'), ('Rawa Mazowiecka', 'Rawa Mazowiecka'), ('Radomsko', 'Radomsko'), ('Radzionków', 'Radzionków'), ('Rybnik', 'Rybnik'), ('Rymanów', 'Rymanów'), ('Rzepin', 'Rzepin'), ('Ryki', 'Ryki'), ('Rzeszów', 'Rzeszów'), ('Sanok', 'Sanok'), ('Sandomierz', 'Sandomierz'), ('Sieradz', 'Sieradz'), ('Sierpc', 'Sierpc'), ('Siedlce', 'Siedlce'), ('Słupca', 'Słupca'), ('Słupsk', 'Słupsk'), ('Tarnobrzeg', 'Tarnobrzeg'), ('Tarnów', 'Tarnów'), ('Tuchola', 'Tuchola'), ('Tarnowskie Góry', 'Tarnowskie Góry'), ('Tuchów', 'Tuchów'), ('Turawa', 'Turawa'), ('Tomaszów Lubelski', 'Tomaszów Lubelski'), ('Turek', 'Turek'), ('Tłuszcz', 'Tłuszcz'), ('Tuczyn', 'Tuczyn'), ('Tychy', 'Tychy'), ('Ustroń', 'Ustroń'), ('Ustrzyki Dolne', 'Ustrzyki Dolne'), ('Ustronie Morskie', 'Ustronie Morskie'), ('Wadowice', 'Wadowice'), ('Wałbrzych', 'Wałbrzych'), ('Wałcz', 'Wałcz'), ('Warka', 'Warka'), ('Włocławek', 'Włocławek'), ('Włoszczowa', 'Włoszczowa'), ('Warszawa', 'Warszawa'), ('Włodawa', 'Włodawa'), ('Wieliczka', 'Wieliczka'), ('Wysokie Mazowieckie', 'Wysokie Mazowieckie'), ('Wyszków', 'Wyszków'), ('Wojnicz', 'Wojnicz'), ('Wronki', 'Wronki'), ('Wrocław', 'Wrocław'), ('Września', 'Września'), ('Zabrze', 'Zabrze'), ('Zamość', 'Zamość'), ('Zakopane', 'Zakopane'), ('Zarzecze', 'Zarzecze'), ('Złocieniec', 'Złocieniec'), ('Złotów', 'Złotów'), ('Zielona Góra', 'Zielona Góra'), ('Żary', 'Żary'), ('Żelechów', 'Żelechów'), ('Żagań', 'Żagań'), ('Żary', 'Żary')])),
                ('postal_code', models.CharField(blank=True, max_length=7, null=True, validators=[django.core.validators.RegexValidator(regex='^[0-9]{2}-[0-9]{3}$')])),
                ('street', models.CharField(blank=True, max_length=30, null=True)),
                ('street_number', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]