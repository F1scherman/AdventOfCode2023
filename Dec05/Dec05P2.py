# Brayden Jonsson, 2023
# I had to read Sam Hill (@Soshjam)'s submission like 20 times to get the solution
import helper

UNREASONABLY_LARGE_NUMBER = 9999999999999999999999999999999999999999999999999999999


def find_slices(start_point: int):
    start_range = UNREASONABLY_LARGE_NUMBER

    for map_index in range(len(maps) - 1, -1, -1):
        current_map = maps[map_index]

        min_interval_distance = UNREASONABLY_LARGE_NUMBER

        for interval in current_map:
            dest = interval[0]
            source = interval[1]
            length = interval[2]

            if dest <= start_point < dest + length:
                offset = start_point - dest
                start_point = offset + source

                start_range = min(start_range, length - offset)
                break

            else:
                distance = dest - start_point

                if distance > 0:
                    min_interval_distance = min(min_interval_distance, distance)
        else:
            start_range = min(start_range, min_interval_distance)

    min_seed_distance = UNREASONABLY_LARGE_NUMBER

    for seed in seeds:
        start = seed[0]
        length = seed[1]
        end = start + length

        if start <= start_point < end:
            return start_range, 0, True

        distance = start - start_point
        if distance < 0:
            continue

        min_seed_distance = min(distance, min_seed_distance)

    success = not (min_seed_distance > start_range)

    return start_range, min_seed_distance, success


file = open("sample_text.txt", "r")

currentMap = -1
seed_line = file.readline()
parsed_seed_line = helper.extract_all_ints(seed_line)

# seeds is formatted like so:
# [
#   (
#       seed-starting-point,
#       seed-range
#   ),
#   ...
# ]
seeds = []
for i in range(0, len(parsed_seed_line), 2):
    seeds.append( (parsed_seed_line[i], parsed_seed_line[i+1]) )

# maps is formatted like so:
# [
#   [
#       (
#           destination-starting-point,
#           source-starting-point,
#           map-range
#       ),
#       ...
#   ],
#   ...
# ]
maps = []
for line in file:
    if not line.strip():
        continue
    elif line[0].isdigit():
        values = helper.extract_all_ints(line)
        maps[currentMap].append( (values[0], values[1], values[2]) )
    else:
        currentMap += 1
        maps.append([])

# Essentially, we start from the lowest possible value and continue onward until we find one that has a hit
current_point = 0
lowest_location = -1
done = False

while not done:
    results = find_slices(current_point)
    done = results[2]

    if done:
        lowest_location = current_point + results[1]
    else:
        current_point = current_point + results[0]

print(lowest_location)

file.close()
