"""
===============================================================================
🚀 AUTOMATED CONTENT & COURSE VIDEO FACTORY PIPELINE
===============================================================================
Modulárna programovateľná pipeline pre tvorbu:
1. Interaktívnych kurzov (Webový portál + Audio + Hovoriaci AI Avatar)
2. YouTube videí (16:9 Full HD)
3. TikTok / Reels / Shorts videí (9:16 vertikál)
4. Instagram / LinkedIn Feed videí (1:1 štvorec)
===============================================================================
"""

import os
import sys
import json
import shutil
import argparse
import subprocess
import requests
from dotenv import load_dotenv

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

load_dotenv()
from voice_engine import generate_voice

class ContentPipeline:
    def __init__(self):
        self.eleven_key = os.getenv("ELEVENLABS_API_KEY")
        self.eleven_voice = os.getenv("ELEVENLABS_VOICE_ID", "4t72Xc6JKiBerVUqj6oK")
        self.heygen_key = os.getenv("HEYGEN_API_KEY")
        self.exports_dir = os.path.join(os.getcwd(), "exports")
        os.makedirs(self.exports_dir, exist_ok=True)

    def generate_lesson_audio(self, text: str, output_path: str, speed_pct: int = 6):
        """Vygeneruje audio lekcie cez ElevenLabs"""
        print(f"🎙️ Generujem hlas pre: {output_path}")
        return generate_voice(text, output_path, speed_pct=speed_pct)

    def export_all_formats(self, input_video: str, project_name: str):
        """
        Zoberie zdrojové video a automaticky vygeneruje:
        - 16:9 (YouTube / Web)
        - 9:16 (TikTok / Reels / Shorts)
        - 1:1 (Instagram / LinkedIn Feed)
        """
        if not os.path.exists(input_video):
            print(f"❌ Zdrojové video neexistuje: {input_video}")
            return False

        print(f"\n🎬 Generujem multi-platformové formáty pre '{project_name}'...")
        out_16x9 = os.path.join(self.exports_dir, f"{project_name}_16x9.mp4")
        out_9x16 = os.path.join(self.exports_dir, f"{project_name}_9x16.mp4")
        out_1x1 = os.path.join(self.exports_dir, f"{project_name}_1x1.mp4")

        # 16:9 (Landscape)
        cmd_16x9 = [
            'ffmpeg', '-y', '-i', input_video,
            '-filter_complex',
            '[0:v]split=2[bg][fg];[bg]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,gblur=sigma=35,eq=brightness=-0.35[blurred];[fg]scale=-1:1000[main];[blurred][main]overlay=(W-w)/2:(H-h)/2[v]',
            '-map', '[v]', '-map', '0:a', '-c:v', 'libx264', '-preset', 'fast', '-crf', '18', '-c:a', 'aac', out_16x9
        ]
        subprocess.run(cmd_16x9, capture_output=True)

        # 9:16 (Vertical)
        cmd_9x16 = [
            'ffmpeg', '-y', '-i', input_video,
            '-filter_complex',
            '[0:v]split=2[bg][fg];[bg]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,gblur=sigma=35,eq=brightness=-0.35[blurred];[fg]scale=1000:-1[main];[blurred][main]overlay=(W-w)/2:(H-h)/2[v]',
            '-map', '[v]', '-map', '0:a', '-c:v', 'libx264', '-preset', 'fast', '-crf', '18', '-c:a', 'aac', out_9x16
        ]
        subprocess.run(cmd_9x16, capture_output=True)

        # 1:1 (Square)
        cmd_1x1 = [
            'ffmpeg', '-y', '-i', input_video,
            '-filter_complex',
            '[0:v]split=2[bg][fg];[bg]scale=1080:1080:force_original_aspect_ratio=increase,crop=1080:1080,gblur=sigma=30,eq=brightness=-0.3[blurred];[fg]scale=-1:1020[main];[blurred][main]overlay=(W-w)/2:(H-h)/2[v]',
            '-map', '[v]', '-map', '0:a', '-c:v', 'libx264', '-preset', 'fast', '-crf', '18', '-c:a', 'aac', out_1x1
        ]
        subprocess.run(cmd_1x1, capture_output=True)

        print(f"✅ Hotovo! Exportované do '{self.exports_dir}/':")
        print(f"   📺 16:9:  {out_16x9}")
        print(f"   📱 9:16:  {out_9x16}")
        print(f"   🖼️ 1:1:   {out_1x1}")
        return True

    def sync_heygen_avatar(self, target_dir: str):
        """Zosynchronizuje najnovšieho HeyGen avatara do cieľového priečinka"""
        assets_dir = os.path.join(target_dir, "assets")
        os.makedirs(assets_dir, exist_ok=True)
        src_video = "course_grok2/assets/heygen_avatar.mp4"
        src_img = "course_grok2/assets/heygen_avatar.jpg"
        if os.path.exists(src_video):
            shutil.copyfile(src_video, os.path.join(assets_dir, "heygen_avatar.mp4"))
        if os.path.exists(src_img):
            shutil.copyfile(src_img, os.path.join(assets_dir, "heygen_avatar.jpg"))
        print(f"✅ HeyGen avatar zosynchronizovaný do {assets_dir}")

def main():
    parser = argparse.ArgumentParser(description="Automatická Video & Content Fabrika")
    parser.add_argument("--action", choices=["export", "voice", "sync-avatar"], default="export", help="Akcia na vykonanie")
    parser.add_argument("--input", type=str, help="Cesta k vstupnému videu pre multi-export")
    parser.add_argument("--name", type=str, default="output", help="Názov výstupu")
    parser.add_argument("--text", type=str, help="Text pre generovanie hlasu")
    parser.add_argument("--target", type=str, default="course_grok2", help="Cieľový priečinok kurzu")
    args = parser.parse_args()

    pipeline = ContentPipeline()

    if args.action == "export":
        if not args.input:
            print("Zadajte --input cestu k MP4 videu (napr. --input exports/1_tiktok_reels_shorts_9x16.mp4)")
            sys.exit(1)
        pipeline.export_all_formats(args.input, args.name)

    elif args.action == "voice":
        if not args.text:
            print("Zadajte --text pre generovanie hlasu")
            sys.exit(1)
        out = f"assets/{args.name}.mp3"
        pipeline.generate_lesson_audio(args.text, out)

    elif args.action == "sync-avatar":
        pipeline.sync_heygen_avatar(args.target)

if __name__ == "__main__":
    main()
