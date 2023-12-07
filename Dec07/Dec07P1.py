# Brayden Jonsson, 2023
import helper
from functools import cmp_to_key

ALL_VALUES = ["A", "K", "Q", "J", "T"]
for i in range(9, 1, -1):
    ALL_VALUES.append(str(i))

MAP_VALUE_TO_NUM = {}
for i in range(14, 0, -1):
    MAP_VALUE_TO_NUM[ALL_VALUES[13-i]] = i

def hand_comparator(hand1_tup:(str, str), hand2_tup:(str, str)):
    hand1 = hand1_tup[0]
    hand2 = hand2_tup[0]
    highest_match_count_hand1 = 0
    second_highest_match_count_hand1 = 0

    for card in ALL_VALUES:
        temp = hand1.count(card)
        if temp >= highest_match_count_hand1:
            second_highest_match_count_hand1 = highest_match_count_hand1
            highest_match_count_hand1 = temp

    if second_highest_match_count_hand1 == 0:
        for card in ALL_VALUES:
            temp = hand1.count(card)
            if temp != highest_match_count_hand1 and temp > second_highest_match_count_hand1:
                second_highest_match_count_hand1 = temp

    highest_match_count_hand2 = 0
    second_highest_match_count_hand2 = 0

    for card in ALL_VALUES:
        temp = hand2.count(card)
        if temp >= highest_match_count_hand2:
            second_highest_match_count_hand2 = highest_match_count_hand2
            highest_match_count_hand2 = temp

    if second_highest_match_count_hand2 == 0:
        for card in ALL_VALUES:
            temp = hand2.count(card)
            if temp != highest_match_count_hand2 and temp > second_highest_match_count_hand2:
                second_highest_match_count_hand2 = temp

    if highest_match_count_hand1 > highest_match_count_hand2:
        return -1
    elif highest_match_count_hand1 < highest_match_count_hand2:
        return 1
    elif second_highest_match_count_hand1 > second_highest_match_count_hand2:
        return -1
    elif second_highest_match_count_hand1 < second_highest_match_count_hand2:
        return 1
    else:
        for index in range(len(hand1)):
            if MAP_VALUE_TO_NUM[hand1[index]] > MAP_VALUE_TO_NUM[hand2[index]]:
                return -1
            elif MAP_VALUE_TO_NUM[hand1[index]] < MAP_VALUE_TO_NUM[hand2[index]]:
                return 1
        return 0


file = open("challenge_text.txt", "r")
sum_of_values = 0
hands_and_bids = []
for line in file:
    line_split = line.split()
    hands_and_bids.append( (line_split[0], line_split[1]) )

hands_and_bids.sort(key=cmp_to_key(hand_comparator))
num_of_hands = len(hands_and_bids)
for i in range(num_of_hands):
    sum_of_values += (num_of_hands - i) * int(hands_and_bids[i][1])

print(sum_of_values)


file.close()
