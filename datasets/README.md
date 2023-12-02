# Scripts for processing datasets

This folder contains scripts that process the datasets into a format suitable for the model. 

## IAM 

* Download the IAM dataset from [here](https://fki.tic.heia-fr.ch/databases/iam-handwriting-database) and place the word-level images into the `iam/words` directory.
* Run `python3 process_dataset.py` to create processed `IAM` directory with word-level images.

Run `python3 process_dataset.py --help` to see available command line arguments.

## Washington

* Download the Washington dataset from [here](https://fki.tic.heia-fr.ch/databases/washington-database) and unzip the washington-v1.0.zip file into the `datasets` directory.
* Run `python3 pre_process_washington_0.py` to reformat the ground truth file and remove the bad annotations.
* Run `python3 process_dataset.py` to create processed `Washington` directory with word-level images.


Run `python3 pre_process_washington_0.py --help` and `python3 process_dataset.py --help` to see available command line arguments.

## IMGUR5k

* Download the IMGUR5k dataset from [the official repository](https://github.com/facebookresearch/IMGUR5K-Handwriting-Dataset).
* Run `python3 pre_process_IMGUR5k_0.py` to segment the sentences into words using bounding box coordinates.
* Run `python3 pre_process_IMGUR5k_1.py` to select a subset of the dataset.


## Other dataset

* Download a dataset of your choice and place the word-level images into the `datasets` directory.
* Run `python3 process_dataset.py` to process the images into format for the model.

