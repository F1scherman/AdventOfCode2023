# Brayden Jonsson, 2023

file = open("challenge_text.txt", "r")
sumOfValues = 0

for line in file:
    numbers = line.split(":")[1].split("|")
    winning_numbers = numbers[0].strip().split()
    my_numbers = numbers[1].strip().split()

    score = 0

    for number in my_numbers:
        if number in winning_numbers:
            if score == 0:
                score = 1
            else:
                score *= 2

    sumOfValues += score

print(sumOfValues)

file.close()
