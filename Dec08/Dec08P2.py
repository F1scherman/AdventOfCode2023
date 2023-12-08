# Brayden Jonsson, 2023
import helper

def check_if_win(arr):
    for key in arr:
        if key[-1] != "Z":
            return False
    return True

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

current_steps = []
for step in next_step.keys():
    if step[-1] == "A":
        current_steps.append(step)

won = False
while not won:
    for c in instruction_line:
        if check_if_win(current_steps):
            won = True
            break
        if c == "R":
            for i in range(len(current_steps)):
                current_steps[i] = next_step[current_steps[i]][1]
        else:
            for i in range(len(current_steps)):
                current_steps[i] = next_step[current_steps[i]][0]
        sum_of_values += 1



print(sum_of_values)

file.close()
