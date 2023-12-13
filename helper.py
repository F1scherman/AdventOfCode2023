def extract_int(string: str):
    """This extracts an integer from a string. Functionality breaks if multiple valid integers exist (it combines them all)"""
    return int(''.join(filter(lambda a: a.isdigit(), string)))


def extract_int_at_location(string: str, location:int):
    """This extract an integer located at a specific location in a string"""
    if not string[location].isdigit():
        raise Exception

    i = location - 1
    while i >= 0:
        if string[i].isdigit():
            i -= 1
        else:
            break
    left_coord = i + 1

    i = location + 1
    while i < len(string):
        if string[i].isdigit():
            i += 1
        else:
            break
    right_coord = i - 1

    return int(string[left_coord:right_coord + 1])


def extract_int_at_location_negatives(string: str, location:int):
    """This extract an integer located at a specific location in a string"""
    if (not string[location].isdigit()) and string[location] != "-":
        raise Exception

    i = location - 1
    while i >= 0:
        if string[i].isdigit() or string[i] == '-':
            i -= 1
        else:
            break
    left_coord = i + 1

    i = location + 1
    while i < len(string):
        if string[i].isdigit() or string[i] == "-":
            i += 1
        else:
            break
    right_coord = i - 1

    return int(string[left_coord:right_coord + 1])


def extract_all_ints(string: str):
    """This extracts all ints from a string and returns an ordered list"""
    returns = []
    i = 0
    while i < len(string):
        if string[i].isdigit():
            returns.append(extract_int_at_location(string, i))
            i += len(str(returns[-1]))
        else:
            i += 1
    return returns


def extract_all_ints_negatives(string: str):
    """This extracts all ints from a string and returns an ordered list with negative symbols"""
    returns = []
    i = 0
    while i < len(string):
        if string[i].isdigit() or string[i] == "-":
            returns.append(extract_int_at_location_negatives(string, i))
            i += len(str(returns[-1]))
        else:
            i += 1
    return returns

def find_all_occurrences(string: str, target: str):
    """This finds all occurrences of target in string, returns a list of the first indices of target"""
    return_list = []
    for index in range(len(string)):
        if string[index:].startswith(target):
            return_list.append(index)

    return return_list


def find_all_occurrences_no_overlap(string: str, target: str):
    """This finds all occurrences of target in string, returns a list of the first indices of target, but ignores the
    second target in the case of an overlap"""
    old_list = find_all_occurrences(string, target)
    new_list = [old_list[0]]
    for i in range(1, len(old_list)):
        if old_list[i] - old_list[i - 1] < len(target):
            continue
        new_list.append(old_list[i])

    return new_list


def is_all_equal(arr: list):
    standard_item = arr[0]
    for item in arr:
        if item != standard_item:
            return False
    return True


def is_all_equal_to(arr: list, standard):
    for item in arr:
        if item != standard:
            return False
    return True


def arr_to_int(arr: list, one_bit):
    """This reads an array as a binary number given the one bits. The first index is the low index. Anything not equal
    to one is assumed to be zero"""
    int = 0
    for i in range(len(arr)):
        if arr[i] == one_bit:
            int += 2**i

    return int


def make_column_matrix(matrix: [[]]):
    new_matrix = []
    for i in range(len(matrix[0])):
        new_matrix.append([y[i] for y in matrix])

    return new_matrix
