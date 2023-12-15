# Brayden Jonsson, 2023

import helper

file = open("sample_text.txt", "r")
sum_of_values = 0

inputs = file.readline().split(",")

for string in inputs:
    string_hash = 0
    for char in string:
        if char == "\n":
            continue
        string_hash += ord(char)
        string_hash *= 17
        string_hash %= 256

    sum_of_values += string_hash
print(sum_of_values)

file.close()
