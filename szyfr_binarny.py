slownik = {
    "00000": 'A',
    "00001": 'B',
    "00010": 'C',
    "00011": 'D',
    "00100": 'E',
    "00101": 'F',
    "00110": 'G',
    "00111": 'H',
    "01000": 'I',
    "01001": 'J',
    "01010": 'K',
    "01011": 'L',
    "01100": 'M',
    "01101": 'N',
    "01110": 'O',
    "01111": 'P',
    "10000": 'Q',
    "10001": 'R',
    "10010": 'S',
    "10011": 'T',
    "10100": 'U',
    "10101": 'V',
    "10110": 'W',
    "10111": 'X',
    "11000": 'Y',
    "11001": 'Z',
}
petli = int(input("Ile testów: "))

warunek = petli
iterator_warunek = 1

while iterator_warunek <= warunek:
    slowo = input("Haslo: ")
    haslo= ''
    word = ''
    licznik = 0
    kolejka = 1

    for litera in slowo:
        haslo += litera
        licznik += 1
        if licznik == 5:
            for haslo in slownik.get(haslo):
                word += haslo
                haslo = ''
                licznik = 0
                kolejka += 1
                break
    iterator_warunek += 1
    print(word)
