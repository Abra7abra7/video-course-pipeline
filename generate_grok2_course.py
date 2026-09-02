import os
import sys
import subprocess
from dotenv import load_dotenv

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

load_dotenv()
from voice_engine import generate_voice

LESSONS_GROK2 = [
    {
        "id": 1,
        "title": "Grok 2 a Evolúcia Agentic Systémov",
        "filename": "lekcia_01_grok2_evolucia.mp3",
        "text": """Vitaj v pokročilom kurze Grok 2. Dnes sa pozrieme pod kapotu novej generácie autonómnych agentov od xAI. Grok 2 nepredstavuje len väčší jazykový model s lepším reasoningom. Je to kompletný operačný systém pre umelú inteligenciu. Rozdiel medzi bežným LLM a agentic runtime je zásadný: model len predpovedá tokeny, zatiaľ čo Grok 2 beží v perzistentnom virtuálnom prostredí, má prístup k systémovému bashu, browseru a izolovanému pamäťovému modulu. Poďme sa pozrieť, ako funguje jadro tohto systému."""
    },
    {
        "id": 2,
        "title": "Hĺbková Architektúra: Dual-Brain a Router",
        "filename": "lekcia_02_dual_brain_architektura.mp3",
        "text": """Srdcom Grok 2 agenta je architektúra Dual-Brain. Pozostáva z dvoch kľúčových komponentov: Fast Reasoning Kernel a Meta-Controller, známy ako Chief of Staff. Keď príde požiadavka, Router najprv analyzuje jej sémantickú komplexitu. Jednoduché úlohy vybaví priamo v mikrosekundách. Zložité výpočty a viac-krokové workflows rozdelí do stromu podúloh. Tento strom je riadený dynamickým kontextovým oknom, ktoré prepája vektorovú databázu s dlhodobou epizodickou pamäťou. Vďaka tomu agent nikdy nestráca kontext ani po týždňoch behu."""
    },
    {
        "id": 3,
        "title": "Tool Execution Bus a Sandboxing",
        "filename": "lekcia_03_tool_bus_sandboxing.mp3",
        "text": """Ako Grok 2 vykonáva akcie bez toho, aby halucinoval? Kľúčom je Tool Execution Bus. Namiesto toho, aby model len vymýšľal odpovede, posiela štruktúrované JSON príkazy do zabezpečeného sandboxu. Sandbox obsahuje plnohodnotný Linux terminál, headless prehliadač Chromium a API adaptéry pre Gmail, Slack či GitHub. Každá akcia prebehne v reálnom čase, výstup sa validuje cez error-handling modul a až overený výsledok sa vracia do mozgu agenta. Tento uzavretý cyklus zaručuje 99-percentnú deterministickú presnosť."""
    },
    {
        "id": 4,
        "title": "Teach a Task 2.0 a Kompilácia Skillov",
        "filename": "lekcia_04_teach_task_kompilacia.mp3",
        "text": """V štvrtej lekcii sa pozrieme na najinovatívnejšiu technológiu Grok 2: Teach a Task 2.0. Keď nahráš obrazovku so svojím pracovným postupom, Grok 2 neukladá len pixely. Multimodálny parser analyzuje kliknutia myšou, klávesové skratky a DOM štruktúru webu. Tento vizuálny záznam následne skompiluje do čistého, optimalizovaného Python skriptu. Z jednorazovej ukážky sa stane trvalý, verzovaný skill s vlastným API endpointom, ktorý sa automaticky spúšťa cez cron alebo webhooky."""
    },
    {
        "id": 5,
        "title": "Multi-Agent Swarm Protocol a P2P Komunikácia",
        "filename": "lekcia_05_swarm_protocol_p2p.mp3",
        "text": """Keď potrebuješ škálovať desiatky procesov naraz, jeden agent nestačí. Grok 2 využíva Swarm Protocol na koordináciu tímu špecialistov. Inbox bot, Calendar bot, Research bot a Code bot nečakajú na pokyny zhora. Komunikujú cez distribuovanú P2P zbernicu. Keď Research bot dokončí analýzu trhu, vygeneruje stavový handoff token a priamo zobudí Content bota. Synchronizácia prebieha asynchrónne na pozadí, čím dosahuje paralelizáciu práce a extrémne nízku latenciu."""
    },
    {
        "id": 6,
        "title": "Enterprise Guardrails a Bezpečnostný Zero-Trust Model",
        "filename": "lekcia_06_enterprise_guardrails.mp3",
        "text": """V poslednej lekcii si prejdeme to najdôležitejšie: ako celý systém bezpečne nasadiť v podniku. Grok 2 implementuje striktný Zero-Trust bezpečnostný model. Každý agent má presne definované RBAC práva. Zavádza sa princíp troch zón: zelená pre autonómne čítanie, oranžová pre draftovanie s notifikáciou a červená pre kritické akcie, ako je platba či odoslanie zmluvy. Tlačidlo finálneho potvrdenia zostáva vždy v rukách človeka. S týmto nastavením máte v rukách bezpečný a nezastaviteľný digitálny tím."""
    }
]

def main():
    output_dir = os.path.join(os.getcwd(), "course_grok2", "audio")
    os.makedirs(output_dir, exist_ok=True)

    print("\n=======================================================")
    print("🎙️ SPÚŠŤAM GENEROVANIE POKROČILÉHO KURZU GROK 2 (ELEVENLABS)")
    print(f"Počet lekcií: {len(LESSONS_GROK2)}")
    print("=======================================================\n")

    for l in LESSONS_GROK2:
        out_path = os.path.join(output_dir, l["filename"])
        print(f"\n--- Lekcia {l['id']}: {l['title']} ---")
        generate_voice(l["text"], out_path)

    # Vytvor zjednotené audio
    print("\n🎼 Vytváram spojené master audio pre celý kurz Grok 2...")
    concat_list = "|".join([os.path.join(output_dir, l["filename"]) for l in LESSONS_GROK2])
    full_audio = os.path.join(output_dir, "full_course_grok2.mp3")
    cmd_concat = ['ffmpeg', '-y', '-i', f"concat:{concat_list}", '-acodec', 'copy', full_audio]
    subprocess.run(cmd_concat, capture_output=True)
    print(f"✅ Celý kurz spojený do: {full_audio}")

if __name__ == "__main__":
    main()
