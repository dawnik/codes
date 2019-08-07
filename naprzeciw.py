# Wejście
# W pierwszym wierszu wejścia znajduje się liczba zapytań q (q ≤ 105). Każde zapytanie opisane jest w osobnym wierszu, gdzie podane są dwie liczby całkowite n, k (1 ≤ n ≤ 106, 1 ≤ k ≤ n) oznaczające kolejno liczbę osób biorących udział w posiedzeniu oraz przypisany numer porządkowy pytającego.
#
# Wyjście
# Dla każdego zapytania program powinien wypisać numer porządkowy osoby siedzącej dokładnie naprzeciw osoby (k) zadającej pytanie, albo napis BRAK, gdy dokładnie naprzeciw nikt nie zasiada.
#
# Przykład
#
# Wejście
# 4
# 2 1
# 3 2
# 4 2
# 4 3
#
# Wyjście
# 2
# BRAK
# 4
# 1

how_many_tests = int(input("How many tests: "))

licznik = 0
while how_many_tests >= licznik:
    licznik += 1
    number_people_attending_metting = int(input("Number of pepole attending the metting: "))
    number_sitting = int(input("Sitting number: "))
    var = 0
    if number_people_attending_metting % 2 == 0:
        var = number_people_attending_metting / 2
        var_sitting = int(var + number_sitting)
        if var_sitting > number_people_attending_metting:
            var_sitting = (number_sitting * 2) - var_sitting
        print(var_sitting)
    else:
        print("BRAK")
