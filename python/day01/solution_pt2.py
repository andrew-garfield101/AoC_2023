import re

"""
Approach:
- Modify calibration func to double each line to handle single digit lines 
- Use regex and digits_dict to match spelled out digits  
- Sum all returned line values
"""


def create_digits_dict():
    # Create a dictionary for numeric and spelled-out digits
    digits_dict = {"zero": "0", "one": "1", "two": "2", "three": "3",
                   "four": "4", "five": "5", "six": "6", "seven": "7",
                   "eight": "8", "nine": "9"}
    # Add numeric digits as keys pointing to themselves
    for digit in "0123456789":
        digits_dict[digit] = digit
    return digits_dict


def get_calibration_value(line, digits_dict):
    # Double the line to handle single-digit cases
    line = 2 * line

    # Create a regex pattern to match all spelled-out digits and numeric digits
    digit_pattern = re.compile(rf"(?=({'|'.join(digits_dict)}))")
    matches = digit_pattern.findall(line)

    # Directly use the first and last matches as there will always be at least two
    first_digit, last_digit = digits_dict[matches[0]], digits_dict[matches[-1]]
    return int(first_digit + last_digit)


def main():
    digits_dict = create_digits_dict()
    total = 0
    with open('input.txt', 'r') as file:
        for line in file:
            line = line.strip()
            calibration_value = get_calibration_value(line, digits_dict)
            print(f"Line: {line} -> Calibration Value: {calibration_value}")
            total += calibration_value

    print("Total calibration value:", total)


if __name__ == "__main__":
    main()
