komenda = input("SZYFRUJ / DESZYFRUJ: ")
klucz = list(input("Jaki klucz: "))
tekst = list(input("Tekst do szyfrowania: "))


warunek_len = True
licznik_warunek_len = 0
klucz_przesuniecie = []

while warunek_len:
    for litera in klucz:
        klucz_przesuniecie += litera
        if len(klucz_przesuniecie) >= len(tekst):
            warunek_len = False
            break


slowo = list('')
if komenda == 'SZYFRUJ':
    for iterator_tekst in tekst:
        a = ord(iterator_tekst)
        for iterator_klucz_przesuniecie in klucz_przesuniecie:
            klucz_przesuniecie.pop(0)
            b = a + int(iterator_klucz_przesuniecie)
            while b > 90:
                b -= 26
            c = chr(b)
            slowo += c
            break

if komenda == 'DESZYFRUJ':
    for iterator_tekst in tekst:
        a = ord(iterator_tekst)
        for iterator_klucz_przesuniecie in klucz_przesuniecie:
            klucz_przesuniecie.pop(0)
            b = a - int(iterator_klucz_przesuniecie)
            while b > 90:
                b -= 26
            c = chr(b)
            slowo += c
            break

haslo = ''
for letter in slowo:
    haslo += letter
print(haslo)
