"""
Part 2 Problem Breakdown:

Cards and matches generate copies of OG cards based on match count
Manage generation of new card copies based on match count and keep track of both

Approach:
- Initialize list with all og cards and contain its position and num of copies - initially 1
- Process each card
    - Calculate num of matches
    - If card has matches - add copies of subsequent cards to list
    - Num of copies added = num of matches
    - Copies should also have their position
- Keep track of total cards
- Repeat until no new cards are added
- Return total count

"""
# card queue list of dicts
# each dict corresponds to a scratchcard
# kp pairs : index: i , card: parse_card(card) , count: 1
# card queue becomes list where each element is a dict representing scratchcard along with
# index and its count


def parse_card(line):
    parts = line.split(':')
    if len(parts) < 2:
        return set(), set()

    numbers_part = parts[1]
    winning_nums, elf_nums = numbers_part.split('|')
    return set(map(int, winning_nums.split())), set(map(int, elf_nums.split()))


def calculate_matches(winning_nums, elf_nums):
    return len(winning_nums.intersection(elf_nums))


def process_scratchcards(cards):
    card_queue = [{'index': i, 'card': parse_card(card), 'count': 1} for i, card in enumerate(cards)]
    total_cards = 0

    for card_info in card_queue:
        matches = calculate_matches(*card_info['card'])
        total_cards += card_info['count']
        print(f"Processing Card {card_info['index'] + 1}, Matches: {matches}, Total Cards so far: {total_cards}")

        for i in range(1, matches + 1):
            next_card_index = card_info['index'] + i
            if next_card_index < len(cards):
                print(f"Adding copy of Card {next_card_index + 1}")
                card_queue.append({'index': next_card_index, 'card': parse_card(cards[next_card_index]), 'count': card_info['count']})

    return total_cards


def main():
    with open('input.txt') as file:
        cards = file.readlines()
    total_scratchcards = process_scratchcards(cards)
    print(f"Total scratchcards (including originals and copies): {total_scratchcards}")


if __name__ == "__main__":
    main()
