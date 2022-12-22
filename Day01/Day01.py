from itertools import groupby

with open("input.txt") as f:
    split_input = f.read().splitlines()

# Group the list of numbers into sublists with the empty string being a delimiter
grouped_list = [list(group) for k, group in groupby(split_input, lambda z: z == "")]

# Convert each sublist into the sum of its items and then find the max value in the resultant list
list_of_sums = [
        sum(map(int, l)) for l in grouped_list if l != [""]
    ]
max_calories = max(list_of_sums)


### Part 2
top_three_summed = sum(sorted(list_of_sums, reverse=True)[0:3])