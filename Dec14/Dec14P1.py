# Brayden Jonsson, 2023

import helper


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


file = open("challenge_text.txt", "r")

row_matrix = []
for line in file:
    row_matrix.append(line[:-1])

columns = helper.transpose_matrix(row_matrix)

sum_of_values = 0
for column in columns:
    insertion_ish_sort(column)
    for i in range(len(column)):
        if column[i] == "O":
            sum_of_values += len(column) - i

print(sum_of_values)

file.close()
