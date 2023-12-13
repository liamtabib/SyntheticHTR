import os
import numpy as np
from PIL import Image
import argparse

def read_images(clean_path, gen_path):
    """
    Reads images from specified clean and generated image directories.
    """
    clean_files = [f for f in os.listdir(clean_path) if f.endswith(".png") or f.endswith(".jpg")]
    clean_files.sort()

    gen_files = [f for f in os.listdir(gen_path) if f.endswith(".png") or f.endswith(".jpg")]
    gen_files.sort()

    clean_images = []
    gen_images = []

    for file_name in clean_files:
        im = Image.open(os.path.join(clean_path, file_name)).convert('L')  # Convert to grayscale
        clean_images.append((file_name, np.array(im)))

    for file_name in gen_files:
        im = Image.open(os.path.join(gen_path, file_name)).convert('L')  # Convert to grayscale
        gen_images.append((file_name, np.array(im)))

    return clean_images, gen_images

def calculate_average_pixel_difference(clean_images, gen_images):
    """
    Calculates the normalized average pixel-wise difference between pairs of images.
    The result is normalized to be in the range [0, 1].
    """
    differences = []
    max_diff = 255.0  # Maximum possible difference for 8-bit images
    for (clean_name, clean_img), (gen_name, gen_img) in zip(clean_images, gen_images):
        if clean_img.shape == gen_img.shape:
            clean_float = clean_img.astype("float")
            gen_float = gen_img.astype("float")

            # Calculate absolute difference and normalize
            diff = np.sum(np.abs(clean_float - gen_float)) / gen_float.size / max_diff
            differences.append((gen_name, diff))
            if clean_name != gen_name:
                print(f"Images with different names:{clean_name} and {gen_name} are compared.")
        else:
            print(f"Image {clean_name} and {gen_name} are of different shapes and cannot be compared.")
            differences.append((gen_name, None))

    return differences

def write_differences_to_file(differences, output_file):
    """
    Writes the differences to a specified output file.
    """
    with open(output_file, 'w') as file:
        for gen_name, diff in differences:
            if diff is not None:
                file.write(f"{gen_name} {diff}\n")
            else:
                file.write(f"{gen_name} N/A\n")


def main():
    parser = argparse.ArgumentParser(description="Calculate average pixel-wise differences between images.")
    parser.add_argument('clean_path', type=str, help="Path to the directory containing clean images")
    parser.add_argument('gen_path', type=str, help="Path to the directory containing generated images")
    parser.add_argument('output_file', type=str, help="Path to the output text file")

    args = parser.parse_args()

    clean_images, gen_images = read_images(args.clean_path, args.gen_path)
    print(f"Number of clean images: {len(clean_images)}")
    print(f"Number of generated images: {len(gen_images)}")
    average_differences = calculate_average_pixel_difference(clean_images, gen_images)
    valid_differences = [diff for _, diff in average_differences if diff is not None]
    if valid_differences:
        overall_average = sum(valid_differences) / len(valid_differences)
        print(f"Average of all differences: {overall_average}")
    else:
        print("No valid differences to calculate an overall average.")
    write_differences_to_file(average_differences, args.output_file)

    print(f"Differences written to {args.output_file}")

if __name__ == "__main__":
    main()
