import argparse
import os
import shutil
def copy_images(input_folder, output_folder, input_file):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with open(input_file, 'r') as file:
        for line in file:
            # Split the line into columns
            writer_image, word = line.split()
            image_name = writer_image.split(',')[1] + '.png'

            # Construct the source and destination paths
            source_path = os.path.join(input_folder, image_name)
            destination_path = os.path.join(output_folder, image_name)

            # Copy the image to the new folder
            shutil.copy(source_path, destination_path)



    print(f"Finished copying images to {output_folder}.")

def main():
    parser = argparse.ArgumentParser(description="Copy images based on score threshold.")
    parser.add_argument("--input_folder", help="Path to the input folder containing images.")
    parser.add_argument("--output_folder", help="Path to the output folder for copied images.")
    parser.add_argument("--input_file", help="Path to the input file containing image details.")

    args = parser.parse_args()
    copy_images(args.input_folder, args.output_folder, args.input_file)

if __name__ == "__main__":
    main()

