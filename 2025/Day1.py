# Part 1
def part1():
    # Reads the txt file
    with open("2025/2025Day1Part1.txt") as file:
        lines = file.read()

    # Splits the lines in the txt file
    splittedLines = lines.split("\n")

    total_sum = 50 # The dial starts at 50
    number_of_zeroes = 0 # Counts the number of times the dial is at 0

    # Iterates through all the lines
    for i in splittedLines:

        direction = i[0] # Turn left or right
        turn = int(i[1:]) # Amount of turns
        
        if direction == "R": # If the direction is right
            total_sum += turn # Adds the amount of turns

        elif direction == "L": # If the direction is left
            total_sum -= turn # Subtracts the amount of turns

        total_sum %= 100 # Modulo 100 to wrap around the dial 0-99

        if total_sum == 0: # If the dial is at 0 then add 1 to the number of zeroes
            number_of_zeroes += 1 # Adds 1 to the number of zeroes
    
    return number_of_zeroes # Returns the final number of zeroes

# Part 2
def part2():
    # Reads the txt file
    with open("2025/2025Day1Part2.txt") as file:
        lines = file.read()

    # Splits the lines in the txt file
    splittedLines = lines.split("\n") 

    total_sum = 50 # The dial starts at 50
    number_of_zeroes = 0 # Counts the number of times the dial is at 0

    # Iterates through all the lines
    for i in splittedLines:

        direction = i[0] # Turn left or right
        turn = int(i[1:]) # Amount of turns
        
        if direction == "R": # If the direction is right
            for i in range(turn): # Iterates through the amount of turns
                total_sum = (total_sum + 1) % 100 # Adds the amount of turns
                if total_sum == 0: # If the dial is at 0 then add 1 to the number of zeroes
                    number_of_zeroes += 1 # Adds 1 to the number of zeroes

        elif direction == "L": # If the direction is left
            for i in range(turn): # Iterates through the amount of turns
                total_sum = (total_sum - 1) % 100 # Subtracts the amount of turns
                if total_sum == 0: # If the dial is at 0 then add 1 to the number of zeroes
                    number_of_zeroes += 1 # Adds 1 to the number of zeroes

        total_sum %= 100 # Modulo 100 to wrap around the dial 0-99
    
    return number_of_zeroes # Returns the final number of zeroes

print("Part 1:", part1())
print("Part 2:", part2())