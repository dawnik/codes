ilosc_testow = int(input())
i_t = 1
slownik = []

while i_t <= ilosc_testow:
    rodzaj_grafu = input()
    slownik.append(rodzaj_grafu)
    ile_krawedzi = int(input())
    slownik.append(ile_krawedzi)
    licznik_ile_krawedzi = 1

    if rodzaj_grafu == 'd' or rodzaj_grafu == 'g':
        while licznik_ile_krawedzi <= ile_krawedzi:
            slownik.append(input())
            slownik.append(input())
            licznik_ile_krawedzi += 1
    if rodzaj_grafu == 'gw' or rodzaj_grafu == 'dw':
        while licznik_ile_krawedzi <= ile_krawedzi:
            slownik.append(input())
            slownik.append(input())
            slownik.append(input())
            licznik_ile_krawedzi += 1

    i_t += 1

i_t = 1
while i_t <= ilosc_testow:
    test = slownik[0]
    slownik.pop(0)
    if test == 'g':
        print("graph {")
        ilosc_krawedzi = slownik[0]
        slownik.pop(0)
        licznik_i_k = 1
        while licznik_i_k <= ilosc_krawedzi:
            napis = ''
            a = slownik[0]
            a = str(a)
            slownik.pop(0)
            b = slownik[0]
            b = str(b)
            slownik.pop(0)
            napis += a + ' -- ' + b + ';'
            print(napis,"\t")
            licznik_i_k += 1
        print("}")
    if test == 'd':
        print("digraph {")
        ilosc_krawedzi = slownik[0]
        slownik.pop(0)
        licznik_i_k = 1
        while licznik_i_k <= ilosc_krawedzi:
            napis = ''
            a = slownik[0]
            a = str(a)
            slownik.pop(0)
            b = slownik[0]
            b = str(b)
            slownik.pop(0)
            napis += a + ' -> ' + b + ';'
            print(napis,"\t")
            licznik_i_k += 1
        print("}")
    if test == 'gw':
        print("graph {")
        ilosc_krawedzi = slownik[0]
        slownik.pop(0)
        licznik_i_k = 1
        while licznik_i_k <= ilosc_krawedzi:
            napis = ''
            a = slownik[0]
            a = str(a)
            slownik.pop(0)
            b = slownik[0]
            b = str(b)
            slownik.pop(0)
            c = slownik[0]
            c = str(c)
            slownik.pop(0)
            napis += a + ' -- ' + b + ' [label = ' + c + '];'
            print(napis,"\t")
            licznik_i_k += 1
        print("}")
    if test == 'dw':
        print("digraph {")
        ilosc_krawedzi = slownik[0]
        slownik.pop(0)
        licznik_i_k = 1
        while licznik_i_k <= ilosc_krawedzi:
            napis = ''
            a = slownik[0]
            a = str(a)
            slownik.pop(0)
            b = slownik[0]
            b = str(b)
            slownik.pop(0)
            c = slownik[0]
            c = str(c)
            slownik.pop(0)
            napis += a + ' -> ' + b + ' [label = ' + c + '];'
            print(napis,"\t")
            licznik_i_k += 1
        print("}")
    i_t += 1
