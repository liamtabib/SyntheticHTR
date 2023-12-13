import os
import shutil

# Define the file names and directories
output_file = 'combined.txt'
image_directory = 'images/'
subsets_directory = 'subsets/'

# Mapping of categories to folder names
category_to_folder = {
    'good': 'good',
    'average': 'average',
    'bad': 'bad'
}

# Read the combined file and process each line
with open(output_file, 'r') as file:
    for line in file:
        parts = line.strip().split('\t')
        image_name, cs_category, nmae_category = parts[0], parts[2], parts[3]

        # Convert categories to folder names
        cs_folder = category_to_folder.get(cs_category, None)
        nmae_folder = category_to_folder.get(nmae_category, None)

        if cs_folder and nmae_folder:
            # Build the source and destination paths
            source_path = os.path.join(image_directory, image_name)
            destination_path = os.path.join(subsets_directory, f"cs_{cs_folder}_NMAE_{nmae_folder}", image_name)

            # Check if the image file exists
            if os.path.exists(source_path):
                # Copy the file to the appropriate directory
                shutil.copy(source_path, destination_path)
            else:
                print(f"Image not found: {image_name}")

print("Images have been categorized and moved.")
