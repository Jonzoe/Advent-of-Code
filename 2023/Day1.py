import re

# Part 1
def part1():
    # Reads the txt file
    with open("Day1Part1.txt") as file:
        lines = file.read()

    # Splits the lines in the txt file
    splittedLines = lines.split("\n")
    total_sum = 0

    # Iterates through all the lines
    for i in splittedLines:
        first_number = None
        second_number = None

        # Iterates through all the characters in every line
        for char in i:
            if char.isdigit(): # Checks if the character is a number
                if first_number is None: # If the first number isn't set then set it to the current one
                    first_number = char # Sets the first number
                second_number = char # Sets the latest number as the second number

        big_number = first_number + second_number # Puts the first and second number together as a new number

        total_sum += int(big_number) # Adds all the new numbers together

    return total_sum # Returns the final sum

def get_digit(d):
    if d.isnumeric():
        return d
    return str(digits.index(d))

digits = ('', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')

# Part 2
def part2():
    # Reads the txt file
    with open("Day1Part2.txt", 'r') as file:
        lines = file.read()
    
    regex = r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))'

    total = 0
    for line in lines.split("\n"):
        number = re.findall(regex, line)
        total += int(get_digit(number[0]) + get_digit(number[-1]))

    return total

print("Part 1:", part1())
print("Part 2:", part2())