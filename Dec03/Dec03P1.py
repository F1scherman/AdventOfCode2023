# Brayden Jonsson, 2023
import helper

file = open("challenge_text.txt", "r")
sumOfValues = 0

matrix = []
# tuples, first value is the number, second value is a coordinate tuple
all_numbers = set()
line_count = 0
for line in file:
    matrix.append(line)
    for i in range(len(line)):
        if line[i].isdigit():
            number = helper.extract_int_at_location(line, i)
            location = 0
            if i - 5 < 0:
                location = line.find(str(number))
            else:
                location = line[i - 5:].find(str(number)) + i - 5
            all_numbers.add((number, (location, line_count)))

    line_count += 1

for (number, coordinates) in all_numbers:
    for x in range(coordinates[0] - 1, coordinates[0] + len(str(number)) + 1, 1):
        broke = False
        for y in range(coordinates[1] - 1, coordinates[1] + 2, 1):
            if y >= len(matrix) or y < 0 or x < 0 or x >= len(matrix[y]):
                continue
            if matrix[y][x] != "." and not matrix[y][x].isdigit() and matrix[y][x] != "\n":
                sumOfValues += number
                broke = True
                break
        if broke:
            break

print(sumOfValues)

file.close()
