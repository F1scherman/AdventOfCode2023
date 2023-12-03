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

for y in range(len(matrix)):
    for x in range(len(matrix[y])):
        if matrix[y][x] != "*":
            continue
        nums = set()
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if matrix[j][i].isdigit():
                    nums.add(helper.extract_int_at_location(matrix[j], i))
        if len(nums) != 2:
            continue

        finalNum = 1
        for num in nums:
            finalNum *= num

        sumOfValues += finalNum

print(sumOfValues)

file.close()
