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
file = open("challenge_text.txt", "r")
sum_of_values = 0

matrix = []

for line in file:
    matrix.append(line[:-1])


visited_matrix = []
for y in range(len(matrix)):
    visited_matrix.append([])
    for x in range(len(matrix[y])):
        visited_matrix[y].append(False)
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

queue.append((x,y))
distance_matrix[y][x] = 0
visited_matrix[y][x] = True

while len(queue) != 0:
    x, y = queue.popleft()

    neighbors_to_append = neighbors_to_visit((x,y), pipe_type[matrix[y][x]], matrix, pipe_type)

    for neighbor in neighbors_to_append:
        if visited_matrix[neighbor[1]][neighbor[0]]:
            continue
        visited_matrix[neighbor[1]][neighbor[0]] = True
        distance_matrix[neighbor[1]][neighbor[0]] = distance_matrix[y][x] + 1
        queue.append((neighbor[0], neighbor[1]))

maximums = [max(line) for line in distance_matrix]

print(max(maximums))

file.close()
