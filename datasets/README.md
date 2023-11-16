# Scripts for processing datasets

This folder contains scripts that process the datasets into in a way required to do full sampling. 

## IAM 

* Download the IAM dataset from [here](https://fki.tic.heia-fr.ch/databases/iam-handwriting-database) and place the word-level images into the `iam/words` directory. 
* Run `python3 process_dataset.py --dataset_path words --save_dir IAM_cleaned` to create IAM directory with word-level images.

## Washington

* Download the Washington dataset from [here](https://fki.tic.heia-fr.ch/databases/washington-database) and unzip the washington-v1.0.zip file.
* Run `python3 process_dataset.py --dataset_path washingtondb-v1.0/data/word_images_normalized --save_dir washington_cleaned` to create Washington directory with word-level images.