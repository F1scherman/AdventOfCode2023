# Brayden Jonsson, 2023
import helper

file = open("challenge_text.txt", "r")

maps = [[], [], [], [], [], [], []]
currentMap = -1

seed_line = file.readline()
seeds = helper.extract_all_ints(seed_line)

for line in file:
    if not line.strip():
        continue
    elif line[0].isdigit():
        values = helper.extract_all_ints(line)
        maps[currentMap].append((range(values[1], values[1] + values[2]), values[1], values[0]))
    else:
        currentMap += 1

lowestLocation = 99999999999999999999999999999999999999999
for seed in seeds:
    currentValue = seed
    for currentMap in maps:
        for currentTup in currentMap:
            if currentValue in currentTup[0]:
                currentValue = currentValue - currentTup[1] + currentTup[2]
                break

    if currentValue < lowestLocation:
        lowestLocation = currentValue

print(lowestLocation)

file.close()
