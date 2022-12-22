import string

with open("input.txt") as f:
    split_input = f.read().splitlines()

# Zip toghether the characters and their corresponding prio into a dict
prio = [*range(1, 53, 1)]
prio_of_items = dict(zip(list(string.ascii_lowercase + string.ascii_uppercase), prio))

sum = 0
for rucksack in split_input:
    # split string into half
    x = len(rucksack)
    compartment1_set = set(rucksack[slice(0, x // 2)])
    compartment2_set = set(rucksack[slice(x // 2, x)])

    # Get the item found in bot lists and add to the sum
    common_item = (compartment1_set & compartment2_set).pop()
    sum += prio_of_items[common_item]


### Round two
