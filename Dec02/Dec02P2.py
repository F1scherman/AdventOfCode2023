# Brayden Jonsson, 2023

file = open("challenge_text.txt", "r")

sum_game = 0

for line in file:
    id_list = line.split(":")
    round_list = id_list[1].split(";")

    red_minimum = 0
    blue_minimum = 0
    green_minimum = 0

    for game_round in round_list:
        red_location = game_round.find("red")
        blue_location = game_round.find("blue")
        green_location = game_round.find("green")

        red_count = 0
        blue_count = 0
        green_count = 0

        if red_location != -1:
            i = red_location - 2
            while game_round[i].isdigit():
                i -= 1
            red_count = int(game_round[i + 1:red_location - 1])

        if blue_location != -1:
            i = blue_location - 2
            while game_round[i].isdigit():
                i -= 1
            blue_count = int(game_round[i + 1:blue_location - 1])

        if green_location != -1:
            i = green_location - 2
            while game_round[i].isdigit():
                i -= 1
            green_count = int(game_round[i + 1:green_location - 1])

        if red_count > red_minimum:
            red_minimum = red_count
        if blue_count > blue_minimum:
            blue_minimum = blue_count
        if green_count > green_minimum:
            green_minimum = green_count

    sum_game += red_minimum * blue_minimum * green_minimum

print(sum_game)

file.close()
