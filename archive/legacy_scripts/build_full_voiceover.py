import asyncio
import edge_tts
import os
import subprocess
import yt_dlp

assets_dir = 'doac-kisin-video/assets'
os.makedirs(assets_dir, exist_ok=True)
url = 'https://www.youtube.com/watch?v=Y43T7VQGtOs'

print("Extracting extra key frames...")
ydl_opts = {'format': 'bestvideo[height<=1080]/best[height<=1080]'}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(url, download=False)
    stream_url = info['url']

extra_ts = {
    'kisin_bartlett.jpg': '00:00:45',
    'kisin_economy.jpg': '00:15:30',
    'kisin_china.jpg': '00:56:30',
    'kisin_action.jpg': '01:28:10'
}

for filename, ts in extra_ts.items():
    out_path = os.path.join(assets_dir, filename)
    cmd = ['ffmpeg', '-y', '-ss', ts, '-i', stream_url, '-frames:v', '1', '-q:v', '2', out_path]
    subprocess.run(cmd, capture_output=True)
    if os.path.exists(out_path):
        print(f"Extracted {filename} ({os.path.getsize(out_path)} bytes)")

print("\nGenerating comprehensive 2-minute Slovak voiceover...")
script_2min = (
    "Svetoví lídri strácajú kontrolu a západná civilizácia čelí najväčšej skúške za posledné desaťročia. "
    "V mimoriadne sledovanej epizóde podcastu The Diary Of A CEO varuje známy autor a komentátor Konstantin Kisin pred sériou kríz, ktoré môžu zmeniť našu spoločnosť od základov. "
    "Prvým varovným signálom je strata legitimity a dôvery v politické inštitúcie. Keď vedenie štátov ignoruje reálne problémy bežných ľudí a ekonomický tlak na strednú triedu prudko rastie, vzniká nebezpečné vákuum, ktoré vedie k polarizácii a spoločenskému nepokoju. "
    "Druhou kľúčovou hrozbou je nástup umelej inteligencie a masívnej automatizácie. Kisin zdôrazňuje, že nejde o bežnú ekonomickú transformáciu, ale o bezprecedentný technologický šok. Vzdelávací systém ani trh práce nie sú pripravené na tempo, akým algoritmy preberajú kognitívne aj manuálne úlohy. "
    "Zároveň porovnáva západný svet s pragmatickou a technologicky dravou Čínou. Na základe svojho detstva v Sovietskom zväze dôrazne varuje pred ideologickou zaslepenosťou a odtrhnutím od reality. "
    "Aké je teda hlavné ponaučenie a praktický návod pre každého z nás? Nespoliehajte sa na štátne záchranné siete. Budujte si praktické a nezameniteľné zručnosti, investujte do technologickej gramotnosti, starajte sa o svoju rodinu a udržiavajte silnú komunitu. "
    "Sledujte náš profil pre viac hĺbkových analýz a praktických zhrnutí svetových podcastov."
)

async def make_full_audio():
    voice = 'sk-SK-LukasNeural'
    communicate = edge_tts.Communicate(script_2min, voice, rate="+2%")
    out_audio = os.path.join(assets_dir, 'voiceover.mp3')
    await communicate.save(out_audio)
    print("Full 2-minute voiceover generated successfully.")

asyncio.run(make_full_audio())
