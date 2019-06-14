print("Program liczy średną predkosć pociągu z punktu A do punktu B, na wejściu pobiera liczbę testów, "
      "następnie pobiera dwie wartosći ")
print("Podaj liczbę testów: ")
i = int(input())

while i >= 1:
    print("Test nr: "+ str(i))

    print("Średnia predkosć pociągu do miejscowośći A: ")
    x = int(input())
    print("Średnia predkosć pociągu do miejscowośći B: ")
    y = int(input())

    a = int(2*x*y/(x+y))
    i -= 1

    print("Średnia prędkosć pociągu na trasie między miejscowościamy A i B wyniosłą: "+ str(a))

