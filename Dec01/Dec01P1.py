# Brayden Jonsson, 2023

file = open("challenge_text.txt", "r")
sumOfValues = 0

for line in file:
    num = 0
    for firstCharIndex in range(len(line)):
        if line[firstCharIndex].isdigit():
            num += int(line[firstCharIndex]) * 10
            break
    for lastCharIndex in range(len(line) - 1, -1, -1):
        if line[lastCharIndex].isdigit():
            num += int(line[lastCharIndex])
            break

    sumOfValues += num
print(sumOfValues)

file.close()
