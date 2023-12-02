# SyntheticHTR

Synthetic image generation for HTR using PyTorch based on [WordStylist: Styled Verbatim Handwritten Text Generation with Latent Diffusion Models](https://github.com/koninik/WordStylist) [1]

## Dependencies

Create a new virtual environment and install all the necessary Python packages:

```
python3 -m venv SyntheticHTR-env
source SyntheticHTR-env/bin/activate
pip install --upgrade pip
python3 -m pip install -r SyntheticHTR/requirements.txt
```

## Content

* [Download our pre-trained models.](#our-pre-trained-models)
* [Download the synthetic datasets.](#synthetic-datasets)
* [Use the pre-trained models for sampling data or fine-tuning on additional datasets.](#use-the-models-for-fine-tuning-or-sampling)

## Our pre-trained models

Download our pre-trained models from [here](https://drive.google.com/drive/folders/1LTJUl3XNl-DlULXw1yDl9U5E7NnsOYAk?usp=sharing). There are 3 models in total, corresponding to the dataset that they have been trained on.


## Our generated datasets

Download our fully regenerated IAM dataset from [here](https://zenodo.org/records/10250221?token=eyJhbGciOiJIUzUxMiJ9.eyJpZCI6ImFlYzQ4ODAyLWQwMjAtNDA0My05OTNlLTJhODY3MjBlNWY2NCIsImRhdGEiOnt9LCJyYW5kb20iOiJlZTYzMzc3ZDY0YWJhZTg3MmI1MTU0NmYzZmE0MWM4NCJ9.YrVBEimPsagjgfaIFWB5O73o0YwYY3SKMbiXxXChvRshCDc1us3beXWFragqr0m-FFvE-fE3YSHGqTlDTAOohQ).

Download our fully regenerated GW dataset from [here](https://zenodo.org/records/10250452?token=eyJhbGciOiJIUzUxMiJ9.eyJpZCI6ImI5MmU2MzFiLWMwOGItNDY3NC1hNDQ2LWU4OGZkNjFhZjc4NyIsImRhdGEiOnt9LCJyYW5kb20iOiJhMmU3YTI0M2YxYWNhYjU3MTAzMDkyM2IzNWI3YjU1ZSJ9.Rbko8i4sFsTrLl0S5z9wuEbPWlB-ZdbDawt9OcWf0bnCnpn2-sAziVJn_x1D8Zd2kfX-if0bJ1-i2xGY8hMmZQ).

Download our regenerated IMGUR5k dataset from [here](https://zenodo.org/records/10250459?token=eyJhbGciOiJIUzUxMiJ9.eyJpZCI6IjE3MmFmY2RhLTk2NTYtNGI4My05ZDEyLTYwNGM1N2VkMmUxNCIsImRhdGEiOnt9LCJyYW5kb20iOiIzYzE1MWNhYjA4OWQ5ZWRlOTQ1YTQ5MDUwMjIwZDU5OSJ9.idRDNo2JlrzGUxaOhhSqcTz3zONzN_hUS737ZubbeHj0LbjcxFCO-N5OfiJYSoaA4OqqPXMSezPbimy4CiTWIg).

## Use the model for sampling or fine-tuning on datasets
Download a dataset of your choice with the word-level images, then run `python3 datasets/process_dataset.py` to preprocess the data before `python3 model/train.py` to train the model on your dataset. Lastly, you may want to regenerate the dataset using `python3 sampling/full_sampling.py`.

## References

[1]: Nikolaidou, K., Retsinas, G., Christlein, V., Seuret, M., Sfikas, G., Smith, E. B., Mokayed, H., & Liwicki, M. (2023). WordStylist: Styled Verbatim Handwritten Text Generation with Latent Diffusion Models. arXiv preprint arXiv:2303.16576. https://arxiv.org/abs/2303.16576
