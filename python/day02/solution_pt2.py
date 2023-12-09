# day two solution pt2

"""
Problem Breakdown:
Determine Minimum Cubes: For each game, find the fewest number of red, green, and blue cubes required to make the game possible.
Calculate Power: The power of a set of cubes is the product of the numbers of red, green, and blue cubes.
Sum the Powers: Sum the powers of these minimum sets for all games.

Approach:
- Determine min num of cubes - for each game find fewest num of red green and blue cubes required
- Find the power of a given set of cubes - which is the product of the number of red, blue and green cubes
- Sum these powers
"""


def calculate_min_cubes_and_power(game_record):
    min_red, min_green, min_blue = 0, 0, 0
    subsets = game_record.split('; ')
    for subset in subsets:
        red, green, blue = 0, 0, 0
        counts = subset.split(', ')
        for count in counts:
            parts = count.split(' ')
            number = int(parts[0])
            color = parts[1]

            if 'red' in color:
                red = number
            elif 'green' in color:
                green = number
            elif 'blue' in color:
                blue = number

        min_red = max(min_red, red)
        min_green = max(min_green, green)
        min_blue = max(min_blue, blue)

    power = min_red * min_green * min_blue
    return power


def sum_of_powers(file_path):
    total_power = 0
    with open(file_path, 'r') as file:
        for line in file:
            game_id, record = line.strip().split(': ')
            total_power += calculate_min_cubes_and_power(record)
    return total_power


def main():
    file_path = 'input.txt'
    print(f"The sum of the power of the minimum sets is: {sum_of_powers(file_path)}")


if __name__ == "__main__":
    main()
