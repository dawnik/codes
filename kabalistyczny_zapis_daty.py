"""Istnieje bardzo łatwy sposób zapisu daty, barokowy pomysł nawiązywał do kabały,
w której literom hebrajskim przypisane były liczby. Datę oblicza się sumując wszystkie liczby odpowiadające
kolejnym literom tekstu"""

zrodlo = {'a': 1,
          'b': 2,
          'c': 3,
          'd': 4,
          'e': 5,
          'f': 6,
          'g': 7,
          'h': 8,
          'i': 9,
          'k': 10,
          'l': 20,
          'm': 30,
          'n': 40,
          'o': 50,
          'p': 60,
          'q': 70,
          'r': 80,
          's': 90,
          't': 100,
          'v': 200,
          'x': 300,
          'y': 400,
          'z': 500,
          }

wyraz = input("Podaj słowo ")
x, suma = 0, 0

for letter in wyraz:
    if letter in zrodlo:
        x = zrodlo[letter]
        suma += x
        print("Letter: '", letter,"'")
        print("Suma:   ", suma)
