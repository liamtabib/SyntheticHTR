# SyntheticHTR

[You can find the official report here](SyntheticHTR.pdf)

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


## Our synthesized datasets

As part of our research, we have fully synthesized four datasets, and further refined these by keeping only the highest quality synthetic images. 

You can download our best synthesized datasets: IAM dataset from [here](https://zenodo.org/records/10392946?token=eyJhbGciOiJIUzUxMiJ9.eyJpZCI6ImI4NWY3Njc1LWYxYWItNDQzMi1hNjM3LTFjZDE2NmI0YjA2NSIsImRhdGEiOnt9LCJyYW5kb20iOiI2M2Q3MzFhZjBhNGY0ZGE5ZWViZjRmOWRlNTM5NzZjNyJ9.V5z0a9qU-_BeG7wFOKVl5riMp04aYb1KPvr_6ntS9OdhTcFlQN3MD5KZNffD_G-03Vm8IVREPFhy1rOyAGW4ug), George Washington dataset from [here](https://zenodo.org/records/10392982?token=eyJhbGciOiJIUzUxMiJ9.eyJpZCI6IjQ1NTI0MjA3LWZjNDAtNDYxMS1hYjk2LTEyZGEyY2RjNjRlOCIsImRhdGEiOnt9LCJyYW5kb20iOiJjZjljNWEzMmZkYmZjMGNmZDZkYTdhZTI3YWVmZmRjNiJ9.XcbZXLbRWM8OdGpr0WZfui_C9Mykg_0ltOkcXvxBHd4B4DDP1dtkck7bUNrccA77DoiReL0NgZOZ-rSb7XBqHg), IMGUR5k dataset from [here](https://zenodo.org/records/10392963?token=eyJhbGciOiJIUzUxMiJ9.eyJpZCI6IjVmNDhmYzRlLWE3OGEtNDJiMS1iY2QxLWExMDI2NmIyOGU1YyIsImRhdGEiOnt9LCJyYW5kb20iOiIwOTY3YzBiYzI0OTRkOTk4NGI5OGE3MjkxNzcxNDYyMiJ9.wiFBP18s05t7m7uaX7hwKiBdENXRbh-h3svaBtiSxUB0Sw-IB4vNL23VbEUkGXjB8AWTMODipz9Vk8bBCx23aQ) and our Out-Of-Vocabulary IAM dataset from [here](https://zenodo.org/records/10393019?token=eyJhbGciOiJIUzUxMiJ9.eyJpZCI6IjViZGJjYmJkLTVlOWMtNGM0MS05MjkwLTQxNjNiODE2NDgzMCIsImRhdGEiOnt9LCJyYW5kb20iOiI0MmM1ZGIxYzg5OTlkM2E4ZTBjZjY2MDVlNjM5YzZhYSJ9.08cC8e_lmkWvCsQsEY_QtjlnpriOCKIp6qQIvDnrjP6ncR8kwx-p3XrUxUhiNXJ99HskbR-x8mHoQoGRVKUTvg)

## Use the model for sampling or fine-tuning on datasets
Download a dataset of your choice with the word-level images, then run `python3 datasets/process_dataset.py` to preprocess the data before `python3 model/train.py` to train the model on your dataset. Lastly, you may want to fully synthesize the dataset using `python3 sampling/full_sampling.py`.

## References

[1]: Nikolaidou, K., Retsinas, G., Christlein, V., Seuret, M., Sfikas, G., Smith, E. B., Mokayed, H., & Liwicki, M. (2023). WordStylist: Styled Verbatim Handwritten Text Generation with Latent Diffusion Models. arXiv preprint arXiv:2303.16576. https://arxiv.org/abs/2303.16576
