# Open the file in read mode
with open('log_confidence_scores.txt', 'r') as file:
    # Read all lines in the file
    lines = file.readlines()

# Count the number of lines
number_of_rows = len(lines)

print("Number of rows in the file:", number_of_rows)
