# Brayden Jonsson, 2023
from collections import deque

import helper


def neighbors_to_visit(coords: (int, int), neighbors_checking: [str], matrix, pipe_type):
    valid_neighbors = []
    if coords[0] - 1 >= 0 and "left" in neighbors_checking:
        valid_neighbors.append((coords[0] - 1, coords[1], "right"))
    if coords[0] + 1 < len(matrix[0]) and "right" in neighbors_checking:
        valid_neighbors.append((coords[0] + 1, coords[1], "left"))
    if coords[1] - 1 >= 0 and "up" in neighbors_checking:
        valid_neighbors.append((coords[0], coords[1] - 1, "down"))
    if coords[0] + 1 >= 0 and "down" in neighbors_checking:
        valid_neighbors.append((coords[0], coords[1] + 1, "up"))

    return_neighbors = []
    for neighbor in valid_neighbors:
        if neighbor[2] in pipe_type[matrix[neighbor[1]][neighbor[0]]]:
            return_neighbors.append((neighbor[0], neighbor[1]))

    return return_neighbors


pipe_type = {"S": ["up", "down", "left", "right"],
             "|": ["up", "down"],
             "-": ["left", "right"],
             "F": ["right", "down"],
             "J": ["left", "up"],
             "L": ["right", "up"],
             "7": ["left", "down"],
             ".": []}
list_of_vertical_pipes = ["F", "J", "L", "7", "|"]
list_of_horizontal_pipes = ["F", "J", "L", "7", "-"]
file = open("sample_text4.txt", "r")
sum_of_values = 0

matrix = []

for line in file:
    matrix.append(line[:-1])


visited_matrix = []
for y in range(len(matrix)):
    visited_matrix.append([])
    for x in range(len(matrix[y])):
        visited_matrix[y].append(False)
horizontal_counted_matrix = []
for y in range(len(matrix)):
    horizontal_counted_matrix.append([])
    for x in range(len(matrix[y])):
        horizontal_counted_matrix[y].append(False)
vertical_counted_matrix = []
for y in range(len(matrix)):
    vertical_counted_matrix.append([])
    for x in range(len(matrix[y])):
        vertical_counted_matrix[y].append(False)
distance_matrix = []
for y in range(len(matrix)):
    distance_matrix.append([])
    for x in range(len(matrix[y])):
        distance_matrix[y].append(-99999999999999999999999999999999)

for y in range(len(matrix)):
    for x in range(len(matrix[y])):
        if matrix[y][x] == "S":
            break
    if matrix[y][x] == "S":
        break

queue = deque()

queue.append((x, y, -1, -1))
distance_matrix[y][x] = 0
visited_matrix[y][x] = True

while len(queue) != 0:
    x, y, come_from_x, come_from_y = queue.pop()

    neighbors_to_append = neighbors_to_visit((x,y), pipe_type[matrix[y][x]], matrix, pipe_type)

    for neighbor in neighbors_to_append:
        if visited_matrix[neighbor[1]][neighbor[0]]:
            continue
        visited_matrix[neighbor[1]][neighbor[0]] = True
        distance_matrix[neighbor[1]][neighbor[0]] = distance_matrix[y][x] + 1
        queue.append((neighbor[0], neighbor[1], x, y))

for y in range(len(matrix)):
    for x in range(len(matrix[y])):
        if matrix[y][x] == "S":
            break
    if matrix[y][x] == "S":
        break

neighbors = neighbors_to_visit((x,y), pipe_type[matrix[y][x]], matrix, pipe_type)

for neighbor in neighbors:
    if matrix[neighbor[1]][neighbor[0]] in list_of_vertical_pipes:
        list_of_vertical_pipes.append("S")
        break

for neighbor in neighbors:
    if matrix[neighbor[1]][neighbor[0]] in list_of_horizontal_pipes:
        list_of_horizontal_pipes.append("S")
        break

vertical_count = 0
for y in range(len(matrix)):
    temp_count = 0
    temp_addresses = []
    counting = False
    for x in range(len(matrix[y])):
        if matrix[y][x] in list_of_vertical_pipes:
            counting = not counting
        if counting and not visited_matrix[y][x]:
            temp_count += 1
            vertical_counted_matrix[y][x] = True
        if not counting:
            vertical_count += temp_count
            temp_count = 0
            for my_x, my_y in temp_addresses:
                vertical_counted_matrix[my_y][my_x] = True
            temp_addresses.clear()

horizontal_count = 0
for x in range(len(matrix[0])):
    temp_count = 0
    temp_addresses = []
    counting = False
    for y in range(len(matrix)):
        if matrix[y][x] in list_of_horizontal_pipes:
            counting = not counting
        if counting and not visited_matrix[y][x]:
            temp_count += 1
            temp_addresses.append((x, y))
        if not counting:
            horizontal_count += temp_count
            temp_count = 0
            for my_x, my_y in temp_addresses:
                horizontal_counted_matrix[my_y][my_x] = True
            temp_addresses.clear()

count = 0
for y in range(len(vertical_counted_matrix)):
    for x in range(len(vertical_counted_matrix[y])):
        if vertical_counted_matrix[y][x] and horizontal_counted_matrix[y][x]:
            count += 1

print(count)
# 0

file.close()
