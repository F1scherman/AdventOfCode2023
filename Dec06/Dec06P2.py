# Brayden Jonsson, 2023
import helper

file = open("challenge_text.txt", "r")
product_of_values = 1

race = (helper.extract_int(file.readline()), helper.extract_int(file.readline()))

minimum_valid_time = -1
maximum_valid_time = -1
for time in range(race[0]):
    speed = time
    distance = (race[0] - time) * speed

    if distance > race[1]:
        minimum_valid_time = time
        break
for time in range(race[0] - 1, -1 , -1):
    speed = time
    distance = (race[0] - time) * speed

    if distance > race[1]:
        maximum_valid_time = time
        break

product_of_values *= (maximum_valid_time - minimum_valid_time) + 1

print(product_of_values)

file.close()