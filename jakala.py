# Wejście
    # W pierwszym wierszu jedna liczba naturalna k ∈ [1, 26] określająca liczbę liter.
    # W drugim wierszu k małych liter alfabetu angielskiego, które Jaś wymawia podwójnie.
    # W trzecim wierszu jeden wyraz złożony wyłącznie z małych liter języka angielskiego.
    # Liczba znaków mieści się w przedziale [1, 1000].
# Wyjście
    # Na wyjściu należy wypisać jak będzie słyszany wyraz wypowiedziany przez jąkającego się Jasia.

ilosc_liter = int(input("Ilość liter: "))
litery = str(input("Jakie litery: "))
wyraz = str(input("Jaki wyraz: "))


i = 0
finish_wyraz = ''

for n_wyraz in wyraz:
    finish_wyraz += n_wyraz

    for n_litery in litery:
        if n_litery == n_wyraz:
            finish_wyraz += n_litery

print(finish_wyraz)

