from random import randint

print(" Witam jestem BOT MAN1EXTER " + "\U0001f600")
print("Mam kilka zadań a oto kilka z nich:")
print("[1] ZGADNE KIM JESTES")
print("[2] POWIEM CI KTORA LICZBA JEST PARZYSTA, A KTORA NIE")
print("[3] UTWORZE CI LOSOWY KLUCZ")
print("[4] ANALIZA TEKSTU")

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

    print(" ")

elif wybor == 3:

    print(" ")
    print(" ")

    ilosc = int(input("Ile liczb ma miec twoj kod przedzial kodu to (0 - 10)? "))
    x = 0

    while x < ilosc:
     print(int(randint(0,10)))
     x += 1
		
elif wybor == 4:

    print(" ")
    print(" ")
    print("Z pliku TEXTOWEGO wczytywany jest text")
    print("możesz go zmienić ja policze swoje procenty")
    print(" ")

    plik = open("import.txt","r")
    txt = plik.read()
    plik.close()

    def policzalne(text,znaki):

        liczenie = 0
        for ele in text:
           if ele == znaki:
               liczenie += 1
        return liczenie
        
    print("znaki (a) w calym teksie ===> ",policzalne(txt,"a"))

    for elementor in "abcdefghijklmnouprstuwyz":

        ileJest = policzalne(txt.lower(), elementor)
        procentowo = 100 * ileJest / len(txt)

        print("{0} - {1} - {2}%".format(elementor.upper(), ileJest ,procentowo)) # całe %
        print("{0} - {1} - {2}%".format(elementor.upper(), ileJest ,round(procentowo,2))) # 2 miejsca po przecinku