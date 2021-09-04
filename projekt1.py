uzivatelia = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

uzivatel = input("vloz meno: ")
heslo = input("vloz heslo: ")

if (uzivatel, heslo) in uzivatelia.items():
    print('Ahoj', uzivatel, "mame na vyber tri texty")
    vyber = input("Zvoleny text: ")
else:
    print("Bohužiaľ nie si registrovaný")
    exit()==quit()

if vyber != "1" and vyber != "2" and vyber != "3":
    print("Bohužiaľ si zadal zlý vstup.")
    exit() == quit()
else:
    vyber_text = TEXTS[int(vyber) - 1]

vycistene_slova = []
velke_slova = []
cele_velke_slovo = []
cele_male_slovo = []
cisla = []

najdlhsie_slovo = 0

for vycistene_slovo in vyber_text.split():
    ciste_slovo = vycistene_slovo.strip(".,:;")
    vycistene_slova.append(ciste_slovo)
    if vycistene_slovo[0].isupper() == True:
        velke_slova.append(ciste_slovo)
    if vycistene_slovo.isupper() == True and vycistene_slovo.isalpha() == True:
        cele_velke_slovo.append(ciste_slovo)
    if vycistene_slovo.islower() == True:
        cele_male_slovo.append(ciste_slovo)
    if vycistene_slovo.isdigit() == True:
        cisla.append(int(ciste_slovo))
    if len(vycistene_slovo) > najdlhsie_slovo:
        najdlhsie_slovo = len(vycistene_slovo)

suma = 0
for hodnota_cisla in cisla:
    suma += hodnota_cisla

print("Text má", len(vycistene_slova), "slov.\n")

if len(velke_slova) > 4:
    print("Text má", len(velke_slova), "slov začínajúcich veľkým písmenom.\n")
elif len(velke_slova) < 5 and len(velke_slova) > 1:
    print("Text má", len(velke_slova), "slová začínajúce veľkým písmenom.\n")
elif len(velke_slova) == 1 :
    print("Text má", len(velke_slova), "slovo začínajúce veľkým písmenom.\n")
else:
    print("Text nemá slovo začínajúce veľkým písmenom.\n")

if len(cele_velke_slovo) > 4:
    print("Text má", len(cele_velke_slovo), "slov napísaných veľkými písmenami.\n")
elif len(cele_velke_slovo) < 5 and len(cele_velke_slovo) > 1:
    print("Text má", len(cele_velke_slovo), "slová napísané veľkými písmenami.\n")
elif len(cele_velke_slovo) == 1 :
    print("Text má", len(cele_velke_slovo), "slovo napísané veľkými písmenami.\n")
else:
    print("Text nemá slovo napísané veľkými písmenami.\n")

print("Text má", len(cele_male_slovo), "slov napísaných malými písmenami.\n")

if len(cisla) > 4:
    print("Text má", len(cisla), "čísel.\n")
elif len(cisla) < 5 and len(cisla) > 1:
    print("Text má", len(cisla), "čísla.\n")
elif len(cisla) == 1 :
    print("Text má", len(cisla), "číslo.\n")
else:
    print("Text nemá číslo.\n")

print("Suma čísel v texte je", suma, "\n")

podtrznik = "-"
print(podtrznik * 36)
print("Dĺžka |       Výskyt         | Počet")
print(podtrznik * 36)

for x in range(1,najdlhsie_slovo + 1):
    dlzka = ""
    for y in vyber_text.split():
        konecne_slovo = y.strip(".,:;")
        if x == len(konecne_slovo):
            dlzka += "*"
    x_str = str(x)
    print(x_str.rjust(5), "|", dlzka.ljust(20), "|", len(dlzka))