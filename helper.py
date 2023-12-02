def extract_int(string: str):
    """This extracts an integer from a string. Functionality breaks if multiple valid integers exist"""
    return int(''.join(filter(lambda a: a.isdigit(), string)))


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

