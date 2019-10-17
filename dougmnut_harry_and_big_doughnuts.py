# Wejście:
# 3
# 5 15 3
# 1 5 4
# 13 25 2
#
# Wyjście:
# yes
# yes
# no

tests = int(input("How many tests: "))

while tests > 0:
    cats = int(input("How many cats: "))
    harry_force = int(input("Harry's force: "))
    weight_doughnut = int(input("How weight one doughnut: "))

    if (cats*weight_doughnut) <= harry_force:
        print("yes")
    else:
        print("no")
    tests -= 1