import asyncio
import edge_tts
import os
import subprocess

assets_dir = 'hermes-viral-video/assets'
os.makedirs(assets_dir, exist_ok=True)

# High-retention viral script with seamless loop and comment hook
viral_script = (
    "Prestaňte používať bežný ChatGPT na kódovanie a zložité projekty. "
    "Hermes Agent od Nous Research je open-source systém, ktorý sa s každou úlohou sám učí a zlepšuje! "
    "Má päť brutálnych pilierov: "
    "Soul pre osobnosť, "
    "trvalú pamäť Memory, "
    "procedurálne Skills, "
    "vyše štyridsať nástrojov ako terminál a browser, "
    "a Gateway prepojený priamo na Telegram či Discord. "
    "Po každej vyriešenej úlohe si sám vytvorí nový skill a uloží ho do vašej lokálnej pamäte. "
    "Všetko si viete prispôsobiť cez súbor Soul dot m d. "
    "Ak chceš kompletnú šablónu na inštaláciu zadarmo, napíš do komentára slovo AGENT a pošlem ti celý návod. "
    "A presne preto by ste mali..."
)

async def generate_voice():
    voice = 'sk-SK-LukasNeural'
    communicate = edge_tts.Communicate(viral_script, voice, rate="+7%")
    out_file = os.path.join(assets_dir, 'voiceover.mp3')
    await communicate.save(out_file)
    print("Viral voiceover generated at:", out_file)

asyncio.run(generate_voice())
