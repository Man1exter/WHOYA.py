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

    if onano == False:
        print("Jestes kobieta")
    else:
        print("Jestes mezczyzna")

elif wybor == 2:
    print("ok")