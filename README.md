### waifu2x batch scale

Goes through all files in a dir and applies the same waifu2x scaling in them.

You need waifu2x-ncnn-vulkan from https://github.com/nihui/waifu2x-ncnn-vulkan along with the models.

### Usage

Modify the code to have the right input and output directories, path to the scaler software, specify your used model, scaling ratio and denoising ratio, then run: `python3 scale.py`
