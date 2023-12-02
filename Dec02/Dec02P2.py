# Brayden Jonsson, 2023
import helper

file = open("challenge_text.txt", "r")

rolling_sum = 0

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
            red_count = helper.extract_int(game_round[red_location-3:red_location])
        if blue_location != -1:
            blue_count = helper.extract_int(game_round[blue_location-3:blue_location])
        if green_location != -1:
            green_count = helper.extract_int(game_round[green_location-3:green_location])

        if red_count > red_minimum:
            red_minimum = red_count
        if blue_count > blue_minimum:
            blue_minimum = blue_count
        if green_count > green_minimum:
            green_minimum = green_count

    rolling_sum += red_minimum * blue_minimum * green_minimum

print(rolling_sum)

file.close()
