# Brayden Jonsson, 2023

import helper


def search_for_mirrors(arr: [int]):
    current_index = 0
    smudge_found = False
    while current_index < len(arr) - 1:
        equal, smudge_found = smudge_equality(arr[current_index], arr[current_index+1])
        if equal:
            offset = 1
            valid_num = True
            while 0 <= current_index - offset and current_index + 1 + offset < len(arr):
                inner_equal, inner_smudge_found = smudge_equality(arr[current_index - offset],
                                                                  arr[current_index + 1 + offset])
                if inner_equal and not inner_smudge_found:
                    pass
                if not inner_equal or (smudge_found and inner_smudge_found):
                    valid_num = False
                    break
                if inner_smudge_found and not smudge_found:
                    smudge_found = True
                offset += 1
            if valid_num and smudge_found:
                return current_index + 1, smudge_found
        current_index += 1
    return 0, False


def smudge_equality(num1: int, num2: int):
    """First bool is true if they are equal, either traditionally or by the binary diff. The second bool is true if
    it was by the binary diff"""
    if num1 == num2:
        return True, False
    elif check_for_binary_difference(num1, num2):
        return True, True
    else:
        return False, False


def check_for_binary_difference(num1: int, num2: int):
    num1_string = bin(num1)[2:]
    num2_string = bin(num2)[2:]

    if len(num1_string) == len(num2_string):
        difference = -1
        for i in range(len(num1_string)):
            if num1_string[i] == num2_string[i]:
                continue
            elif difference == -1:
                difference = i
            else:
                return False
        return True
    if len(num1_string) < len(num2_string):
        # Enforce that the matching parts are the same and the non-matching parts only contain a single 1
        if (num1_string == num2_string[len(num2_string) - len(num1_string):]
                and num2_string[:len(num2_string) - len(num1_string)].strip("0") == "1"):
            return True
        else:
            return False
    if len(num1_string) > len(num2_string):
        # Enforce that the matching parts are the same and the non-matching parts only contain a single 1
        if (num2_string == num1_string[len(num1_string) - len(num2_string):]
                and num1_string[:len(num1_string) - len(num2_string)].strip("0") == "1"):
            return True
        else:
            return False

    return False


file = open("challenge_text.txt", "r")

row_matrix = []

sum_of_values = 0

for line in file:
    # I have to purposefully add a newline to the end of the file for this :/
    if line.strip() != "":
        row_matrix.append([])
        for char in line:
            if char != "\n":
                row_matrix[-1].append(char)
    else:
        column_matrix = helper.make_column_matrix(row_matrix)

        rows = [helper.arr_to_int(row, "#") for row in row_matrix]
        columns = [helper.arr_to_int(column, "#") for column in column_matrix]

        row_count, row_smudge = search_for_mirrors(rows)
        column_count, column_smudge = search_for_mirrors(columns) if not row_smudge else (0, False)

        sum_of_values += column_count + row_count * 100
        row_matrix.clear()


print(sum_of_values)

file.close()
