# Brayden Jonsson, 2023
from collections import deque

import helper


def neighbors_to_visit(coords: (int, int), neighbors_checking: [str], matrix, pipe_type):
    valid_neighbors = []
    if coords[0] - 1 >= 0 and "left" in neighbors_checking:
        valid_neighbors.append((coords[0] - 1, coords[1], "right"))
    if coords[1] - 1 >= 0 and "up" in neighbors_checking:
        valid_neighbors.append((coords[0], coords[1] - 1, "down"))
    if coords[0] + 1 < len(matrix[0]) and "right" in neighbors_checking:
        valid_neighbors.append((coords[0] + 1, coords[1], "left"))
    if coords[1] + 1 < len(matrix[0]) and "down" in neighbors_checking:
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
file = open("challenge_text.txt", "r")
sum_of_values = 0

matrix = []

for line in file:
    matrix.append([])
    for char in line:
        if char != "\n":
            matrix[-1].append(char)


visited_matrix = []
for y in range(len(matrix)):
    visited_matrix.append([])
    for x in range(len(matrix[y])):
        visited_matrix[y].append(False)
come_from_matrix = []
for y in range(len(matrix)):
    come_from_matrix.append([])
    for x in range(len(matrix[y])):
        come_from_matrix[y].append("nowhere")

for start_y in range(len(matrix)):
    for start_x in range(len(matrix[y])):
        if matrix[start_y][start_x] == "S":
            break
    if matrix[start_y][start_x] == "S":
        break

queue = deque()

queue.append((start_x, start_y, -1, -1))
visited_matrix[start_y][start_x] = True

# Step 1: DFS to create a loop
while len(queue) != 0:
    x, y, prev_x, prev_y = queue.pop()

    neighbors_to_append = neighbors_to_visit((x, y), pipe_type[matrix[y][x]], matrix, pipe_type)
    if matrix[y][x] == "S":
        neighbors_to_append = neighbors_to_append[0:1]
    for neighbor in neighbors_to_append:
        if visited_matrix[neighbor[1]][neighbor[0]]:
            continue
        visited_matrix[neighbor[1]][neighbor[0]] = True
        queue.append((neighbor[0], neighbor[1], x, y))

    x_diff = prev_x - x
    y_diff = prev_y - y
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

# Step 2: Remove any pipes that aren't part of the loop
for y in range(len(matrix)):
    for x in range(len(matrix[y])):
        if not visited_matrix[y][x]:
            matrix[y][x] = "."


# Step 3: Go through the loop, paint any dirt to the left side of the pipes
# May need to switch side based on input
current_neighbor = neighbors_to_visit((start_x, start_y), pipe_type[matrix[start_y][start_x]], matrix, pipe_type)[-1]

while current_neighbor != (start_x, start_y):
    match come_from_matrix[current_neighbor[1]][current_neighbor[0]]:
        case "down":
            paint_coords = (current_neighbor[0] - 1, current_neighbor[1])
            if paint_coords[0] < len(matrix[0]) and matrix[paint_coords[1]][paint_coords[0]] == ".":
                matrix[paint_coords[1]][paint_coords[0]] = "#"
            current_neighbor = (current_neighbor[0], current_neighbor[1] + 1)
        case "up":
            paint_coords = (current_neighbor[0] + 1, current_neighbor[1])
            if paint_coords[0] >= 0 and matrix[paint_coords[1]][paint_coords[0]] == ".":
                matrix[paint_coords[1]][paint_coords[0]] = "#"
            current_neighbor = (current_neighbor[0], current_neighbor[1] - 1)
        case "left":
            paint_coords = (current_neighbor[0], current_neighbor[1] - 1)
            if paint_coords[1] >= 0 and matrix[paint_coords[1]][paint_coords[0]] == ".":
                matrix[paint_coords[1]][paint_coords[0]] = "#"
            current_neighbor = (current_neighbor[0] - 1, current_neighbor[1])
        case "right":
            paint_coords = (current_neighbor[0], current_neighbor[1] + 1)
            if paint_coords[1] < len(matrix) and matrix[paint_coords[1]][paint_coords[0]] == ".":
                matrix[paint_coords[1]][paint_coords[0]] = "#"
            current_neighbor = (current_neighbor[0] + 1, current_neighbor[1])

# Step 4: Now floodfill based on where hashtags currently are
flood_fill_queue = deque()
for y in range(len(matrix)):
    for x in range(len(matrix[y])):
        if matrix[y][x] == "#":
            flood_fill_queue.append((x,y))

while len(flood_fill_queue) != 0:
    (x,y) = flood_fill_queue.popleft()
    if matrix[y][x] == ".":
        matrix[y][x] = "#"

    if matrix[y-1][x] == ".":
        flood_fill_queue.append((x, y-1))
    if matrix[y+1][x] == ".":
        flood_fill_queue.append((x, y+1))
    if matrix[y][x-1] == ".":
        flood_fill_queue.append((x-1, y))
    if matrix[y][x+1] == ".":
        flood_fill_queue.append((x+1, y))

count = 0
# Step 5: Count hashtags
for y in matrix:
    for x in y:
        if x == "#":
            count += 1

print(count)
# 0

file.close()
