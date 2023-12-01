# Brayden Jonsson, 2023

file = open("challenge_text.txt", "r")
sumOfValues = 0
mapNameToNum = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

for line in file:
    smallestIndex = 999999999999
    smallestIndexValue = 0
    largestIndex = -1
    largestIndexValue = 0
    for key in mapNameToNum.keys():
        index = 0
        try:
            index = line.index(key)
        except ValueError:
            continue
        if index < smallestIndex:
            smallestIndex = index
            smallestIndexValue = mapNameToNum[key]

    for key in mapNameToNum.keys():
        index = line.rfind(key)
        if index > largestIndex:
            largestIndex = index
            largestIndexValue = mapNameToNum[key]

    for value in mapNameToNum.values():
        index = 0
        try:
            index = line.index(str(value))
        except ValueError:
            continue
        if index < smallestIndex:
            smallestIndex = index
            smallestIndexValue = value

    for value in mapNameToNum.values():
        index = line.rfind(str(value))
        if index > largestIndex:
            largestIndex = index
            largestIndexValue = value

    sumOfValues += largestIndexValue + smallestIndexValue * 10

print(sumOfValues)

file.close()
