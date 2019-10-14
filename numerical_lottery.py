import random

play_game = "yes"
figures_give = []
var_figure_give = ''
lap = 0
figures_draw_by_lot = []

print("Game of chance, give 6 figures from the range 1/50")

while play_game == "yes":
    for a in range(6):
        figures_give.append((input("Give me a number " + str(a+1) + ": ")))
        figures_draw_by_lot.append(random.randint(1, 50))

    figures_score_a_hit = 0
    for b in figures_give:
        for c in figures_draw_by_lot:
            if b == c:
                figures_score_a_hit += 1
    print("Your figure score a hit:", str(figures_score_a_hit))
    figures_give.sort()
    print("Your figures: ", figures_give)
    figures_draw_by_lot.sort()
    print("Draw by lot figures for program: ", figures_draw_by_lot)

    figures_give.clear()
    figures_draw_by_lot.clear()

    play_game = (input("Do you want to keep playing (yes/no): "))

# print(figures_draw_by_lot)
# print(figures_give)
