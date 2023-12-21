# Brayden Jonsson, 2023
from collections import deque
import helper
from math import gcd

file = open("sample_text.txt", "r")
matrix_size = 1_000

current_point = (matrix_size//2, matrix_size//2)

matrix = [["." for x in range(matrix_size)] for y in range(matrix_size)]

matrix[current_point[1]][current_point[0]] = "#"

dig_instructions = []

for line in file:
    hex_rep = line.split("(")[1][1:-2]

    instruction = int(hex_rep[-1])
    num = int(hex_rep[:-1], 16)

    match instruction:
        case 0:
            dig_instructions.append(("R", num))
        case 1:
            dig_instructions.append(("D", num))
        case 2:
            dig_instructions.append(("L", num))
        case 3:
            dig_instructions.append(("U", num))


# Brute force won't work, the sample would require over a terabyte of memory
flood_fill_queue = deque()
flood_fill_queue.append((current_point[0] - 1, current_point[1] - 1))

while flood_fill_queue:
    x, y = flood_fill_queue.popleft()
    if not (0 <= x < len(matrix[0])):
        continue
    if not (0 <= y < len(matrix)):
        continue
    if matrix[y][x] == "#":
        continue

    matrix[y][x] = "#"
    flood_fill_queue.append((x - 1, y))
    flood_fill_queue.append((x + 1, y))
    flood_fill_queue.append((x, y - 1))
    flood_fill_queue.append((x, y + 1))


count = 0

for y in matrix:
    for x in y:
        if x == "#":
            count += 1

print(count)


file.close()
