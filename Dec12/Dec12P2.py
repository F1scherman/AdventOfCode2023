# Brayden Jonsson, 2023
import helper


def validate_list(arr: [str], nums: [int]):
    current_nums_index = 0
    current_arr_index = 0
    counting = arr[0] == "#"
    start_index = 0
    while current_arr_index < len(arr) and current_nums_index < len(nums):
        if arr[current_arr_index] == "#" and counting:
            pass
        elif arr[current_arr_index] != "#" and not counting:
            pass
        elif arr[current_arr_index] == "#":
            start_index = current_arr_index
            counting = True
        else:
            if current_arr_index - start_index != nums[current_nums_index]:
                return False
            counting = False
            start_index = current_arr_index
            current_nums_index += 1
        current_arr_index += 1

    if counting:
        if current_arr_index - start_index != nums[current_nums_index]:
            return False
        current_nums_index += 1
    if current_arr_index != len(arr):
        for i in arr[current_arr_index:]:
            if i != ".":
                return False
    elif current_nums_index != len(nums):
        return False
    return True


def count_up(arr: [str]):
    for i in range(len(arr)):
        if arr[i] == ".":
            arr[i] = "#"
            break
        else:
            arr[i] = "."


file = open("sample_text.txt", "r")
sum_of_values = 0
line_counter = 1
for line in file:
    print(f"Line Number: {line_counter}")
    line_counter += 1

    temp_count = 0

    original_nums = helper.extract_all_ints(line)
    nums = []
    for i in range(5):
        for num in original_nums:
            nums.append(num)

    original_char_array = [char for char in line if char in ["#", "?", "."]]
    char_array = []
    for i in range(5):
        for char in original_char_array:
            char_array.append(char)
        if i != 4:
            char_array.append("?")

    char_array_copy_with_delimiter = char_array.copy()
    char_array_copy_with_delimiter.append("\n")

    # find the ranges of all question mark values
    unconfirmed_ranges = []
    start_value = 0
    counting = line[0] == "?"
    for i in range(len(char_array_copy_with_delimiter)):
        char = char_array_copy_with_delimiter[i]
        if char == "?" and counting:
            continue
        elif char == "?":
            start_value = i
            counting = True
        elif counting:
            unconfirmed_ranges.append(range(start_value, i))
            counting = False

    unconfirmed = []
    for unconfirmed_range in unconfirmed_ranges:
        for i in unconfirmed_range:
            unconfirmed.append(i)

    insert_array = ["." for i in unconfirmed]
    current_index = 0
    for i in unconfirmed:
        char_array[i] = insert_array[current_index]
        current_index += 1

    if validate_list(char_array, nums):
        temp_count += 1

    count_up(insert_array)

    while not helper.is_all_equal_to(insert_array, "."):
        current_index = 0
        for i in unconfirmed:
            char_array[i] = insert_array[current_index]
            current_index += 1
        if validate_list(char_array, nums):
            temp_count += 1
        count_up(insert_array)

    print(f"This line's count: {temp_count}")
    sum_of_values += temp_count

print(sum_of_values)

file.close()
