# Brayden Jonsson, 2023
import helper
file = open("challenge_text.txt", "r")

sum_game = 0

for line in file:
    id_list = line.split(":")
    game_id = helper.extract_int(id_list[0])
    round_list = id_list[1].split(";")

    for game_round in round_list:
        red_location = game_round.find("red")
        blue_location = game_round.find("blue")
        green_location = game_round.find("green")

        red_count = 0
        blue_count = 0
        green_count = 0

        if red_location != -1:
            red_count = helper.extract_int(game_round[red_location-3:red_location])

        if blue_location != -1:
            blue_count = helper.extract_int(game_round[blue_location-3:blue_location])

        if green_location != -1:
            green_count = helper.extract_int(game_round[green_location-3:green_location])

        if red_count > 12 or green_count > 13 or blue_count > 14:
            break
    else:
        sum_game += game_id


print(sum_game)

file.close()
