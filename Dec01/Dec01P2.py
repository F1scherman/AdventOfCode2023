# Brayden Jonsson, 2023

file = open("challenge_text.txt", "r")
sum_of_values = 0
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
        index = line.find(key)
        if index != -1 and index < smallestIndex:
            smallestIndex = index
            smallestIndexValue = mapNameToNum[key]

        index = line.rfind(key)
        if index > largestIndex:
            largestIndex = index
            largestIndexValue = mapNameToNum[key]

    for value in mapNameToNum.values():
        valueString = str(value)
        index = line.find(valueString)
        if index != -1 and index < smallestIndex:
            smallestIndex = index
            smallestIndexValue = value

        index = line.rfind(valueString)
        if index > largestIndex:
            largestIndex = index
            largestIndexValue = value

    sum_of_values += largestIndexValue + smallestIndexValue * 10

print(sum_of_values)

file.close()
