# Brayden Jonsson, 2023
import helper

file = open("challenge_text.txt", "r")
sum_of_values = 0

for line in file:
    sequences = [helper.extract_all_ints_negatives(line)]

    currentIndex = 0
    while not helper.is_all_equal(sequences[currentIndex]):
        old_sequence = sequences[currentIndex]
        new_sequence = []
        for i in range(len(old_sequence) - 1):
            new_sequence.append(old_sequence[i + 1] - old_sequence[i])

        sequences.append(new_sequence)
        currentIndex += 1

    for i in range(len(sequences) - 2, -1, -1):
        sequences[i].append(sequences[i+1][-1] + sequences[i][-1])

    sum_of_values += sequences[0][-1]

print(sum_of_values)

file.close()
