# Brayden Jonsson, 2023

import helper
from itertools import cycle


def insertion_ish_sort(arr: [str]):
    for i in range(1, len(arr)):
        if arr[i] != "O":
            continue
        current_index = i
        while current_index > 0:
            if arr[current_index - 1] == ".":
                helper.swap(arr, current_index - 1, current_index)
                current_index -= 1
            else:
                break


def rotate_matrix(arr: [[str]]):
    """Rotates a matrix 90* clockwise"""
    transposed_matrix = helper.transpose_matrix(arr)
    return_matrix = [row[::-1] for row in transposed_matrix]
    return return_matrix


file = open("challenge_text.txt", "r")

row_matrix = []
for line in file:
    row_matrix.append(line[:-1])

matrix = rotate_matrix(rotate_matrix(rotate_matrix(row_matrix)))

warm_up_cycles = 1_000

pattern_cycles = 10_000
pattern_list = []
for i in range(1_000_000_000):
    for j in range(4):
        for column in matrix:
            insertion_ish_sort(column)

        matrix = rotate_matrix(matrix)

    if warm_up_cycles <= i <= warm_up_cycles + pattern_cycles:
        temp_sum_of_values = 0
        for column in matrix:
            for i in range(len(column)):
                if column[i] == "O":
                    temp_sum_of_values += len(column) - i

        pattern_list.append(temp_sum_of_values)
    elif i > warm_up_cycles + pattern_cycles:
        break

print("Completed Processing!")

new_pattern_list = []
for i in range(len(pattern_list)):
    new_pattern_list.append(pattern_list[i])
    if new_pattern_list == pattern_list[i + 1:i + 1 + len(new_pattern_list)]:
        print("Pattern found!")
        break

print(new_pattern_list)
required_cycles = 1_000_000_000 - warm_up_cycles - 1
last_item = required_cycles % len(new_pattern_list)

print(new_pattern_list[last_item])

file.close()
