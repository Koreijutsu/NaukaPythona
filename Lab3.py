## Policz sumę cyfr     """ZROBIONE"""



# liczba = input("Podaj liczbę: ")  ## Podaję liczbę
# suma = 0                          ## suma na starcie musi wynosić 0
# for cyfra in liczba:              ## Pętla przechodzi przez kolejne cyfry
#     suma += int(cyfra)            ## Konwersja na inta  
# print("Suma cyfr to:", suma)      ## Wyświetlenie wyniku  


## Wypisz n kolejnych potęg  """ZROBIONE"""

# Liczba = int(input("Podaj liczbę n: "))  ## Podaję liczbę
# potega = 1                               ## Ustawiamy potęgę na 1 
# for i in range(Liczba):                  ## pętla która powtarza liczbę n razy 
#     potega *= 2                          ## Potęga jest mnożona przez 2
#     print(potega)                        ## Wyświetla wynik 
    


# ## Oblicz pierwiastek       """ZROBIONE"""


# NaszaLiczba = int(input("Podaj liczbę całkowitą: "))    ## Podaję liczbę

# if NaszaLiczba < 0:                                     ## Musi być większa od 0
#     print("NaszaLiczba musi być liczbą dodatnią.")
# else:
#     Szukana = 0                                         ## Ustawienie na 0
#     while Szukana * Szukana <= NaszaLiczba:             ## Sprawdzenie czy liczba spełnia odpowiednie warunki
#         Szukana += 1
#     Szukana -= 1
#     if Szukana * Szukana == NaszaLiczba:                ## Sprawdzenie czy liczby są równe
#         print(f"Pierwiastek kwadratowy z {NaszaLiczba} to {Szukana}")
#     else:
#         print(f"{NaszaLiczba} nie ma pierwiastka kwadratowego w zbiorze liczb całkowitych.")

    

 ## PIERWSZA GRA ##        """ZROBIONE"""


import random

ImieGracza = input("Podaj swoje imię: ")    ## Prosi o podanie imienia
print("Cześć " + ImieGracza)    ##Wyświetla imie
PrzedzialLiczbMin = int(input("Podaj minimalny zakres Liczby: "))   ## Pobiera min liczbę
PrzedzialLiczbMax = int(input("Podaj maxymalny zakres Liczby: "))   ## Pobiera max liczbę
NaszaLiczba = random.randint(PrzedzialLiczbMin, PrzedzialLiczbMax)
print("Podany zakres to od", PrzedzialLiczbMin, "do", PrzedzialLiczbMax)

# print(NaszaLiczba)    ##sprawdza czy generowanie działa

LiczbaPodejsc = 0
while True:
    SzukanaLiczba = input("Podaj wybraną przez siebię liczbę z podanego wcześniej zakresu ")
    if SzukanaLiczba == "X":
        print("Koniec Gry")
        break
    try:                                                ## Obsługa błędu 
        SzukanaLiczba = int(SzukanaLiczba)
    except:
        print("To nie jest liczba! Spróbuj ponownie.")
        continue
    if SzukanaLiczba < PrzedzialLiczbMin or SzukanaLiczba > PrzedzialLiczbMax:
        print("Liczba musi być z zakresu od", PrzedzialLiczbMin, "do", PrzedzialLiczbMax)
        continue

    LiczbaPodejsc += 1
    if SzukanaLiczba == NaszaLiczba:                    ## Program porównuje i wyświetla informacje
        print("Gratulacje", ImieGracza + "!", "Udało Ci się odgadnąć liczbę za", LiczbaPodejsc, "podejściem.")
        break
    elif SzukanaLiczba < NaszaLiczba:
        print("Podana liczba jest zbyt mała!")
    else:
        print("Podana liczba jest zbyt duża!")





