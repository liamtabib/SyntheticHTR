def process_file(input_file_path, output_file_path):
    with open(input_file_path, 'r') as file:
        lines = file.readlines()

    processed_lines = []
    for line in lines:
        parts = line.split(',')
        if len(parts) > 1:
            # Remove the part before the comma and add .png to the first string
            processed_line = f"{parts[1].split()[0]}.png " + " ".join(parts[1].split()[1:])
            processed_lines.append(processed_line)

    with open(output_file_path, 'w') as file:
        for line in processed_lines:
            file.write(line + '\n')

# Replace these file paths with the actual paths on your system
input_file_path = 'log_confidence_scores.txt'
output_file_path = 'log_confidence_scores_edited.txt'

# Call the function to process the file
process_file(input_file_path, output_file_path)
