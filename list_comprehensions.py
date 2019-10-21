numbers =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_list = []
for n in numbers:
    my_list.append(n)
print(my_list)

my_list_comprehensions = [n for n in numbers]
print(my_list_comprehensions)

my_list_square_comprehensions = [n*n for n in numbers]
print(my_list_square_comprehensions)


my_list_if_n_even = []
for n in numbers:
    if n%2 == 0:
        my_list_if_n_even.append(n)
print(my_list_if_n_even)

my_list_if_n_even_comprehensions = [n for n in numbers if n%2 == 0]
print(my_list_if_n_even_comprehensions)


my_list_pair = []
for letter in 'abcs':
    for n in range(4):
        my_list_pair.append((letter, n))
print(my_list_pair)

my_list_pair_comprehensions = [(let, numbers) for let in 'abcd' for numbers in range(4)]
print(my_list_pair_comprehensions)


other_numbers = [1, 1, 2, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 8, 9, 9]
my_set = set()
for n in other_numbers:
    my_set.add(n)
print(my_set)

my_set_comprehensions = {n for n in other_numbers}
print(my_set_comprehensions)