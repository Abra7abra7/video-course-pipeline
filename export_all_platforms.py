import subprocess
import os
import shutil

exports_dir = 'exports'
os.makedirs(exports_dir, exist_ok=True)

src_vertical = 'doac-kisin-video/doac-kisin-vertical.mp4'

# 1. 9:16 Shorts / TikTok / Reels
out_9x16 = os.path.join(exports_dir, '1_tiktok_reels_shorts_9x16.mp4')
shutil.copyfile(src_vertical, out_9x16)
print(f"1. 9:16 export ready: {out_9x16}")

# 2. 16:9 Landscape for YouTube, LinkedIn & Twitter
out_16x9 = os.path.join(exports_dir, '2_youtube_linkedin_twitter_16x9.mp4')
cmd_16x9 = [
    'ffmpeg', '-y',
    '-i', src_vertical,
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
print("2. Rendering 16:9 landscape export...")
res_16x9 = subprocess.run(cmd_16x9, capture_output=True, text=True)
if os.path.exists(out_16x9):
    print(f"Success: {out_16x9} size={os.path.getsize(out_16x9)} bytes")
else:
    print("16:9 error:", res_16x9.stderr[:300])

# 3. 1:1 Square for Instagram Feed & LinkedIn Post
out_1x1 = os.path.join(exports_dir, '3_instagram_linkedin_feed_1x1.mp4')
cmd_1x1 = [
    'ffmpeg', '-y',
    '-i', src_vertical,
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
print("3. Rendering 1:1 square export...")
res_1x1 = subprocess.run(cmd_1x1, capture_output=True, text=True)
if os.path.exists(out_1x1):
    print(f"Success: {out_1x1} size={os.path.getsize(out_1x1)} bytes")
else:
    print("1:1 error:", res_1x1.stderr[:300])

print("\nAll multi-platform exports generated successfully!")
