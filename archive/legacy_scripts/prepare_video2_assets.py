import yt_dlp
import subprocess
import os
import asyncio
import edge_tts

assets_dir = 'doac-kisin-video/assets'
os.makedirs(assets_dir, exist_ok=True)
url = 'https://www.youtube.com/watch?v=Y43T7VQGtOs'

print("1. Extracting high-res screenshots from stream...")
ydl_opts = {'format': 'bestvideo[height<=1080]/best[height<=1080]'}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(url, download=False)
    stream_url = info['url']

timestamps = {
    'kisin_intro.jpg': '00:01:15',
    'kisin_leaders.jpg': '00:05:30',
    'kisin_ai.jpg': '01:14:05',
    'kisin_future.jpg': '01:27:00'
}

for filename, ts in timestamps.items():
    out_path = os.path.join(assets_dir, filename)
    cmd = ['ffmpeg', '-y', '-ss', ts, '-i', stream_url, '-frames:v', '1', '-q:v', '2', out_path]
    subprocess.run(cmd, capture_output=True)
    if os.path.exists(out_path):
        print(f"Extracted {filename} at {ts} ({os.path.getsize(out_path)} bytes)")

print("\n2. Generating 2-minute Slovak voiceover...")
script_text = (
    "Svetoví lídri strácajú kontrolu a západná civilizácia stojí pred zásadným zlomom. "
    "V tejto silnej epizóde podcastu The Diary Of A CEO varuje spisovateľ a komentátor Konstantin Kisin pred blížiacou sa krízou inštitúcií a rozpadom dôvery v spoločnosti. "
    "Prvým veľkým varovaním je strata legitimity politických elít. Keď sa prehliadajú reálne problémy bežných ľudí a ekonomický tlak rastie, spoločnosť sa začína polarizovať a radikalizovať. "
    "Druhou obrovskou témou je nástup umelej inteligencie a automatizácie. Kisin upozorňuje, že AI nespôsobí len bežnú zmenu práce, ale hlboký technologický šok, na ktorý náš vzdelávací a sociálny systém nie je pripravený. "
    "Porovnáva západný model s autoritárskou Čínou a pripomína svoje detstvo v Sovietskom zväze ako varovanie pred ideologickým dogmatizmom. "
    "Aké je teda hlavné posolstvo pre jednotlivca? Nespoliehať sa na štátne garancie, ale investovať do vlastného vzdelania, adaptibility a budovania silnej rodiny a komunity. "
    "Sledujte náš kanál pre viac hĺbkových analýz a zhrnutí kľúčových rozhovorov."
)

async def make_audio():
    voice = 'sk-SK-LukasNeural'
    communicate = edge_tts.Communicate(script_text, voice, rate="+5%")
    out_audio = os.path.join(assets_dir, 'voiceover.mp3')
    await communicate.save(out_audio)
    print("Voiceover generated at:", out_audio)

asyncio.run(make_audio())
