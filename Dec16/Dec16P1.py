# Brayden Jonsson, 2023
from collections import deque

import helper

file = open("challenge_text.txt", "r")

matrix = []

for line in file:
    matrix.append(line[:-1])


energized_matrix = []
for line in matrix:
    energized_matrix.append([False for _ in range(len(line))])

beam_queue = deque()
beam_queue.append(("right", (0, 0)))

beam_set = set()

while len(beam_queue) != 0:
    (direction, (x, y)) = beam_queue.popleft()
    if not (0 <= x < len(matrix[0]) and 0 <= y < len(matrix)) or (direction, (x, y)) in beam_set:
        continue
    curr_item = matrix[y][x]
    energized_matrix[y][x] = True
    beam_set.add((direction, (x, y)))

    match curr_item:
        case ".":
            match direction:
                case "right":
                    beam_queue.append(("right", (x + 1, y)))
                case "left":
                    beam_queue.append(("left", (x - 1, y)))
                case "up":
                    beam_queue.append(("up", (x, y - 1)))
                case "down":
                    beam_queue.append(("down", (x, y + 1)))
        case "\\":
            match direction:
                case "right":
                    beam_queue.append(("down", (x, y + 1)))
                case "left":
                    beam_queue.append(("up", (x, y - 1)))
                case "up":
                    beam_queue.append(("left", (x - 1, y)))
                case "down":
                    beam_queue.append(("right", (x + 1, y)))
        case "/":
            match direction:
                case "left":
                    beam_queue.append(("down", (x, y + 1)))
                case "right":
                    beam_queue.append(("up", (x, y - 1)))
                case "down":
                    beam_queue.append(("left", (x - 1, y)))
                case "up":
                    beam_queue.append(("right", (x + 1, y)))
        case "|":
            match direction:
                case "right" | "left":
                    beam_queue.append(("up", (x, y - 1)))
                    beam_queue.append(("down", (x, y + 1)))
                case "up":
                    beam_queue.append(("up", (x, y - 1)))
                case "down":
                    beam_queue.append(("down", (x, y + 1)))
        case "-":
            match direction:
                case "up" | "down":
                    beam_queue.append(("left", (x - 1, y)))
                    beam_queue.append(("right", (x + 1, y)))
                case "right":
                    beam_queue.append(("right", (x + 1, y)))
                case "left":
                    beam_queue.append(("left", (x - 1, y)))

counter = 0
for line in energized_matrix:
    for item in line:
        if item:
            counter += 1

print(counter)

file.close()
