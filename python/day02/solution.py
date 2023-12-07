# day two solution

"""
Problem Breakdown:
Game Records: Each game's record shows several subsets of cubes that were revealed from the bag.
Task: Determine which games could occur if the bag contained only 12 red, 13 green, and 14 blue cubes.
Identify Impossible Games: A game is impossible if, at any point, the number of cubes shown exceeds the number available in the bag.
Calculate Sum of IDs: For the games that are possible, sum their IDs.

Approach:
- Parse each game record - extract ID and counts of each color cube shown in subset
- Check Feasibility - for each game - check if any subset exceeds Task's counts
- Sum IDs of Possible Games - if game is possible - add ID to total sum
"""

# func to parse game records to check each game's feasibility
def is_game_possible(game_record, max_red, max_green, max_blue):
    subsets = game_record.split('; ')
    for subset in subsets:
        red, green, blue = 0, 0, 0
        counts = subset.split(', ')
        for count in counts:
            parts = count.split(' ')
            number = int(parts[0])
            color = parts[1]

            if 'red' in color:
                red += number
            elif 'green' in color:
                green += number
            elif 'blue' in color:
                blue += number

        if red > max_red or green > max_green or blue > max_blue:
            return False
    return True

# func to sum possible game ids
def sum_possible_game_ids(file_path):
    total_sum = 0
    with open(file_path, 'r') as file:
        for line in file:
            game_id, record = line.strip().split(': ')
            if is_game_possible(record, 12, 13, 14):
                total_sum += int(game_id.split(' ')[1])
    return total_sum

def main():
    file_path = 'input.txt'  # Path to your input file
    total_sum = sum_possible_game_ids(file_path)
    print(f"The sum of the IDs of the possible games is: {total_sum}")

if __name__ == "__main__":
    main()