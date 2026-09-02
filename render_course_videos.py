"""
===============================================================================
🎬 AUTOMATICKÝ RENDER VIDEO LEKCIÍ PRE GROK BOT KURZ
===============================================================================
Vyrenderuje všetkých 6 MP4 videí lekcií kurzu Grok Bot:
1. Zoberie index.html z priečinka danej lekcie
2. Cez Headless Chrome vygeneruje 1080p snímky jednotlivých scén s prémiovým dizajnom
3. Cez ffmpeg poskladá plnohodnotné MP4 video synchronizované s ElevenLabs audiom
4. Pridá dynamický progress bar a uloží výstupné video
===============================================================================
"""

import os
import sys
import json
import subprocess
import argparse
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

BASE_DIR = Path(__file__).parent.resolve()
GROK_BOT_DIR = BASE_DIR / "course_grok_bot"
VIDEOS_DIR = GROK_BOT_DIR / "videos"
AUDIO_DIR = GROK_BOT_DIR / "audio"

LESSONS = [
    {
        "id": 1,
        "title": "Čo je Grok Bot a prečo je to zlom",
        "audio": AUDIO_DIR / "lekcia_01_co_je_grok_bot.mp3",
        "scenes": [
            {"start": 0.0, "end": 13.0},
            {"start": 13.0, "end": 28.0},
            {"start": 28.0, "end": 41.0},
            {"start": 41.0, "end": None} # None = up to end of audio
        ]
    },
    {
        "id": 2,
        "title": "Architektúra — Chief of Staff a špecialisti",
        "audio": AUDIO_DIR / "lekcia_02_architektura.mp3",
        "scenes": [
            {"start": 0.0, "end": 15.0},
            {"start": 15.0, "end": 32.0},
            {"start": 32.0, "end": 45.0},
            {"start": 45.0, "end": None}
        ]
    },
    {
        "id": 3,
        "title": "Ako začať — prvý bot a pripojenie nástrojov",
        "audio": AUDIO_DIR / "lekcia_03_ako_zacat.mp3",
        "scenes": [
            {"start": 0.0, "end": 15.0},
            {"start": 15.0, "end": 28.0},
            {"start": 28.0, "end": 45.0},
            {"start": 45.0, "end": None}
        ]
    },
    {
        "id": 4,
        "title": "Učenie skillov a rutiny",
        "audio": AUDIO_DIR / "lekcia_04_ucenie_skillov.mp3",
        "scenes": [
            {"start": 0.0, "end": 18.0},
            {"start": 18.0, "end": 35.0},
            {"start": 35.0, "end": 55.0},
            {"start": 55.0, "end": None}
        ]
    },
    {
        "id": 5,
        "title": "Guardrails a bezpečnosť",
        "audio": AUDIO_DIR / "lekcia_05_guardrails.mp3",
        "scenes": [
            {"start": 0.0, "end": 18.0},
            {"start": 18.0, "end": 35.0},
            {"start": 35.0, "end": 48.0},
            {"start": 48.0, "end": None}
        ]
    },
    {
        "id": 6,
        "title": "Ako to celé spojiť a čo ďalej",
        "audio": AUDIO_DIR / "lekcia_06_ako_to_spojit.mp3",
        "scenes": [
            {"start": 0.0, "end": 35.0},
            {"start": 35.0, "end": 55.0},
            {"start": 55.0, "end": None}
        ]
    }
]

def get_audio_duration(audio_path: Path) -> float:
    cmd = [
        'ffprobe', '-v', 'error',
        '-show_entries', 'format=duration',
        '-of', 'default=noprint_wrappers=1:nokey=1',
        str(audio_path)
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    return float(res.stdout.strip())

def capture_scenes_node(lesson_num: int, scene_count: int) -> list:
    cmd = ['node', str(BASE_DIR / 'capture_scenes.mjs'), str(lesson_num), str(scene_count)]
    res = subprocess.run(cmd, capture_output=True, text=True, cwd=str(BASE_DIR))
    if res.returncode != 0:
        raise RuntimeError(f"Chyba pri zachytávaní scén lekcie {lesson_num}:\n{res.stderr}")
    data = json.loads(res.stdout.strip())
    return data.get("paths", [])

def render_lesson(lesson_info: dict) -> Path:
    lesson_id = lesson_info["id"]
    title = lesson_info["title"]
    audio_path = lesson_info["audio"]
    scenes = lesson_info["scenes"]
    scene_count = len(scenes)

    folder_name = f"lesson_{lesson_id:02d}"
    lesson_dir = VIDEOS_DIR / folder_name
    lesson_dir.mkdir(parents=True, exist_ok=True)
    output_mp4 = lesson_dir / f"{folder_name}.mp4"

    print(f"\n=======================================================")
    print(f"🎬 RENDERUJEM LEKCIU {lesson_id:02d}: {title}")
    print(f"=======================================================")

    # 1. Zisti dĺžku audia
    total_duration = get_audio_duration(audio_path)
    print(f"⏱️ Dĺžka lekcie: {total_duration:.2f}s | Počet scén: {scene_count}")

    # Nastav dĺžku poslednej scény
    scenes[-1]["end"] = total_duration

    # 2. Zachyť snímky scén cez Headless Chrome
    print(f"📸 Generujem 1080p grafiku pre {scene_count} scén...")
    scene_images = capture_scenes_node(lesson_id, scene_count)
    print(f"✅ Zachytených {len(scene_images)} vizuálnych scén")

    # 3. Zostav ffmpeg filter complex
    ffmpeg_cmd = ['ffmpeg', '-y']

    # Vstupné obrázky so svojimi dĺžkami
    for i, sc in enumerate(scenes):
        dur = sc["end"] - sc["start"]
        img_path = scene_images[i]
        ffmpeg_cmd.extend(['-loop', '1', '-t', f"{dur:.3f}", '-i', str(img_path)])

    # Vstupné audio
    audio_input_index = len(scenes)
    ffmpeg_cmd.extend(['-i', str(audio_path)])

    # Concat filtrov + animated progress bar
    concat_inputs = "".join([f"[{i}:v]" for i in range(len(scenes))])
    filter_graph = f"{concat_inputs}concat=n={len(scenes)}:v=1:a=0[vbase];"
    filter_graph += f"[vbase]drawbox=x=80:y=1030:w='(1920-160)*(t/{total_duration:.3f})':h=6:color=#6366f1@1.0:t=fill[v]"

    ffmpeg_cmd.extend([
        '-filter_complex', filter_graph,
        '-map', '[v]',
        '-map', f'{audio_input_index}:a',
        '-c:v', 'libx264',
        '-pix_fmt', 'yuv420p',
        '-preset', 'fast',
        '-crf', '18',
        '-c:a', 'aac',
        '-b:a', '192k',
        '-shortest',
        str(output_mp4)
    ])

    print(f"🎞️ Komponujem master video cez FFmpeg...")
    res = subprocess.run(ffmpeg_cmd, capture_output=True, text=True)
    if res.returncode != 0:
        raise RuntimeError(f"FFmpeg zlyhal:\n{res.stderr}")

    size_mb = output_mp4.stat().st_size / (1024 * 1024)
    print(f"✅ Lekcia {lesson_id:02d} úspešne vyrenderovaná!")
    print(f"   📁 Výstup: {output_mp4} ({size_mb:.2f} MB)")
    return output_mp4

def main():
    parser = argparse.ArgumentParser(description="Renderovanie MP4 videí pre Grok Bot kurz")
    parser.add_argument("--lesson", type=int, choices=range(1, 7), help="Vyrenderovať len konkrétnu lekciu (1-6)")
    args = parser.parse_args()

    print("\n" + "=" * 65)
    print("🚀 ŠPUŠŤAM HROMADNÉ GENEROVANIE VIDEO LEKCIÍ KURZU GROK BOT")
    print("=" * 65)

    rendered_files = []
    if args.lesson:
        target = next((l for l in LESSONS if l["id"] == args.lesson), None)
        if target:
            out = render_lesson(target)
            rendered_files.append(out)
    else:
        for lesson_info in LESSONS:
            out = render_lesson(lesson_info)
            rendered_files.append(out)

    print("\n" + "=" * 65)
    print("🎉 VŠETKY LEKCIE BOLI ÚSPEŠNE VYRENDEROVANÉ!")
    print("=" * 65)
    for rf in rendered_files:
        print(f"  🎬 {rf}")
    print("\n")

if __name__ == "__main__":
    main()
