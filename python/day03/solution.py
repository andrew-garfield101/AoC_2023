"""
Problem Breakdown:

Input is a grid with numbers and symbols
Identify the "part numbers" - any number adjacent to a symbol - including diagonals
Calculate the sum of all part numbers

Approach 1:
Parse the grid into a structure that allows easy access to each element and neighbors (2d list)
Check adjacency - for each number in the grid - check if its adjacent to a symbol
If a num is adjacent - add it to the sum

Using a 2D grid is efficient to access each element - this structure is good for grid-based problems
Scalability - this is a solid approach for larger inputs as well

Updated Approach:
- Create a dict for all symbols - keys are rows and column cells for each non-digit / . character
- Identify numbers and their edges - for each num found in regex - calculate an edge set that includes a num's position
- Map Nums to adjacent symbols
- Calculate the sum
- Pt2. Calculate product for each symbol position
"""


import math as m
import re

board = list(open('input.txt'))
chars = {(r, c): [] for r in range(140) for c in range(140) if board[r][c] not in '01234566789.'}

for r, row in enumerate(board):
    for n in re.finditer(r'\d+', row):
        edge = {(r, c) for r in (r-1, r, r+1) for c in range(n.start()-1, n.end()+1)}

        for o in edge & chars.keys():
            chars[o].append(int(n.group()))

# Solution for part 1 & 2
print(sum(sum(p) for p in chars.values()),
      sum(m.prod(p) for p in chars.values() if len(p) == 2))


# First Attempt:
# def is_adjacent_to_symbol(grid, x, y, symbols):
#     for dx in range(-1, 2):
#         for dy in range(-1, 2):
#             if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]):
#                 if grid[x + dx][y + dy] in symbols:
#                     return True
#     return False
#
#
# def sum_part_numbers(grid):
#     symbols = set("*#$+")  # Define the symbols
#     total_sum = 0
#     for x in range(len(grid)):
#         for y in range(len(grid[x])):
#             if grid[x][y].isdigit() and is_adjacent_to_symbol(grid, x, y, symbols):
#                 print(f"Adding {grid[x][y]} at ({x}, {y})")  # Debug print
#                 total_sum += int(grid[x][y])
#     return total_sum
#
#
# def main():
#     with open('input.txt') as file:
#         grid = [list(line.strip()) for line in file]
#
#     # Debugging print to verify grid structure
#     for row in grid:
#         print(''.join(row))
#
#     print("The sum of all the part numbers is:", sum_part_numbers(grid))
#
# if __name__ == "__main__":
#     main()
#
