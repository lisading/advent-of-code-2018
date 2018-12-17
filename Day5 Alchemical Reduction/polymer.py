from string import ascii_lowercase
import sys


def reacting_polymer(polymer):
    fully_reacted = False
    remaining = polymer
    while not fully_reacted:
        reacting_polymer = ""
        former_unit = ''
        reacted = False
        for unit in remaining:
            reacting_polymer = reacting_polymer + unit
            if (former_unit.isupper() and unit.islower() and former_unit.lower() == unit) \
                    or (former_unit.islower() and unit.isupper() and former_unit == unit.lower()):
                reacting_polymer = reacting_polymer[:-2]
                reacted = True
                former_unit = ''
            else:
                former_unit = unit
        if not reacted:
            fully_reacted = True
        remaining = reacting_polymer

    return remaining.strip()


def shortest_polymer(polymer):
    shortest_polymer = ""
    length = sys.maxsize
    for c in ascii_lowercase:
        cur_polymer = polymer.replace(c, "").replace(c.upper(), "")
        remaining_polymer = reacting_polymer(cur_polymer)
        cur_length = len(remaining_polymer)
        if cur_length < length:
            length = cur_length
            shortest_polymer = remaining_polymer

    return shortest_polymer, length


if __name__ == '__main__':

    # polymer = "dabAcCaCBAcCcaDA"
    polymer = ""
    with open("input.txt") as file:
        for line in file:
            polymer = line

    remaining = reacting_polymer(polymer)
    print(remaining)
    print(len(remaining))

    shortest_polymer, length = shortest_polymer(polymer)
    print(shortest_polymer)
    print(length)
