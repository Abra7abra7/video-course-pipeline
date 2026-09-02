import subprocess
import os
import shutil

exports_dir = 'exports'
os.makedirs(exports_dir, exist_ok=True)

src_vert = 'apodex-goldie-video/apodex-goldie-vertical.mp4'

# 1. 9:16
out_9x16 = os.path.join(exports_dir, 'apodex_goldie_9x16.mp4')
shutil.copyfile(src_vert, out_9x16)

# 2. 16:9
out_16x9 = os.path.join(exports_dir, 'apodex_goldie_16x9.mp4')
cmd_16x9 = [
    'ffmpeg', '-y',
    '-i', src_vert,
    '-filter_complex',
    '[0:v]split=2[bg][fg];'
    '[bg]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,gblur=sigma=35,eq=brightness=-0.35[blurred];'
    '[fg]scale=-1:1000[main];'
    '[blurred][main]overlay=(W-w)/2:(H-h)/2[v]',
    '-map', '[v]',
    '-map', '0:a',
    '-c:v', 'libx264',
    '-preset', 'fast',
    '-crf', '18',
    '-c:a', 'aac',
    out_16x9
]
subprocess.run(cmd_16x9, capture_output=True)

# 3. 1:1
out_1x1 = os.path.join(exports_dir, 'apodex_goldie_1x1.mp4')
cmd_1x1 = [
    'ffmpeg', '-y',
    '-i', src_vert,
    '-filter_complex',
    '[0:v]split=2[bg][fg];'
    '[bg]scale=1080:1080:force_original_aspect_ratio=increase,crop=1080:1080,gblur=sigma=30,eq=brightness=-0.3[blurred];'
    '[fg]scale=-1:1020[main];'
    '[blurred][main]overlay=(W-w)/2:(H-h)/2[v]',
    '-map', '[v]',
    '-map', '0:a',
    '-c:v', 'libx264',
    '-preset', 'fast',
    '-crf', '18',
    '-c:a', 'aac',
    out_1x1
]
subprocess.run(cmd_1x1, capture_output=True)

print("Exported all 3 formats for Apodex Goldie style video!")
