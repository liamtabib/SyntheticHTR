import shutil


with open(f"datasets/imgur5k_gt/gt_150_words_per_image.txt", 'r') as f:
    file_content = f.readlines()

for line in file_content:
    # Split the line into image name and description
    parts = line.split('\t')

    # Check if the line has both parts (image name and description)
    if len(parts) == 2:
        file_name = parts[0]
            
        src_path = r"datasets/imgur5k_cleaned/" + file_name
        dst_path = r"datasets/imgur5k_subset_cleaned/" + file_name
        shutil.copy(src_path, dst_path)
