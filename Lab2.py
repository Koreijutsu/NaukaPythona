from ast import While


liczby_pierwsze = [2,3,5,7,11]

for pierwsza in liczby_pierwsze:
    print(pierwsza)

liczby = [1,2,3,4,5,6,7,8,9,10,11]

for liczba in liczby:
    if liczba%2 == 0:
        print (str(liczba) + " jest liczbą parzystą")
        else:
            continue  


i = 1
while i<10:
    print(i)
    i += 1

while True:
    print(i)
    i += 1
    if i>19:
        break


