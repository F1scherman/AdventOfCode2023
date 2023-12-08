# Brayden Jonsson, 2023
import helper

file = open("challenge_text.txt", "r")
sum_of_values = 0

instruction_line = file.readline().strip()

# skip empty line
file.readline()

next_step = {}

for line in file:
    key = line[0:3]
    value_1 = line[7:10]
    value_2 = line[12:15]

    next_step[key] = (value_1, value_2)

current_step = "AAA"
while current_step != "ZZZ":
    for c in instruction_line:
        if current_step == "ZZZ":
            break
        if c == "R":
            current_step = next_step[current_step][1]
        else:
            current_step = next_step[current_step][0]
        sum_of_values += 1


print(sum_of_values)

file.close()
