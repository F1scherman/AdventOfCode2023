# Brayden Jonsson, 2023
import helper

file = open("sample_text.txt", "r")

maps = [[], [], [], [], [], [], []]
currentMap = -1

seed_line = file.readline()
parsed_seed_line = helper.extract_all_ints(seed_line)

seeds = []
for i in range(0, len(parsed_seed_line), 2):
    for j in range(parsed_seed_line[i+1]):
        seeds.append(parsed_seed_line[i] + j)

for line in file:
    if not line.strip():
        continue
    elif line[0].isdigit():
        values = helper.extract_all_ints(line)
        maps[currentMap].append((range(values[1], values[1] + values[2]), values[1], values[0]))
    else:
        currentMap += 1

lowest_possible_values = [0]

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
