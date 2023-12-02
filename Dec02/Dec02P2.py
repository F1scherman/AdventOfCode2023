# Brayden Jonsson, 2023

file = open("challenge_text.txt", "r")

sumGame = 0

for line in file:
    id_list = line.split(":")
    i = len(id_list[0]) - 1
    while id_list[0][i].isdigit():
        i -= 1
    gameId = int(id_list[0][i + 1:])
    game_list = id_list[1].split(";")

    red_minimum = 0
    blue_minimum = 0
    green_minimum = 0
    for game in game_list:
        if "Game" in game:
            continue
        red_location = game.find("red")
        blue_location = game.find("blue")
        green_location = game.find("green")
        red_count = 0
        blue_count = 0
        green_count = 0
        if red_location != -1:
            i = red_location - 2
            while game[i].isdigit():
                i -= 1
            red_count = int(game[i + 1:red_location - 1])
        if blue_location != -1:
            i = blue_location - 2
            while game[i].isdigit():
                i -= 1
            blue_count = int(game[i + 1:blue_location - 1])
        if green_location != -1:
            i = green_location - 2
            while game[i].isdigit():
                i -= 1
            green_count = int(game[i + 1:green_location - 1])

        if red_count > red_minimum:
            red_minimum = red_count
        if blue_count > blue_minimum:
            blue_minimum = blue_count
        if green_count > green_minimum:
            green_minimum = green_count
    sumGame += red_minimum * blue_minimum * green_minimum

print(sumGame)

file.close()
