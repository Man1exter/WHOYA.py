print(" Witam jestem BOT MAN1EXTER " + "\U0001f600")
print("Mam kilka zadań a oto kilka z nich:")
print("[1] ZGADNE KIM JESTES")
print("[2] POWIEM CI KTORA LICZBA JEST PARZYSTA, A KTORA NIE")
print("[3] UTWORZE CI LOSOWY KLUCZ")

print(" ")
wybor = int(input("Jaka opcja cie interesuje? =======> "))

if wybor == 1:

    imie = input("Jak masz na imie?")
    onano = print(imie.endswith("a"))

    print(" ")
    print("Witaj " + imie)

    if onano == False:
        print("Jestes kobieta")
    else:
        print("Jestes mezczyzna")

elif wybor == 2:

    print(" ")
    print("Pokaze ci parzyste i nieparzyste liczby w podanej liscie")
    print("Bedzie to pokazane na pare sposobow")

    lista = [10,20,30,40,50,60,65,70,75,80,92,100]
    print(lista)

    print("użycie =====> all / any")

    if all([element % 2 == 0 for element in lista]):
        print("Wszystkie parzyste")
    else:
        print("Niektóre są tu nieparzyste")

    if any([el % 2 == 0 for el in lista]):
        print("Chociaż 1 element jest parzysty")
    else:
        print("nie ma takigo")

    print(" ")

    for elem in enumerate(lista):
        print(elem)

elif wybor == 3:

    print("ok")