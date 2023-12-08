# Brayden Jonsson, 2023
import helper
import math

# def check_if_win(arr):
#     for key in arr:
#         if key[-1] != "Z":
#             return False
#     return True

def check_if_win(value: str):
    return value[-1] == "Z"

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

nodes = []
for node in next_step.keys():
    if node[-1] == "A":
        nodes.append(node)

nodes_repeats = []
for node in nodes:
    count = 0
    current_node = node
    while not check_if_win(current_node):
        for c in instruction_line:
            if check_if_win(current_node):
                break
            if c == "R":
                current_node = next_step[current_node][1]
            else:
                current_node = next_step[current_node][0]
            count += 1

    nodes_repeats.append(count)

sum_of_values = 1
for node_count in nodes_repeats:
    sum_of_values = math.lcm(sum_of_values, node_count)

print(sum_of_values)

file.close()
