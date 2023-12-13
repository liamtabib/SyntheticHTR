import numpy as np
import pandas as pd
import math
import shutil
import os

def create_folder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)


def create_metric(dataset, metric, threshold, metric_df):
    print(metric)
    #if metric == 'confidence':
    #    metric_path = f'thresholded_datasets/{dataset}/log_confidence_scores.txt'
    #    metric_df = pd.read_csv(metric_path, sep=" ", header=None, names=["imagename", "word", "confidence"]).sort_values(by=['confidence'], ascending=False)
    #elif metric == 'NMAE' and dataset != 'IAM_OOV':
    #    metric_path = f'thresholded_datasets/{dataset}/NMAE.txt'
    #    metric_df = pd.read_csv(metric_path, sep=" ", header=None, names=["imagename", "NMAE"]).sort_values(by=['NMAE'], ascending=True)

    if metric == 'confidence':
        metric_df = metric_df.sort_values(by=['confidence'], ascending=False)
    elif metric == 'NMAE' and dataset != 'IAM_OOV':
        metric_df = metric_df.sort_values(by=['NMAE'], ascending=True)

    string_threshold = str(threshold)
    metric_folder = f'thresholded_datasets/{dataset}/{string_threshold}/{metric}/'
    create_folder(metric_folder)

    synthetic_images_folder = f'thresholded_datasets/{dataset}/{string_threshold}/{metric}/synthetic_images/'
    create_folder(synthetic_images_folder)

    if dataset != 'IAM_OOV':
        real_images_folder = f'thresholded_datasets/{dataset}/{string_threshold}/{metric}/real_images/'
        create_folder(real_images_folder)

    number_of_images = math.ceil(len(metric_df)*(threshold/100))
    
    for image_name in metric_df['imagename'].head(number_of_images):

        original_synthetic_images_path = f'synthetic_datasets/{dataset}_full/images/'
        source_path = os.path.join(original_synthetic_images_path, image_name)
        destination_path = os.path.join(synthetic_images_folder, image_name)
        shutil.copy(source_path, destination_path)

        if dataset != 'IAM_OOV':
            original_real_images_path = f'datasets/{dataset}_subset_cleaned/'
            source_path = os.path.join(original_real_images_path, image_name)
            destination_path = os.path.join(real_images_folder, image_name)
            shutil.copy(source_path, destination_path)
    
    print(f'Copied {number_of_images} images to {synthetic_images_folder}')
    if dataset != 'IAM_OOV':
        print(f'Copied {number_of_images} images to {real_images_folder}')
    
    mean_confidence = metric_df[f'confidence'].head(number_of_images).mean()

    mean_confidence_file = open(f'thresholded_datasets/{dataset}/{string_threshold}/{metric}/mean_confidence.txt', 'w')
    mean_confidence_file.write(f'Mean confidence: {mean_confidence}\n')

    if dataset != 'IAM_OOV':
        mean_NMAE = metric_df[f'NMAE'].head(number_of_images).mean()

        mean_NMAE_file = open(f'thresholded_datasets/{dataset}/{string_threshold}/{metric}/mean_NMAE.txt', 'w')
        mean_NMAE_file.write(f'Mean NMAE: {mean_NMAE}\n')

    metric_df.head(number_of_images).to_csv(f'thresholded_datasets/{dataset}/{string_threshold}/{metric}/{metric}_top_{string_threshold}.txt', header=None, index=None, sep=' ', mode='w')


GW = 'GW'
IAM = 'IAM'
IMGUR5k = 'imgur5k'
IAM_OOV = 'IAM_OOV'
#datasets = [IAM, IMGUR5k, GW, IAM_OOV]
datasets = [IAM_OOV]
thresholds = [100, 90, 50]

for i, dataset in enumerate(datasets):
    print(f'Handling {dataset}')
    for threshold in thresholds:
        threshold_folder = f'thresholded_datasets/{dataset}/{str(round(threshold))}/'
        create_folder(threshold_folder)

        confidence_path = f'thresholded_datasets/{dataset}/log_confidence_scores.txt'
        metric_df = pd.read_csv(confidence_path, sep=" ", header=None, names=["imagename", "word", "confidence"])

        if dataset != 'IAM_OOV':
            NMAE_path = f'thresholded_datasets/{dataset}/NMAE.txt'
            NMAE_df = pd.read_csv(NMAE_path, sep=" ", header=None, names=["imagename", "NMAE"])
            metric_df = metric_df.merge(NMAE_df, on='imagename', how='left') 
        create_metric(dataset, 'confidence', threshold, metric_df)
        if dataset != 'IAM_OOV':
            create_metric(dataset, 'NMAE', threshold, metric_df)
        
        

        

print(f'Finished!')
