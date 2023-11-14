# Scripts for processing datasets

This folder contains scripts that process the datasets into in a way required to do full sampling. 

## IAM 

* Download the IAM dataset from [here](https://fki.tic.heia-fr.ch/databases/iam-handwriting-database) and place the word-level images into the `iam/words` directory. 
* Run `python3 process_iam.py` to create IAM directory with images.