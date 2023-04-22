from datetime import datetime
from re import A

teraz = (datetime.now())
obecny_rok = teraz.year
# Zapytaj o imie
imie = input("Podaj imie: ")
# Zapytaj o rok urodzenia
urodzony = input("podaj rok urodzenia: ") 
# konwersja zmiennych
# int("32")
# Wyświetlenie informacji
# - Cześć imie
print("Cześć  " + imie) 
# - Masz obecnie {wiek} lat
wiek = obecny_rok - int(urodzony)

print("Masz obecnie "+ str(wiek) + " lat")

if (wiek >18):
    print("Możesz kupić piwo w PL")

print("To się wydrujuje następne")
# - 100 lat skończysz w {rok osiągnięcia 100 lat} roku

# - Sprawdzanie Czy liczba jest parzysta. + weryfikacja 0
liczba = int(input("Podaj liczbę: "))
if (liczba ==0):
    print("To jest 0")
elif (liczba % 2) == 0:
    print("jest parzysta")
else:
    print("jest nieparzysta")

#Wartosć bezwsględna

liczba = int(input("Podaj liczbę: "))
if (liczba ==0):
    print("To jest 0")
elif (liczba <0):
    print("wartość bezwzględna to " + str(-liczba))
else:
    print("wartość bezwzględna to " + str(liczba))

# Użycie funkcji

def wartosc_bezwzgledna(liczba):
    if (liczba ==0):
        print("To jest 0")
    elif (liczba <0):
        print("wartość bezwzględna to " + str(-liczba))
    else:
        print("wartość bezwzględna to " + str(liczba))

nowa_liczba = int (input("podaj liczbe: "))
wartosc_bezwzgledna(nowa_liczba)


## Napisz program który 
# 1. Pobiera od użytkownika 2 liczby
# 2. Da możliwośc wyboru i po naciśnięciu:
# - 1 - zwróci większą liczbę ( porównanie) 
# - 2 - zwrócenie wartości bezwzględnej (wartość bezwzględna)
# - 3 - Pomnoży liczby (mnożenie)


##Pobiera liczby
liczba1 = input("Podaj liczbę: ")
liczba2 = input("Podaj drugą liczbę: ")

input(1)
def porownanie()
if (liczba1 > liczba2):
    print(liczba1)
else:
    print(liczba2) 

input(2)
def wartosc_bezwzgledna(liczba1, liczba2):
    if (liczba1, liczba2 <0):
        print("wartość bezwzględna to " + str(liczba1, liczba2))
    else:
        print("wartość bezwzględna to " + str(liczba1, liczba2))
input(3)
def mnozenie()
print(liczba1*liczba2)


