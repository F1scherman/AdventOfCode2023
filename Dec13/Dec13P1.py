# Brayden Jonsson, 2023

import helper


def search_for_mirrors(arr: [int]):
    current_index = 0
    while current_index < len(arr) - 1:
        if arr[current_index] == arr[current_index + 1]:
            offset = 1
            valid_num = True
            while 0 <= current_index - offset and current_index + 1 + offset < len(arr):
                if arr[current_index - offset] != arr[current_index + 1 + offset]:
                    valid_num = False
                    break
                offset += 1
            if valid_num:
                return current_index + 1
        current_index += 1
    return 0


file = open("challenge_text.txt", "r")

row_matrix = []

sum_of_values = 0

for line in file:
    # I have to purposefully add a newline to the end of the file for this :/
    if line.strip() != "":
        row_matrix.append([])
        for char in line:
            if char != "\n":
                row_matrix[-1].append(char)
    else:
        column_matrix = helper.make_column_matrix(row_matrix)

        rows = [helper.arr_to_int(row, "#") for row in row_matrix]
        columns = [helper.arr_to_int(column, "#") for column in column_matrix]

        row_count = search_for_mirrors(rows)
        column_count = search_for_mirrors(columns) if row_count == 0 else 0

        sum_of_values += column_count + row_count * 100
        row_matrix.clear()


print(sum_of_values)

file.close()
