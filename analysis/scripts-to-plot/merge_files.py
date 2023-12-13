# Define the file names
file1 = 'IAM_full.txt'
file2 = 'log_confidence_scores_edited.txt'
output_file = 'combined.txt'

# Function to categorize score for file1
def categorize_file1(score):
    score = float(score)
    if score < 0.02:
        return 'good'
    elif 0.02 <= score <= 0.15:
        return 'average'
    else:
        return 'bad'

# Function to categorize score for file2
def categorize_file2(score):
    score = float(score)
    if score > 0.99:
        return 'good'
    elif 0.8 < score <= 0.99:
        return 'average'
    else:
        return 'bad'

# Create dictionaries to store the data from each file
data1 = {}
data2 = {}

# Read the first file and store its contents in a dictionary
with open(file1, 'r') as f1:
    for line in f1:
        parts = line.strip().split(' ')
        identifier = parts[0]
        score = categorize_file1(parts[1])
        data1[identifier] = score

# Read the second file and store its contents in a dictionary
with open(file2, 'r') as f2:
    for line in f2:
        parts = line.strip().split(' ')
        identifier = parts[0]
        words_score = ' '.join(parts[1:-1])
        score = categorize_file2(parts[-1])
        data2[identifier] = f"{words_score}\t{score}"

# Write to the output file
with open(output_file, 'w') as out:
    for identifier in data1:
        if identifier in data2:
            # Combine the data from both files with tab separation
            combined_line = f"{identifier}\t{data2[identifier]}\t{data1[identifier]}\n"
            out.write(combined_line)

print("Output file created:", output_file)
