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
second_visited_matrix = []
for y in range(len(matrix)):
    second_visited_matrix.append([])
    for x in range(len(matrix[y])):
        second_visited_matrix[y].append(False)
counted_matrix = []
for y in range(len(matrix)):
    counted_matrix.append([])
    for x in range(len(matrix[y])):
        counted_matrix[y].append(False)
distance_matrix = []
for y in range(len(matrix)):
    distance_matrix.append([])
    for x in range(len(matrix[y])):
        distance_matrix[y].append(-99999999999999999999999999999999)
come_from_matrix = []
for y in range(len(matrix)):
    come_from_matrix.append([])
    for x in range(len(matrix[y])):
        come_from_matrix[y].append("nowhere")

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

    x_diff = come_from_x - x
    y_diff = come_from_y - y

    if x_diff == 0:
        if y_diff == -1:
            come_from_matrix[y][x] = "up"
        else:
            come_from_matrix[y][x] = "down"
    else:
        if x_diff == -1:
            come_from_matrix[y][x] = "left"
        else:
            come_from_matrix[y][x] = "right"

for y in range(len(matrix)):
    for x in range(len(matrix[y])):
        if matrix[y][x] == "S":
            break
    if matrix[y][x] == "S":
        break

neighbor_to_flip = neighbors_to_visit((x,y), pipe_type[matrix[y][x]], matrix, pipe_type)[0]

match come_from_matrix[neighbor_to_flip[1]][neighbor_to_flip[0]]:
    case "left":
        come_from_matrix[neighbor_to_flip[1]][neighbor_to_flip[0]] = "right"
    case "right":
        come_from_matrix[neighbor_to_flip[1]][neighbor_to_flip[0]] = "left"
    case "up":
        come_from_matrix[neighbor_to_flip[1]][neighbor_to_flip[0]] = "down"
    case "down":
        come_from_matrix[neighbor_to_flip[1]][neighbor_to_flip[0]] = "up"

count = 0
while not second_visited_matrix[y][x]:
    second_visited_matrix[y][x] = True
    if matrix[y][x] in ["_", "|"]:
        match come_from_matrix[y][x]:
            case "up":
                temp_count = 0
                broke = False
                for i in range(x + 1, len(matrix[y])):
                    if visited_matrix[y][i]:
                        broke = True
                        break
                    if not counted_matrix[y][i]:
                        counted_matrix[y][i] = True
                        temp_count += 1
                if broke:
                    count += temp_count
            case "down":
                temp_count = 0
                broke = False
                for i in range(x - 1, 0, -1):
                    if visited_matrix[y][i]:
                        broke = True
                        break
                    if not counted_matrix[y][i]:
                        counted_matrix[y][i] = True
                        temp_count += 1
                if broke:
                    count += temp_count
            case "left":
                temp_count = 0
                broke = False
                for i in range(y - 1, 0, -1):
                    if visited_matrix[i][x]:
                        broke = True
                        break
                    if not counted_matrix[i][x]:
                        counted_matrix[i][x] = True
                        temp_count += 1
                if broke:
                    count += temp_count
            case "right":
                temp_count = 0
                broke = False
                for i in range(y + 1, len(matrix)):
                    if visited_matrix[i][x]:
                        broke = True
                        break
                    if not counted_matrix[i][x]:
                        counted_matrix[i][x] = True
                        temp_count += 1
                if broke:
                    count += temp_count

    match come_from_matrix[y][x]:
        case "up":
            y -= 1
        case "down":
            y += 1
        case "left":
            x -= 1
        case "right":
            x += 1



print(count)
# 0

file.close()
