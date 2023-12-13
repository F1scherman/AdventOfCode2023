# Brayden Jonsson, 2023
import helper
from threading import Thread, Lock


def validate_list(arr: [str], nums: [int]):
    current_nums_index = 0
    current_arr_index = 0
    counting = arr[0] == "#"
    start_index = 0
    while current_arr_index < len(arr) and current_nums_index < len(nums):
        if arr[current_arr_index] == "#" and not counting:
            start_index = current_arr_index
            counting = True
        elif arr[current_arr_index] != "#" and counting:
            if current_arr_index - start_index != nums[current_nums_index]:
                return False
            counting = False
            start_index = current_arr_index
            current_nums_index += 1
        current_arr_index += 1

    if current_nums_index != len(nums):
        return False
    elif current_arr_index != len(arr):
        for i in range(current_arr_index, len(arr)):
            if arr[i] == "#":
                return False
    return True


def count_up(arr: [str]):
    for i in range(len(arr)):
        if arr[i] == ".":
            arr[i] = "#"
            break
        else:
            arr[i] = "."


def figure_out_permutations(nums: [int], char_array: [str], unconfirmed: [str]):
    global sum_lock, sum_of_values, thread_counter
    temp_count = 0

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

    with sum_lock:
        sum_of_values += temp_count
        print(f"Thread {thread_counter} concluded!")
        thread_counter += 1


file = open("sample_text.txt", "r")
sum_of_values = 0
sum_lock = Lock()
thread_counter = 1

threads = []
for line in file:
    nums = helper.extract_all_ints(line)
    nums = nums * 5

    original_char_array = [char for char in line if char in ["#", "?", "."]]

    char_array = []
    for i in range(5):
        for char in original_char_array:
            char_array.append(char)
        if i != 4:
            char_array.append("?")
        else:
            char_array.append("\n")

    char_array = [char_array[i] for i in range(len(char_array))
                  if char_array[i] != "." or (0 < i < len(char_array) - 1 and char_array[i - 1] != ".")]

    # find the ranges of all question mark values
    unconfirmed_ranges = []
    start_value = 0
    counting = line[0] == "?"
    for i in range(len(char_array)):
        char = char_array[i]
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

    thread = Thread(target=figure_out_permutations, args=(nums, char_array, unconfirmed))
    threads.append(thread)
    thread.start()


file.close()
for thread in threads:
    thread.join()

print(sum_of_values)

file.close()
