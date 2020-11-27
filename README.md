### waifu2x batch scale

Goes through all files in a dir and applies the same waifu2x scaling in them.

You need waifu2x-ncnn-vulkan from https://github.com/nihui/waifu2x-ncnn-vulkan along with the models.

### Usage

Modify the code to have the right input and output directories, path to the scaler software, specify your used model, scaling ratio and denoising ratio, then run: `python3 scale.py`

You can use ^C to stop processing. If you then re-execute the program, it will continue from where it left off.

### Useful things

* Extract audio from video: `ffmpeg -i video.mp4 -vn -acodec copy out.aac`
* Disassemble a video into individual frames: `ffmpeg -i video.mp4 -r 29/1 out%09d.png`
	* `29/1` specifies FPS of 29 and every frame outputted
	 * `%09d` specifies filenames to have 9 digits in them. Increase if the video has over 999999999 frames.
* Create video from the frames: `ffmpeg -r 29 -f image2 -s 1920x1080 -i out%09d.png -vcodec libx264 -crf 25 -pix_fmt yuv420p out.mp4`
* Add audio to video file: `ffmpeg -i out.mp4 -i out.aac -c copy -map 0:v:0 -map 1:a:0 out_w_sound.mp4`
