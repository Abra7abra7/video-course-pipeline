import os
import sys
import subprocess
import shutil
import argparse
from voice_engine import generate_voice

def run_pipeline(title: str, script_text: str, project_name: str = "custom-video"):
    print(f"\n=======================================================")
    print(f"🚀 ŠPUŠŤAM AUTOMATICKÚ VIDEO FABRIKU PRE: {title}")
    print(f"=======================================================\n")

    project_dir = os.path.join(os.getcwd(), project_name)
    assets_dir = os.path.join(project_dir, "assets")
    os.makedirs(assets_dir, exist_ok=True)

    # 1. Skopíruj tvojho avatara do projektu
    user_avatar = os.path.join(os.getcwd(), "assets", "user_avatar.jpg")
    if os.path.exists(user_avatar):
        shutil.copyfile(user_avatar, os.path.join(assets_dir, "user_avatar.jpg"))
        print("✅ Tvoj osobný avatar vložený do projektu.")

    # 2. Vygeneruj hlas (ElevenLabs alebo Edge-TTS)
    voice_file = os.path.join(assets_dir, "voiceover.mp3")
    generate_voice(script_text, voice_file, speed_pct=6)

    # 3. Zisti dĺžku audia cez ffprobe
    cmd_ffprobe = ['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', voice_file]
    res_dur = subprocess.run(cmd_ffprobe, capture_output=True, text=True)
    duration_sec = float(res_dur.stdout.strip() or "40.0")
    total_dur_ceil = int(duration_sec + 1)
    print(f"⏱️ Dĺžka hlasovej stopy: {duration_sec:.2f}s (celková kompozícia: {total_dur_ceil}s)")

    # 4. Priprav HyperFrames súbory
    pkg_json = '''{
  "name": "''' + project_name + '''",
  "version": "1.0.0",
  "type": "module",
  "scripts": {
    "dev": "hyperframes preview",
    "check": "hyperframes check",
    "render": "hyperframes render"
  },
  "devDependencies": {
    "hyperframes": "latest"
  }
}'''
    with open(os.path.join(project_dir, "package.json"), "w", encoding="utf-8") as f:
        f.write(pkg_json)

    # 5. Vyrenderuj video
    out_mp4 = os.path.join(project_dir, f"{project_name}-vertical.mp4")
    print("\n🎬 Renderujem video cez HyperFrames...")
    cmd_render = ["npx", "hyperframes", "render", "--quality", "high", "--output", f"{project_name}-vertical.mp4"]
    subprocess.run(cmd_render, cwd=project_dir)

    # 6. Multi-format export (9:16, 16:9, 1:1)
    exports_dir = os.path.join(os.getcwd(), "exports")
    os.makedirs(exports_dir, exist_ok=True)
    
    if os.path.exists(out_mp4):
        shutil.copyfile(out_mp4, os.path.join(exports_dir, f"{project_name}_9x16.mp4"))
        
        # 16:9
        out_16x9 = os.path.join(exports_dir, f"{project_name}_16x9.mp4")
        subprocess.run([
            'ffmpeg', '-y', '-i', out_mp4,
            '-filter_complex',
            '[0:v]split=2[bg][fg];[bg]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,gblur=sigma=35,eq=brightness=-0.35[blurred];[fg]scale=-1:1000[main];[blurred][main]overlay=(W-w)/2:(H-h)/2[v]',
            '-map', '[v]', '-map', '0:a', '-c:v', 'libx264', '-preset', 'fast', '-crf', '18', '-c:a', 'aac', out_16x9
        ], capture_output=True)

        # 1:1
        out_1x1 = os.path.join(exports_dir, f"{project_name}_1x1.mp4")
        subprocess.run([
            'ffmpeg', '-y', '-i', out_mp4,
            '-filter_complex',
            '[0:v]split=2[bg][fg];[bg]scale=1080:1080:force_original_aspect_ratio=increase,crop=1080:1080,gblur=sigma=30,eq=brightness=-0.3[blurred];[fg]scale=-1:1020[main];[blurred][main]overlay=(W-w)/2:(H-h)/2[v]',
            '-map', '[v]', '-map', '0:a', '-c:v', 'libx264', '-preset', 'fast', '-crf', '18', '-c:a', 'aac', out_1x1
        ], capture_output=True)

        print(f"\n✨ VŠETKY FORMÁTY SÚ HOTOVÉ V ZLOŽKE 'exports/'!")
        print(f"👉 9:16:  exports/{project_name}_9x16.mp4")
        print(f"👉 16:9: exports/{project_name}_16x9.mp4")
        print(f"👉 1:1:  exports/{project_name}_1x1.mp4")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automatická video fabrika")
    parser.add_argument("--title", type=str, default="Hermes Agent Update", help="Názov videa")
    parser.add_argument("--text", type=str, help="Textový scenár")
    parser.add_argument("--file", type=str, help="Cesta k textovému súboru so scenárom")
    args = parser.parse_args()

    script = args.text
    if args.file and os.path.exists(args.file):
        with open(args.file, "r", encoding="utf-8") as f:
            script = f.read()

    if not script:
        script = (
            "Prestaňte používať bežný ChatGPT na zložité projekty. "
            "Hermes Agent od Nous Research je open-source systém s uzavretým učiacim sa cyklom. "
            "Má päť pilierov: Soul pre osobnosť, Memory pre trvalú pamäť, Skills, 40 systémových nástrojov a Gateway na Telegram či Discord. "
            "Ak chcete kompletný návod a šablónu zadarmo, napíšte do komentára slovo AGENT."
        )

    run_pipeline(args.title, script)
