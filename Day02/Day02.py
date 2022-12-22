with open("input.txt") as f:
    split_input = f.read().splitlines()

mapping_scores = {
    "A Y": 8,
    "A X": 4,
    "A Z": 3,
    "B Y": 5,
    "B X": 1,
    "B Z": 9,
    "C Y": 2,
    "C X": 7,
    "C Z": 6,
}

sum_of_scores = 0
for game_round in split_input:
    sum_of_scores += mapping_scores[game_round]


### Round 2
updated_mapping_scores = {
    "A Y": 4,
    "A X": 3,
    "A Z": 8,
    "B Y": 5,
    "B X": 1,
    "B Z": 9,
    "C Y": 6,
    "C X": 2,
    "C Z": 7,
}
sum_of_scores_round_two = 0
for game_round in split_input:
    sum_of_scores_round_two += updated_mapping_scores[game_round]
