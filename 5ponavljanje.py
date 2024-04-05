#Zadana je lista brojeva
#Lista = [1, 2, 4, 5, 6, 7, 10, 11, 12, 13, 15, 18, 19, 20]
#Lista je nepotpuna, nedostaju joj neki brojevi kako bi tvorila listu brojeva od 1 do 2
#Ispišite koji brojevi nedostaju
#Ispišite novu listu koja je nastala spajanjem zadane liste i liste s 
#rezultatima. Neka lista bude sortirana silazno

#primjer
""" 
lista = [3,1,2]
sortirana = sorted(lista)
silazno = sorted(lista, reverse=True)
print(sortirana)
print(silazno)
"""
# primjer koji sam sam uradio nije bas dobar jer nisam napravio da program sam nađe brojeve koji fale
"""
lista = [1, 2, 4, 5, 6, 7, 10, 11, 12, 13, 15, 18, 19, 20]
nedostajuci = [3,8,9,14,16,17]
skupna = lista + nedostajuci
print(skupna)
sortirana = sorted(skupna)
print(sortirana)
silazna = sorted(skupna, reverse=True)
print(silazna)
"""
"""# ja uradio doma, kao odradi što je ali nije baš dobar način
lista = [1,2,4,5,6,7,10,11,12,13,15,18,19,20]
for i in range(6):
    lista.append(int(input("Unesi element: ")))
    sortirana = sorted(lista)
silazno = sorted(lista, reverse=True)
print(silazno)
"""
# ja uradio doma ali sam prepisao glavni dio koda
"""
lista = [1, 2, 4, 5, 6, 7, 10, 11, 12, 13, 15, 18, 19, 20]
listaprvi = lista[0]
listazadnji = lista[-1]
nedostajuci = []
for i in range(listaprvi,listazadnji):
    if i in lista:
        continue
    nedostajuci.append(i)
print(nedostajuci)
skupni = lista + nedostajuci
uzlazno = sorted(skupni)
print(uzlazno)
silazno = sorted(skupni, reverse=True)
print(silazno)
"""
# na satu radili
"""
lista = [1, 2, 4, 5, 6, 7, 10, 11, 12, 13, 15, 18, 19, 20]
prvi = lista[0]
zadnji = lista[-1]#20
nedostajuci = []
for i in range(prvi, zadnji):# bitna su samo prvi i zadnji 
    if i in lista:# a može i not
        continue
    nedostajuci.append(i)
print(nedostajuci)
#ispiši sve sortirano silazno
rez = lista + nedostajuci#nadodaje jednu listu na drugu, i ne raspoređiva brojeve koji fale
print(rez)
#ovaj dio koda sa sorted sam ja napravio
sortirana = sorted(rez)#sorted napravi od najmanjeg prema najvecem
print(sortirana)
#
silaznoRez = sorted(rez, reverse=True)#rez ako ocemo onda sve, profa je samo lista, ne znam zašto
print(silaznoRez)
"""
#Potrebno je napraviti program koji računa indeks tjelesne mase
#Indeks tjelesne mase
#okvirna mjera za procjenu stanja uhranjenosti
#Formula: BMI = težina / (visina/100)2
#težina – kg; visina – cm
"""
visina = float(input("Unesi visinu: "))
tezina = float(input("Unesi tezinu: "))
spol = input("Unesi m za muškarce a za žene z: ")
BMI = tezina/(visina/100)**2
if spol=="m":
    if BMI<20:
        print(f"U pitanju je muškarac a BMI mu je {BMI} a to je pothranjenost")
    elif 20<=BMI<=25:
        print(f"U pitanju je muškarac a BMI mu je {BMI} a to je idealno")
    else:
        print(f"U pitanju je muškarac a BMI mu je {BMI} a to je pretilost")
elif spol=="z":
    if BMI<19:
        print(f"U pitanju je žena a BMI joj je {BMI} a to je pothranjenost")
    elif 19<=BMI<=24:
        print(f"U pitanju je žena a BMI joj je {BMI} a to je idealno")
    else:
        print(f"U pitanju je žena a BMI joj je {BMI} a to je pretilost")
else:
    print("Pogrešan unos")
"""
#Papir, škare, kamen
#Računalo generira slučajan odabir, a korisnik igra protiv računala
#Ispisuje se tko je pobjednik ili da se radi o izjednačenom rezultatu
#Ako korisnik unese „kraj” igra se završava i ispisuje se broj pobjeda 
#korisnika i računala te konačni pobjednik
#Random – generiranje pseudoslučajnih brojeva
"""# ja radio 1.4.
import random
izbor = ["papir", "skare", "kamen"]
ja = 0
racunalo = 0
izjednaceno = 0
odg = "kraj"
while odg != True:
    korisnik = input("Unesi: ")
    komp = random.choice(izbor)#bira slučajni element list
    print("Racunalo: ", komp)
    if korisnik == "kamen" and komp == "skare":
        ja += 1
        print("Pobjedio si!")
    elif  korisnik == "kamen" and komp == "papir":
        racunalo += 1 
        print("Računalo je pobjedilo!")  
    elif korisnik == "kamen" and komp == "kamen":
        izjednaceno += 1
        print("Izjednačeno")
    elif  korisnik == "skare" and komp == "papir":
        ja += 1
        print("Pobjedio si!")  
    elif  korisnik == "skare" and komp == "kamen":
        racunalo += 1 
        print("Računalo je pobjedilo!") 
    elif korisnik == "skare" and komp == "skare":
        izjednaceno += 1
        print("Izjednačeno")
    elif  korisnik == "papir" and komp == "kamen":
        ja += 1   
        print("Pobjedio si!")
    elif korisnik == "papir" and komp == "papir":
        izjednaceno += 1
        print("Izjednačeno")
    elif  korisnik == "papir" and komp == "skare":
        racunalo += 1 
        print("Računalo je pobjedilo!") 
    odg = input("Da li želite nastaviti igru? ")
    if odg == "kraj":
        break
print("Korisnik: ",ja)
print("Racunalo: ", racunalo)
print("Izjednaceno: ", izjednaceno)
if ja > racunalo:
    print("Čestitam! Pobjedio si")
elif ja < racunalo:
    print("Nažalost si izgubio")
elif ja == racunalo:
    print("Izjednačeno")
"""
#papir škare kamen ja radio 25.2. zabroavio stavit izjednačeno ako brojac
"""
import random
izbor = ["papir","skare","kamen"]
odg = "da"
#unos = input("Unesi: ")
rac = 0
ja = 0
while odg == "da":
    unos = input("Unesi: ")
    komp = random.choice(izbor)
    print(komp)
    if unos == "skare" and komp == "papir":
        ja += 1
    elif unos == "papir" and komp == "kamen":
        ja += 1
    elif unos == "kamen" and komp == "skare":
        ja += 1
    elif unos == "skare" and komp == "kamen":
        rac += 1
    elif unos == "papir" and komp == "skare":
        rac += 1
    elif unos == "kamen" and komp == "papir":
        rac += 1
    odg = input("Da li želite nastaviti igrati, da/ne: ")
print("Igrac: ", ja, "pobjeda")
print("Računalo: ", rac, "pobjada")
if ja > rac:
    print("Pobjedili ste")
elif ja==rac:
    print("Izjednačeno")
else:
    print("Izgubili ste")
"""
# na satu sa profom radili
"""
import random
izbor = ["papir", "skare", "kamen"]
odg = "da"
pobjede = 0
porazi  = 0
izjednaceno = 0
while odg == "da":
    komp = random.choice(izbor)
    ja = (input("Unesi: "))
    print(komp)
    if ja == 'papir':
        if komp == "kamen":
            print("Ja sam pobjednik")
            pobjede += 1
        elif komp == "skare":
            print("Računalo je pobjednik")
            porazi += 1
        else:
            print("Izjednačeno")
            izjednaceno += 1
    if ja == 'kamen':
        if komp == 'skare':
            print("Ja sam pobjednik")
            pobjede += 1
        elif komp == "papir":
            print("Računalo je pobjednik")
            porazi += 1
        else:
            print("Izjednačeno")
            izjednaceno += 1

    if ja == 'skare':
        if komp == "papir":
            print("Ja sam pobjednik")
            pobjede += 1
        elif komp == "kamen":
            print("Računalo je pobjednik")
            porazi += 1
        else:
            print("Izjednačeno")
            izjednaceno += 1
    odg = input ("Nastavak? da /ne: ")

print(f"Broj pobjeda: {pobjede}")
print(f"Broj poraza: {porazi}")
print(f"Izjednačeno: {izjednaceno}")
if pobjede > porazi:
    print("ČESTITAM! Pobjedili ste!")
elif pobjede < porazi:
    print("Nažalost izgubili ste!")
else:
    print("Ostali ste izjednačeni!")  
"""