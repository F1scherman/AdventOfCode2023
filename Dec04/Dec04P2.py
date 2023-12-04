# Brayden Jonsson, 2023
import helper

file = open("challenge_text.txt", "r")
sumOfValues = 0

total_scorecard = []
original_scorecard = []

score_table = {}
id_table = {}

for line in file:
    total_scorecard.append(line)
    original_scorecard.append(line)

    id_and_numbers = line.split(":")
    card_id = helper.extract_int(id_and_numbers[0])
    numbers = id_and_numbers[1].split("|")
    winning_numbers = numbers[0].strip().split()
    my_numbers = numbers[1].strip().split()

    score = 0

    for number in my_numbers:
        if number in winning_numbers:
            score += 1

    score_table[line] = score
    id_table[line] = card_id

for card in total_scorecard:
    score = score_table[card]
    card_id = id_table[card]

    for i in range(score):
        total_scorecard.append(original_scorecard[i + card_id])

print(len(total_scorecard))

file.close()