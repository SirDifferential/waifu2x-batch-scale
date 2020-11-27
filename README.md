### waifu2x batch scale

Goes through all files in a dir and applies the same waifu2x scaling in them.

You need waifu2x-ncnn-vulkan from https://github.com/nihui/waifu2x-ncnn-vulkan along with the models.

### Usage

Modify the code to have the right input and output directories, path to the scaler software, specify your used model, scaling ratio and denoising ratio, then run: `python3 scale.py`

### Useful things

* Disassemble a video into individual frames: `ffmpeg -i video.mp4 -r 29/1 out%09d.png`
	* `29/1` specifies FPS of 29 and every frame outputted
	 * `%09d` specifies filenames to have 9 digits in them. Increase if the video has over 999999999 frames.
* Extract audio from video: `ffmpeg -i video.mp4 -vn -acodec copy out.aac`
