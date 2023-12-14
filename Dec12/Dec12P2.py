# Brayden Jonsson, 2023

# Heavily relied on Stefan Todorov's (@coravacav) solution for this one.

import helper


def generate_possibilities(field : str, nums : tuple[int], damaged_count: int, cache):
    if (field, nums, damaged_count) in cache:
        return cache[(field, nums, damaged_count)]

    if len(nums) == 0:
        return 0

    if damaged_count == nums[0]:
        nums = nums[1:]
        damaged_count = 256
        if len(nums) == 0:
            return 0 if field.find("#") != -1 else 1

    if len(field) == 0:
        return 0
    else:
        cell = field[0]

    match cell:
        case "#":
            if damaged_count == 256:
                return 0
            else:
                res = generate_possibilities(field[1:], nums, damaged_count + 1, cache)
                cache[(field[1:], nums, damaged_count + 1)] = res
                return res
        case ".":
            if 0 < damaged_count < 256:
                return 0
            else:
                res = generate_possibilities(field[1:], nums, 0, cache)
                cache[(field[1:], nums, 0)] = res
                return res
        case "?":
            if damaged_count == 256:
                damaged_res = 0
            else:
                damaged_res = generate_possibilities(field[1:], nums, damaged_count + 1, cache)
                cache[(field[1:], nums, damaged_count + 1)] = damaged_res
            if 0 < damaged_count < 256:
                operational_res = 0
            else:
                operational_res = generate_possibilities(field[1:], nums, 0, cache)
                cache[(field[1:], nums, 0)] = operational_res
            return damaged_res + operational_res
        case _:
            raise Exception()


file = open("challenge_text.txt", "r")

sum_of_values = 0

for line in file:
    nums = helper.extract_all_ints(line) * 5
    # has to be a tuple for hashing (mutability probably)
    nums = tuple(nums)
    # unstripped field just adds together all 5 repeats with the extra question mark,
    # field removes repeated duplicates (they are redundant)
    # and intentionally leaves off the last question mark (not in spec)
    unstripped_field = ((line.split()[0] + "?") * 5)
    field = ''.join([unstripped_field[i] for i in range(len(unstripped_field) - 1)
             if unstripped_field[i] != "." or unstripped_field[i+1] != "."])

    cache = {}

    sum_of_values += generate_possibilities(field, nums, 0, cache)

print(sum_of_values)
