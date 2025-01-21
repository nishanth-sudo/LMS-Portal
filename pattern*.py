pattern
code:
def print_pattern(n):
    # Outer loop for each row
    for i in range(n):
        # Start by determining the starting character for the row
        if i % 2 == 0:
            # Even rows: starting from 'A' and going forward
            start_char = ord('A')
            end_char = start_char + (n - i)  # End point for characters
            row = [chr(start_char + j) for j in range(n - i)]
        else:
            # Odd rows: starting from the letter 'A' and going backward
            start_char = ord('A') + (n - i - 1)  # start from last letter
            end_char = ord('A')  # end at letter 'A'
            row = [chr(start_char - j) for j in range(n - i)]

        # Join the characters in the row with space and print
        print(" ".join(row))

# Take input from user
n = int(input())  # Enter the value of n
print_pattern(n)
