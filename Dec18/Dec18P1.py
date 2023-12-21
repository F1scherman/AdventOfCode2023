# Brayden Jonsson, 2023
from collections import deque

import helper

file = open("challenge_text.txt", "r")
matrix_size = 1_000

current_point = (matrix_size//2, matrix_size//2)

matrix = [["." for x in range(matrix_size)] for y in range(matrix_size)]

matrix[current_point[1]][current_point[0]] = "#"

for line in file:
    num = helper.extract_all_ints(line)[0]
    instruction = line[0]

    match instruction:
        case "U":
            for y in range(1, num + 1):
                matrix[current_point[1] - y][current_point[0]] = "#"
            current_point = (current_point[0], current_point[1] - y)
        case "D":
            for y in range(1, num + 1):
                matrix[current_point[1] + y][current_point[0]] = "#"
            current_point = (current_point[0], current_point[1] + y)
        case "L":
            for x in range(1, num + 1):
                matrix[current_point[1]][current_point[0] - x] = "#"
            current_point = (current_point[0] - x, current_point[1])
        case "R":
            for x in range(1, num + 1):
                matrix[current_point[1]][current_point[0] + x] = "#"
            current_point = (current_point[0] + x, current_point[1])

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
