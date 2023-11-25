import argparse
import numpy as np
import cv2
import json
import ast  # To convert a string representation of a list into a list.
from pathlib import Path  # To create folders safely.
import time
import PIL
from PIL import Image, ImageOps
import os


def parse_args():
    parser = argparse.ArgumentParser(description="Argument parser")

    parser.add_argument(
        "--path_to_repo",
        default="datasets/IMGUR5K-Handwriting-Dataset/",
        required=False,
        help="Path to a cloned Imgur5K GitHub repo.")

    parser.add_argument(
        "--out",
        default="datasets/imgur5k",
        required=False,
        help="Prefix of the directory to contain output.")

    parser.add_argument(
        "--idx_from",
        type=int,
        default=0,
        required=False,
        help="Index of an image to process from. Default: 0 (start from the first image).")

    parser.add_argument(
        "--idx_to",
        type=int,
        default=None,
        required=False,
        help="Index of an image to process to. Default: None (process all images).")

    parser.add_argument(
        "--display",
        action='store_true',
        help="Display each processed image. Default: False.")

    parser.add_argument(
        "--verbose",
        type=int,
        default=0,
        required=False,
        help="Print debug info. 0 - important messages only, 1 - more details, 2 - even more details. Default: 0.")

    parser.add_argument(
        "--keep_missing",
        action='store_true',
        help="Export images with missing annotations.")

    args = parser.parse_args()

    if args.verbose >= 1:
        print(f"Parsed arguments: {args}")

    return args

def resize_pad_cv2(image, target_width=256, target_height=64):

    # Get the original width and height
    img_height, img_width = image.shape[:2]

    # Resize image to height 64, keeping the aspect ratio
    new_width = int(img_width * target_height / img_height)
    resized_image = cv2.resize(image, (new_width, target_height), interpolation=cv2.INTER_LANCZOS4)

    # Pad image if the width is less than the target width
    if new_width > target_width:
        resized_image = cv2.resize(resized_image, (target_width, target_height), interpolation=cv2.INTER_LANCZOS4)
    else:
        # Calculate the padding size
        pad_width = target_width - new_width
        left_pad = pad_width // 2
        right_pad = pad_width - left_pad

        # Pad the image with white color
        resized_image = cv2.copyMakeBorder(resized_image, 0, 0, left_pad, right_pad, cv2.BORDER_CONSTANT, value=[255, 255, 255])

    return resized_image


def create_output_paths(args):
    """Create output directories if do not exist."""
    Path(f"{args.out}_gt/").mkdir(parents=True, exist_ok=True)
    Path(args.path_out).mkdir(parents=True, exist_ok=True)


def change_args(args, n_img):
    """Change args where necessary."""

    # Process *all* images if a user did not specify otherwise.
    if args.idx_to is None:
        args.idx_to = n_img

    return args


def rotate_crop_image(args, img, sub_box):
    """Rotates and crop an image, returns a cropped image."""

    # Elements of the bounding box.
    xc, yc, w, h, a = ast.literal_eval(sub_box)
    # (xc, ys) is the center of the rotated box, and the angle a is in degrees ccw.

    # Get the rotation matrix.
    rotate_matrix = cv2.getRotationMatrix2D(center=(xc, yc), angle=-a, scale=1)

    # Rotate the original image.
    rotated_img = cv2.warpAffine(src=img, M=rotate_matrix, dsize=(img.shape[1], img.shape[0]))

    # Crop the rotated image.
    crop_img = rotated_img[max(0, int(yc - h / 2)):int(yc + h / 2), max(0, int(xc - w / 2)):int(xc + w / 2)]

    if args.display:
        # Display images.
        cv2.imshow('Original', resize(img, 512))
        cv2.imshow('Rotated', resize(rotated_img, 512))
        cv2.imshow("Cropped", resize(crop_img, 64))

        # Press any key to continue.
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return crop_img


def write_gts(args, gts):
    """Write a gt.txt from a dictionary gt as instructed here:
        https://github.com/clovaai/deep-text-recognition-benchmark#when-you-need-to-train-on-your-own-dataset-or-non-latin-language-datasets"""

    with open(args.path_to_gt, "wt", encoding="utf-8") as f:
        for k, v in gts.items():
            imagepath = k
            label = v
            f.write(f"{imagepath}\t{label}\n")

    if args.verbose >= 1:
        print(f"{args.path_to_gt} contains {len(gts.items())} sub-images.")


def get_image_annotations(args):
    """Import JSON with bounding boxes and annotations."""
    with open(args.path_to_annotations) as json_file:
        data = json.load(json_file)
    return data


def process_data(args, data):
    """Export word-level images and corresponding gt annotations."""

    gts = {}

    # Create a list of images to process.
    img_to_process = list(data["index_id"].keys())[args.idx_from:args.idx_to]
    print(f"Started processing {len(img_to_process)} images (of possible {len(data['index_id'])}).")

    for img_name in img_to_process:
        img_path = data["index_id"][img_name]["image_path"]
        sub_images_lst = data["index_to_ann_map"][img_name]

        if args.verbose >= 1:
            print(
                f"Processing {args.path_to_repo + img_path}. Contains {len(sub_images_lst)} sub-image(s).")

        if args.verbose >= 2:
            print(f"Sub-images for image {img_name}: {sub_images_lst}")
            print(f"Sub-image data for {img_name}:")

        # Read image.
        img = cv2.imread(args.path_to_repo + img_path)

        # Check if the image file exists.
        if img is None:
            print(f"* {args.path_to_repo + img_path} does not exist.")
            continue

        for sub_image in sub_images_lst:

            # Ground truth label.
            sub_word = data["ann_id"][sub_image]["word"]

            if sub_word == "." and not args.keep_missing:
                # Skip words with missing annotations.
                continue
            
            if not (sub_word.isalpha() and sub_word.isascii() and len(sub_word) >= 2 and len(sub_word) <= 10):
                # Skip words that is not in latin alphabet and 2-10 characters long.
                continue

            # Bounding box.
            sub_box = data["ann_id"][sub_image]["bounding_box"]

            # DO THE WORK (ROTATE & CROP) WITH IMAGES HERE.    
            crop_img = rotate_crop_image(args, img, sub_box)

            # Resize.    
            crop_img = resize_pad_cv2(crop_img)

            # Create a filename for the cropped image.
            ext = img_path.split(".")[-1]
            out_filename = sub_image + "." + ext

            # Export a cropped image.
            cv2.imwrite(args.path_out + out_filename, crop_img)

            # Save gt info: filepath & label.
            gts[out_filename] = sub_word

            if args.verbose >= 2:
                print(f"Sub-image: {sub_image}, label: {sub_word}, box: {sub_box}")

        if args.verbose >= 2:
            print()

        if (img_to_process.index(img_name) + 1) % 200 == 0:
            print(f"Update: processed {img_to_process.index(img_name) + 1} images.")

    return gts


def main():
    # Parse arguments.
    args = parse_args()

    args.path_to_annotations = args.path_to_repo + "dataset_info/imgur5k_annotations.json"
    # Structure:
    # "index_id": get "image_path" here.
    # "index_to_ann_map": get a list of all sub-images.
    # "ann_id": get annotations and bounding-boxes for each sub-image.
    args.path_out = f"{args.out}_cleaned/"
    args.path_to_gt = f"{args.out}_gt/gt.txt"

    # Get image annotations.
    data = get_image_annotations(args)

    # Change args where necessary.
    args = change_args(args, n_img=len(data["index_id"]))

    # Create output directories with image indices in the folder names.
    create_output_paths(args)

    # Loop over all images and produce a gt dict.
    gts = process_data(args, data)
    print("Finished image processing.")

    # Write gt.txt files.
    write_gts(args, gts)
    print(f"gt.txt exported to {args.path_to_gt}.")


if __name__ == '__main__':
    tic = time.time()
    main()
    toc = time.time()
    print(f"Elapsed: {(toc - tic) / 60:.2f} min.")
