"""
Wypisz wszystkie liczby ai podzielne przez x i niepodzielne przez y, gdzie 1 < ai < n < 100000.
Wejście
Najpierw w oddzielnej linii t liczba przypadków testowych następnie w kolejnych t liniach liczby n x y.
Wyjście
W kolejnych t liniach oddzielone pojedynczym odstępem liczby spełniające warunki zadania wypisane od najmniejszej do największej.

Przykład

Wejście:
2
7 2 4
n x y
35 5 12
Wyjście:
2 6
5 10 15 20 25 30
"""
i = int(input("Liczba testów: "))
ii = 1
while ii <= i:

    slownik = []
    nn = 1
    n = int(input("Liczba n: "))
    x = int(input("Liczby podzielne przez x: "))
    y = int(input("Liczba nie podzielne przez y: "))
    while nn <= n:
        if nn % x == 0:
            slownik.append(nn)
            if nn % y == 0:
                a = nn % y
                slownik.remove(nn)
        nn +=1


    print(slownik)
    ii += 1

