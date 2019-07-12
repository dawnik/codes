
dlugosc_slowa = int(input("Podaj długość słowa"))
slowo = input("Podaj słowo")

srodek_slowa = int(dlugosc_slowa/2 + 0.5)
slowo_l = srodek_slowa - 1
slowo_p = srodek_slowa
kropki = int(srodek_slowa - 1)
lop = slowo_p

while lop <= dlugosc_slowa:
    print((kropki*chr(46))+ slowo[slowo_l: slowo_p]+ (kropki*chr(46)))
    kropki -= 1
    slowo_l -= 1
    slowo_p += 1
    lop += 1
