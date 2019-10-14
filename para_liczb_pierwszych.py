# Wejście:
#
# 3
# 4
# 17
# 5
#
# Wyjście:
#
# TAK 2 2
# NIE
# TAK 2 3

# number_of_data_sets = int(input("How many data sets: "))
# target_data = int(input("Serve number: "))

i = 400
j = 0
zbiur_odrzuconych = ''
zbiur_pierwszych = ''
a = 2
b = 0
c = 1

while a <= i:
    print("a",a)
    zbiur_pierwszych += str(a)
    print("zbiur_pierwszych",zbiur_pierwszych)
    while j < i:
        b    += a
        zbiur_odrzuconych += str(b) + ' '
        j += a
        if j >= i:
            a += c
    print('zbiur_odrzuconych',zbiur_odrzuconych)
    print('a',a)
    print('b',a)
    print('c',a)
    break