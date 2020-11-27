from os import listdir
from os.path import isfile, join
import os
from datetime import datetime

indir = "./data"
outdir = "./out"
model = "models-upconv_7_photo"
scaler = "waifu2x-ncnn-vulkan.exe"
denoise = "3"
scale = "2"

all_files = [f for f in listdir(indir) if isfile(join(indir, f))]

print("got " + str(len(all_files)) + "files")
print(all_files[0])

processed = 0

# Includes non-pngs, but meh
total = len(all_files)
done = False

for f in all_files:
    if done == True:
        break
        
    if not f.endswith(".png"):
        continue
        
    inf = indir + "/" + f
    outf = outdir + "/" + f
    if os.path.exists(outf) and os.path.isfile(outf):
        # Already done
        processed += 1
        continue
        
    start_t = datetime.now()

    try:
        #waifu2x-ncnn-vulkan.exe -i out000000001.png -o out.png -n 3 -s 2 -m models-upconv_7_photo
        cmd = scaler + " -i " + inf + " -o " + outf + " -n " + denoise + " -s " + scale + " -m " + model
        print("executing " + cmd)
        res = os.system(cmd)
        if res != 0:
            print("Failed executing: " + res)
            done = True
            continue
    except Exception as e:
        print("Exception processing: " + f + ", " + str(e))
        break
    
    processed += 1
    end_t = datetime.now()
    delta = end_t - start_t
    files_left = total - processed
    us_per_file = delta.microseconds
    time_left_min = round((us_per_file * files_left) / 1000.0 / 1000.0 / 60, 2)

    percent = round(processed / float(total) * 100, 2)
    print(str(percent) + "% done, ETA: " + str(time_left_min) + " minutes")
    
print("finished processing " + str(processed) + " frames")
