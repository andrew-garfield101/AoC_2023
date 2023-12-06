# day one solution

"""
Approach:
- Downlaod input.txt file
    wget --header "Cookie: session=session_cookie" -O input.txt https://adventofcode.com/2023/day/1/input
- Process each line in file
    - Grabbing the first and last digit of given line to make 2 digit num
- Sum all returned line values
"""

def get_calibration_value(line):
    # get first digit
    first_digit = next(char for char in line if char.isdigit())

    # get last digit - reversed line for efficiency
    last_digit = next(char for char in reversed(line) if char.isdigit())

    # combine
    return int(first_digit + last_digit)

def main():
    total = 0
    with open('input.txt', 'r') as file:
        for line in file:
            total += get_calibration_value(line.strip())

    print("Total calibration value:", total)

if __name__ == "__main__":
    main()
