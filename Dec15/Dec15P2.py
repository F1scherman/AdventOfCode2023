# Brayden Jonsson, 2023

import helper
import re

file = open("challenge_text.txt", "r")
sum_of_values = 0

inputs = file.readline().split(",")

boxes = {}

for string in inputs:
    split_string = re.split(r"([=-])", string)
    operator = split_string[1]
    label = split_string[0]
    if operator == "=":
        lens_number = int(split_string[2])
    else:
        lens_number = -1

    label_hash = 0
    for char in label:
        label_hash += ord(char)
        label_hash *= 17
        label_hash %= 256

    if label_hash not in boxes:
        boxes[label_hash] = []
    box = boxes[label_hash]

    if operator == "-":
        for lens in box:
            if lens[0] == label:
                box.remove(lens)
                break
    else:
        for lens in box:
            if lens[0] == label:
                lens[1] = lens_number
                break
        else:
            box.append([label, lens_number])

for box_number, box in boxes.items():
    for i in range(len(box)):
        focusing_power = box_number + 1
        focusing_power *= i + 1
        focusing_power *= box[i][1]

        sum_of_values += focusing_power

print(sum_of_values)

file.close()
