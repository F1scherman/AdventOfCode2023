# Brayden Jonsson, 2023

import helper

GALAXY_EXPANSION_MULTIPLIER = 1_000_000
file = open("challenge_text.txt", "r")

matrix = []
for line in file:
    matrix.append([])
    for char in line:
        if char != "\n":
            matrix[-1].append(char)

# Handle Expansion
rows_to_add = []
for row_index in range(len(matrix)):
    if helper.is_all_equal_to(matrix[row_index], "."):
        rows_to_add.append(row_index)

columns_to_add = []
for column_index in range(len(matrix[0])):
    column = [row[column_index] for row in matrix]
    if helper.is_all_equal_to(column, "."):
        columns_to_add.append(column_index)

# Find all galaxies
galaxies = []
for y in range(len(matrix)):
    for x in range(len(matrix[0])):
        if matrix[y][x] == "#":
            galaxies.append((x, y))

# Manhattan Distance between each
print(len(galaxies))
sum_of_values = 0
for i in range(len(galaxies)):
    print(i)
    for j in range(i + 1, len(galaxies)):
        x_distance = abs(galaxies[i][0] - galaxies[j][0])
        if galaxies[i][0] < galaxies[j][0]:
            in_between_columns = [column for column in columns_to_add if galaxies[i][0] < column < galaxies[j][0]]
        else:
            in_between_columns = [column for column in columns_to_add if galaxies[j][0] < column < galaxies[i][0]]
        y_distance = abs(galaxies[i][1] - galaxies[j][1])
        if galaxies[i][1] < galaxies[j][1]:
            in_between_rows = [row for row in rows_to_add if galaxies[i][1] < row < galaxies[j][1]]
        else:
            in_between_rows = [row for row in rows_to_add if galaxies[j][1] < row < galaxies[i][1]]
        sum_of_values += x_distance + y_distance
        sum_of_values += (len(in_between_columns) + len(in_between_rows)) * (GALAXY_EXPANSION_MULTIPLIER - 1)

print(sum_of_values)

file.close()
