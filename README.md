# DiffusionHTR

Generate realistic handwritten text using diffusion models. This project creates synthetic handwriting that captures individual writing styles and can be used for data augmentation in handwritten text recognition systems.

Built on top of the [WordStylist](https://github.com/koninik/WordStylist) architecture, this implementation uses latent diffusion models to generate high-quality handwritten text images with controllable writer characteristics.

## What you can do with this

Want to create synthetic handwriting datasets? This tool lets you:
- Train diffusion models on existing handwriting datasets
- Generate new handwritten text with specific writer styles
- Create large-scale synthetic datasets for training HTR systems
- Experiment with different writing styles and text content

## Getting started

First, set up your environment:

```bash
python3 -m venv DiffusionHTR-env
source DiffusionHTR-env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Quick start

If you want to jump right in, we've prepared everything you need:

**Pre-trained models**: We have models trained on IAM, George Washington, and IMGUR5k datasets. You can download them [here](https://drive.google.com/drive/folders/1LTJUl3XNl-DlULXw1yDl9U5E7NnsOYAk?usp=sharing).

**Ready-to-use datasets**: Skip the training and use our pre-generated synthetic datasets:
- [IAM dataset](https://zenodo.org/records/10392946?token=eyJhbGciOiJIUzUxMiJ9.eyJpZCI6ImI4NWY3Njc1LWYxYWItNDQzMi1hNjM3LTFjZDE2NmI0YjA2NSIsImRhdGEiOnt9LCJyYW5kb20iOiI2M2Q3MzFhZjBhNGY0ZGE5ZWViZjRmOWRlNTM5NzZjNyJ9.V5z0a9qU-_BeG7wFOKVl5riMp04aYb1KPvr_6ntS9OdhTcFlQN3MD5KZNffD_G-03Vm8IVREPFhy1rOyAGW4ug)
- [George Washington dataset](https://zenodo.org/records/10392982?token=eyJhbGciOiJIUzUxMiJ9.eyJpZCI6IjQ1NTI0MjA3LWZjNDAtNDYxMS1hYjk2LTEyZGEyY2RjNjRlOCIsImRhdGEiOnt9LCJyYW5kb20iOiJjZjljNWEzMmZkYmZjMGNmZDZkYTdhZTI3YWVmZmRjNiJ9.XcbZXLbRWM8OdGpr0WZfui_C9Mykg_0ltOkcXvxBHd4B4DDP1dtkck7bUNrccA77DoiReL0NgZOZ-rSb7XBqHg)
- [IMGUR5k dataset](https://zenodo.org/records/10392963?token=eyJhbGciOiJIUzUxMiJ9.eyJpZCI6IjVmNDhmYzRlLWE3OGEtNDJiMS1iY2QxLWExMDI2NmIyOGU1YyIsImRhdGEiOnt9LCJyYW5kb20iOiIwOTY3YzBiYzI0OTRkOTk4NGI5OGE3MjkxNzcxNDYyMiJ9.wiFBP18s05t7m7uaX7hwKiBdENXRbh-h3svaBtiSxUB0Sw-IB4vNL23VbEUkGXjB8AWTMODipz9Vk8bBCx23aQ)
- [Out-of-vocabulary IAM dataset](https://zenodo.org/records/10393019?token=eyJhbGciOiJIUzUxMiJ9.eyJpZCI6IjViZGJjYmJkLTVlOWMtNGM0MS05MjkwLTQxNjNiODE2NDgzMCIsImRhdGEiOnt9LCJyYW5kb20iOiI0MmM1ZGIxYzg5OTlkM2E4ZTBjZjY2MDVlNjM5YzZhYSJ9.08cC8e_lmkWvCsQsEY_QtjlnpriOCKIp6qQIvDnrjP6ncR8kwx-p3XrUxUhiNXJ99HskbR-x8mHoQoGRVKUTvg)

## Training your own model

Want to train on your own handwriting dataset? Here's the typical workflow:

1. **Prepare your data**: Process your handwriting images into the right format
   ```bash
   python3 preprocessing/process_dataset.py --dataset_path /path/to/your/images --save_dir /path/to/processed
   ```

2. **Train the diffusion model**: This will take a while, but it's worth it
   ```bash
   python3 train_diffusion.py --dataset iam --iam_path /path/to/processed --epochs 1000
   ```

3. **Generate synthetic text**: Create new handwriting samples
   ```bash
   python3 inference.py --models_path /path/to/trained/models --single_image True
   ```

That's it! You'll have a trained model that can generate handwriting in the style of your training data.

## How it works

The system uses a diffusion model architecture specifically designed for handwritten text generation. It learns to capture both the content (what letters to write) and the style (how to write them) from training examples. During inference, you can control both aspects to generate exactly the kind of handwriting you need.

Check out the [official paper](DiffusionHTR.pdf) for all the technical details.

## References

[1]: Nikolaidou, K., Retsinas, G., Christlein, V., Seuret, M., Sfikas, G., Smith, E. B., Mokayed, H., & Liwicki, M. (2023). WordStylist: Styled Verbatim Handwritten Text Generation with Latent Diffusion Models. arXiv preprint arXiv:2303.16576. https://arxiv.org/abs/2303.16576
