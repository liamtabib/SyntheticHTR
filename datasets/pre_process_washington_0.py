"""
Script to restructure the george washington ground truth file and remove bad annotations.
"""

import argparse
from pathlib import Path

def process_word(word):
    clean_dict = {"s_0": "0", "s_1": "1", "s_2": "2", "s_3": "3", "s_4": "4", "s_5": "5", "s_6": "6", "s_7": "7", "s_8": "8", "s_9": "9", "-": "", "s_pt" : "", "s_cm" : "", "s_mi" : "", "s_sq" : "", "s_qt": "","s_GW" : "", "s_qo": ""}

    parts = word.split()
    identifier = parts[0]

    content = parts[1]
    for s_number, number in clean_dict.items():
        content = content.replace("s_et-c-s_pt", "")
        content = content.replace("s_lb-s_1-s_0-s_0-s_0", "")
        content = content.replace(s_number, number)
        content = content.replace("s_", "")

    word = identifier + " " + content
    return word


def process_file(input_file, output_file, dataset_path):
    dataset_path = Path(dataset_path)

    with open(input_file, 'r') as file:
        words = file.readlines()

    processed_words = [process_word(word.strip()) for word in words]

    with open(output_file, 'w') as file:
        for clean_word in processed_words:
            parts = clean_word.split()
            if len(parts) > 1:
                file.write(clean_word + '\n')
            else:
                
                file_name = clean_word.strip() + '.png'
                file_path = dataset_path / file_name

                if file_path.exists():
                        file_path.unlink()
                        print(f"File {file_name} deleted due to unclear annotation")
                else:
                    print(f"File {file_name} already deleted.")



def main(args):
    process_file(args.path_gt, args.output_path_gt, args.path_to_dataset)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--path_gt', type=str, default='/path/to/gt.txt', help='Path to the original word-level ground truth file.')
    parser.add_argument('--output_path_gt', type=str, default='/path/to/save/new_gt.txt', help='Path where the new, processed ground truth file will be saved.')
    parser.add_argument('--path_to_dataset', type=str, default='/path/to/washington/dataset_dir', help='Path to the unprocessed George Washington dataset directory.')

        
    args = parser.parse_args()
    main(args)