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