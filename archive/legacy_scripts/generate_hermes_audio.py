import asyncio
import edge_tts
import os
import subprocess

assets_dir = 'hermes-architecture-video/assets'
os.makedirs(assets_dir, exist_ok=True)

# Transcript adapted for natural spoken pacing
spoken_script = (
    "Hermes Agent od Nous Research je open-source, stále sa zlepšujúci AI agent s uzavretým učiacim sa cyklom. "
    "Skladá sa z piatich hlavných pilierov: "
    "Soul – definuje osobnosť a tón. "
    "Memory – zabezpečuje trvalú pamäť. "
    "Skills – procedurálne recepty a schopnosti. "
    "Tools – viac ako štyridsať nástrojov ako terminál, browser, web search a kód. "
    "A Cron s Gatewayom pre plánovanie a prepojenie na Telegram, Discord či Slack. "
    "Jadro tvorí ReAct loop: pozoruje, myslí, koná a učí sa. "
    "Medzi kľúčové funkcie patrí trvalá pamäť naprieč sessionami, automatické vytváranie nových skills, podpora rôznych modelov a sub-agenti s checkpointami. "
    "Systém si jednoducho prispôsobíte cez súbory Soul dot m d pre osobnosť, User dot m d pre vaše preferencie, Memory dot m d a config súbor. "
    "Tieto nastavenia robia z Hermesa vášho osobného, neustále sa zlepšujúceho asistenta. Sledujte pre viac tipov na AI."
)

async def generate_voice():
    voice = 'sk-SK-LukasNeural'
    communicate = edge_tts.Communicate(spoken_script, voice, rate="+4%")
    out_file = os.path.join(assets_dir, 'voiceover.mp3')
    await communicate.save(out_file)
    print("Voiceover generated at:", out_file)

asyncio.run(generate_voice())
