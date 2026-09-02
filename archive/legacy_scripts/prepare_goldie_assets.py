import yt_dlp
import subprocess
import os
import asyncio
import edge_tts

assets_dir = 'apodex-goldie-video/assets'
os.makedirs(assets_dir, exist_ok=True)
url = 'https://www.youtube.com/watch?v=ijlkO_U1grY'

print("1. Extracting high-res screenshots from Julian Goldie's video...")
ydl_opts = {'format': 'bestvideo[height<=1080]/best[height<=1080]'}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(url, download=False)
    stream_url = info['url']

timestamps = {
    'julian_hook.jpg': '00:00:25',
    'julian_agents.jpg': '00:01:45',
    'julian_whiteboard.jpg': '00:03:35',
    'julian_frontier.jpg': '00:05:15'
}

for filename, ts in timestamps.items():
    out_path = os.path.join(assets_dir, filename)
    cmd = ['ffmpeg', '-y', '-ss', ts, '-i', stream_url, '-frames:v', '1', '-q:v', '2', out_path]
    subprocess.run(cmd, capture_output=True)
    if os.path.exists(out_path):
        print(f"Extracted {filename} at {ts} ({os.path.getsize(out_path)} bytes)")

print("\n2. Generating high-retention Julian Goldie style Slovak voiceover...")
script = (
    "Nový update Apodex 1.1 mení pravidlá hry a prináša asynchrónne tímy AI agentov! "
    "Doteraz si zadal úlohu a 20 minút si pozeral na spinner, len aby si zistil, že agent išiel celú dobu po zlej ceste. "
    "Apodex to rieši v troch krokoch: "
    "Po prvé – Manažérsky rozpad úloh. Model najprv premýšľa ako projektový manažér a rozdelí prácu na samostatné bloky. "
    "Po druhé – Paralelné spracovanie. Namiesto hodiny bežia štyria agenti naraz a skracujú čas zo 60 minút na 15! "
    "A po tretie – Zdieľaná tabuľa a živé riadenie. Ak jeden agent narazí na slepú uličku, okamžite to vidia všetci a ty môžeš zmeniť smer bez reštartu. "
    "Navyše, open-source nástroj Frontier Agent ti umožní spustiť celý tento tím lokálne priamo na tvojom počítači s maximálnym súkromím dát. "
    "Sledujte náš profil pre najnovšie AI stratégie a návody na automatizáciu!"
)

async def make_voice():
    voice = 'sk-SK-LukasNeural'
    communicate = edge_tts.Communicate(script, voice, rate="+7%")
    out_audio = os.path.join(assets_dir, 'voiceover.mp3')
    await communicate.save(out_audio)
    print("Voiceover generated at:", out_audio)

asyncio.run(make_voice())
