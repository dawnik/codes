"""Wejście
Zadaniem jest napisanie programu konwertującego z formatu zapisu grafu na format języka dot,
zrozumiały dla programu graphviz.

W pierwszej linii liczba grafów t  (1 ≤ t ≤ 10). W nastepnej linii rodzaj grafu:

g - graf

d - graf skierowany

gw - graf ważony

dw - graf skierowany ważony

Następnie liczba krawędzi n (1 ≤ n ≤ 20). W kolejnych liniach opisy n krawędzi. Każdy opis to dwa indentyfikatory węzła
początkowego i końcowego dla danej krawędzi. Dla grafów ważonych dodatkowo, jako trzeci parametr, waga krawędzi.
Identyfikator węzła id nie przekracza 5 znaków (litery lub cyfry), a waga mieści się typie int."""

ilosc_testow = int(input("Ile testów: "))
i_t = 1
while i_t <= ilosc_testow:
    jaki_rodzaj_grafu = input("Jaki rodzaj grafu: ")

    if jaki_rodzaj_grafu == 'g' or jaki_rodzaj_grafu == 'd':
        ile_krawedzi = int(input("Ile krawędzi"))
        i = 1
        slownik = []
        while i <= ile_krawedzi:
            slownik.append(input())
            slownik.append(input())
            i += 1

        # 1. Graf skierowany [directed graph]:
        if jaki_rodzaj_grafu == 'd':
            print("digraph {")
            licznik = 1
            while licznik <= ile_krawedzi:
                a = slownik[0]
                slownik.pop(0)
                b = slownik[0]
                slownik.pop(0)
                print(a, "->", b + ";")
                licznik += 1
            print("}")
        # 2. graf nieskierowany [undirected graph]
        if jaki_rodzaj_grafu == 'g':
            licznik = 1
            while licznik <= ile_krawedzi:
                a = slownik[0]
                slownik.pop(0)
                b = slownik[0]
                slownik.pop(0)
                print(a, "--", b + ";")
                licznik += 1

    if jaki_rodzaj_grafu == 'gw' or jaki_rodzaj_grafu == 'dw':
        ile_krawedzi = int(input("Ile krawędzi"))
        i = 1
        slownik = []
        while i <= ile_krawedzi:
            slownik.append(input())
            slownik.append(input())
            slownik.append(input())
            i += 1


        #3. graf nieskierowany ważony  [undirected weighted graph]
        if jaki_rodzaj_grafu == 'gw':
            licznik = 1
            while licznik <= ile_krawedzi:
                a = slownik[0]
                slownik.pop(0)
                b = slownik[0]
                slownik.pop(0)
                c = slownik[0]
                slownik.pop(0)
                print(a, "--", b, "[label = ", c + "]")
                licznik += 1

        #4. graf skierowany ważony [directed weighted graph]
        if jaki_rodzaj_grafu == 'dw':
            licznik = 1
            while licznik <= ile_krawedzi:
                a = slownik[0]
                slownik.pop(0)
                b = slownik[0]
                slownik.pop(0)
                c = slownik[0]
                slownik.pop(0)
                print(a, "->", b, "[label = ", c + "]")
                licznik += 1
    i_t += 1
