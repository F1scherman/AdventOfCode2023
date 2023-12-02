# Brayden Jonsson, 2023

file = open("challenge_text.txt", "r")

sum_game = 0

for line in file:
    id_list = line.split(":")
    i = len(id_list[0]) - 1
    while id_list[0][i].isdigit():
        i -= 1
    game_id = int(id_list[0][i + 1:])
    round_list = id_list[1].split(";")

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

        if red_count > 12 or green_count > 13 or blue_count > 14:
            break
    else:
        sum_game += game_id


print(sum_game)

file.close()
