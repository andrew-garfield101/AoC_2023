"""
Problem Breakdown:

Calculate total points based on matching winning numbers and numbers elf has
Each card value is determined by the number of matches - the point value doubles for each match after first

Approach:
- Parse input
- Calculate Points for each card
- Sum Points
"""

# extract only numeric parts of each line - skip non-numeric prefixes Card # :
# parse after each line colon
# takes line from input - parses into two sets
# further split lines at | and again into lists of nums
# map(int) converts nums from str to int
# set() converts lists of nums into set - for easy check between to sets - intersections

# calculate points
# intersection finds common eles from two sets - matching nums
# if matches - point value calc'd as 2 ** len(matches) - 1 , accounts for doubling of points
# for each subsequent match - ex 3 matches = 2^3 - 1 = 7
# else 0 points

# get total sum after parsing each card


def parse_card(line):
    parts = line.split(':')
    if len(parts) < 2:
        return set(), set()

    numbers_part = parts[1]
    winning_nums, player_nums = numbers_part.split('|')
    return set(map(int, winning_nums.split())), set(map(int, player_nums.split()))


def calculate_card_points(winning_nums, player_nums):
    matches = winning_nums.intersection(player_nums)
    if not matches:
        return 0
    points = 1
    for _ in range(1, len(matches)):
        points *= 2
    return points


def total_points(cards):
    return sum(calculate_card_points(*parse_card(card)) for card in cards)


def main():
    with open('input.txt') as file:
        cards = file.readlines()
    points = total_points(cards)
    print(f"The total points of the scratchcards is: {points}")


if __name__ == "__main__":
    main()



# part 2