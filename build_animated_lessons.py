import os
import sys
import json

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

LESSONS_DATA = [
    {
        "id": 1,
        "title": "Čo je Grok Bot a prečo je to zlom",
        "duration": 50.4,
        "audio_file": "../audio/lekcia_01_co_je_grok_bot.mp3",
        "scenes": [
            {
                "time_start": 0,
                "time_end": 13,
                "badge": "Úvod do kurzu",
                "heading": "Čo je Grok Bot?",
                "subheading": "Virálny workshop SpaceX AI inžinierky Lauren Tan, ktorý obletel svet.",
                "visual_type": "hero_intro",
                "cards": [
                    {"icon": "🚀", "title": "Lauren Tan", "desc": "SpaceX AI Inžinierka"},
                    {"icon": "⚡", "title": "Grok Bot", "desc": "Autonómny agent tím"},
                    {"icon": "🎯", "title": "Marian Stančík", "desc": "Lektor kurzu"}
                ]
            },
            {
                "time_start": 13,
                "time_end": 28,
                "badge": "Zmena paradigmy",
                "heading": "Chatbot vs. Skutočný Agent Tím",
                "subheading": "Agenti majú vlastný počítač v cloude a pracujú nonstop v tvojich nástrojoch.",
                "visual_type": "comparison",
                "left_card": {
                    "badge": "Bežný Chatbot",
                    "points": ["Píšeš otázky, vráti text", "Žiadna vlastná akcia", "Čaká na tvoj laptop"]
                },
                "right_card": {
                    "badge": "Grok Bot Agent Tím",
                    "points": ["Prihlásený do Gmailu, Slacku, GitHubu", "Vlastný cloud počítač", "Nezaspáva, pracuje 24/7"]
                }
            },
            {
                "time_start": 28,
                "time_end": 41,
                "badge": "Prax z xAI",
                "heading": "10 až 20 agentov pod jedným velením",
                "subheading": "Ovládanie celého tímu cez jediného Chief of Staff agenta.",
                "visual_type": "stats",
                "stat_number": "90%",
                "stat_label": "Denná rutina zautomatizovaná",
                "note": "Agenti bežia paralelne na pozadí aj keď zatvoríš laptop."
            },
            {
                "time_start": 41,
                "time_end": 51,
                "badge": "Čo ťa čaká",
                "heading": "Postav si vlastný systém",
                "subheading": "V nasledujúcich lekciách si krok za krokom nastavíme vlastný tím agentov.",
                "visual_type": "roadmap_preview",
                "steps": ["1. Architektúra", "2. Nastavenie & Nástroje", "3. Teach a Task", "4. Guardrails", "5. Nasadenie"]
            }
        ]
    },
    {
        "id": 2,
        "title": "Architektúra — Chief of Staff a špecialisti",
        "duration": 56.2,
        "audio_file": "../audio/lekcia_02_architektura.mp3",
        "scenes": [
            {
                "time_start": 0,
                "time_end": 15,
                "badge": "Kľúčový princíp",
                "heading": "Jeden Orchestrátor: Chief of Staff",
                "subheading": "Nekomunikuješ so všetkými botmi naraz. Hovoríš len s jedným koordinátorom.",
                "visual_type": "orchestrator",
                "orchestrator_name": "Chief of Staff",
                "orchestrator_desc": "Osobný asistent, ktorý pozná všetkých odborníkov v tvojej firme"
            },
            {
                "time_start": 15,
                "time_end": 32,
                "badge": "Praktický príklad",
                "heading": "Príprava cenovej ponuky pre klienta",
                "subheading": "Chief of Staff automaticky rozdelí úlohu medzi špecialistov.",
                "visual_type": "workflow_flow",
                "flow": [
                    {"step": "1", "title": "Ty zadáš požiadavku", "desc": "Priprav ponuku pre klienta"},
                    {"step": "2", "title": "Kalkulácia", "desc": "Špecialista spočíta ceny"},
                    {"step": "3", "title": "Copywriting", "desc": "Content bot napíše text"},
                    {"step": "4", "title": "Odoslanie", "desc": "Inbox bot pripraví draft"}
                ]
            },
            {
                "time_start": 32,
                "time_end": 45,
                "badge": "Tím špecialistov",
                "heading": "5 Trvalých Rolí v Tíme",
                "subheading": "Každý má vlastnú doménu a dlhodobú pamäť.",
                "visual_type": "specialist_grid",
                "specialists": [
                    {"name": "Inbox Manager", "role": "Správa pošty & triedenie", "icon": "📬"},
                    {"name": "Calendar Scheduler", "role": "Plánovanie meetingov", "icon": "📅"},
                    {"name": "To-Do Organizer", "role": "Sledovanie úloh", "icon": "✅"},
                    {"name": "Research Bot", "role": "Prieskum trhu", "icon": "🔍"},
                    {"name": "Content Bot", "role": "Tvorba príspevkov & textov", "icon": "✍️"}
                ]
            },
            {
                "time_start": 45,
                "time_end": 57,
                "badge": "Zhrnutie",
                "heading": "Nie 1 super-agent, ale koordinovaný tím",
                "subheading": "Špecialisti medzi sebou komunikujú priamo a autonómne sa zlepšujú.",
                "visual_type": "insight_card",
                "insight": "Dlhodobá pamäť + Špecializácia + Koordinácia = 10x vyššia produktivita"
            }
        ]
    },
    {
        "id": 3,
        "title": "Ako začať — prvý bot a pripojenie nástrojov",
        "duration": 65.3,
        "audio_file": "../audio/lekcia_03_ako_zacat.mp3",
        "scenes": [
            {
                "time_start": 0,
                "time_end": 15,
                "badge": "Krok 1",
                "heading": "Stiahnutie aplikácie",
                "subheading": "Grok Bot je dostupný pre macOS a iOS.",
                "visual_type": "app_download",
                "platforms": [
                    {"name": "macOS", "status": "Odporúčané prostredie", "icon": "💻"},
                    {"name": "iOS", "status": "Mobilný prístup", "icon": "📱"},
                    {"name": "Android", "status": "Zatiaľ nie je podporovaný", "icon": "⏳"}
                ]
            },
            {
                "time_start": 15,
                "time_end": 28,
                "badge": "Krok 2",
                "heading": "Vytvorenie prvého bota",
                "subheading": "Daj mu okamžite rolu Chief of Staff.",
                "visual_type": "first_bot",
                "bot_title": "Chief of Staff",
                "tip": "Nepremýšľaj nad tým príliš zložito — toto je základný kameň celého systému."
            },
            {
                "time_start": 28,
                "time_end": 45,
                "badge": "Krok 3",
                "heading": "Pripojenie nástrojov (Auth)",
                "subheading": "Stačí sa prihlásiť raz a prístup získajú všetci boti v tíme.",
                "visual_type": "tools_connect",
                "tools": [
                    {"name": "Gmail", "desc": "Čítanie a draftovanie pošty", "color": "#ea4335"},
                    {"name": "Google Calendar", "desc": "Plánovanie rozvrhu", "color": "#4285f4"},
                    {"name": "Slack", "desc": "Interná tímová komunikácia", "color": "#4a154b"}
                ]
            },
            {
                "time_start": 45,
                "time_end": 66,
                "badge": "Krok 4 — Kľúčový moment",
                "heading": "Daj Chief of Staff voľnosť",
                "subheading": "Povedz mu: 'Tu sú moje nástroje, navrhni mi tím na mieru.'",
                "visual_type": "magic_prompt",
                "prompt_box": "\"Tu sú moje nástroje a moja denná agenda. Navrhni mi zloženie tímu agentov, ktorý by mi najviac pomohol.\"",
                "outcome": "On navrhne štruktúru, ty ju len schváliš jedným klikom."
            }
        ]
    },
    {
        "id": 4,
        "title": "Učenie skillov a rutiny",
        "duration": 73.2,
        "audio_file": "../audio/lekcia_04_ucenie_skillov.mp3",
        "scenes": [
            {
                "time_start": 0,
                "time_end": 18,
                "badge": "Revolučná funkcia",
                "heading": "Teach a Task: Žiadne zložité prompty",
                "subheading": "Zapneš nahrávanie obrazovky, spravíš úlohu a bot sa ju naučí.",
                "visual_type": "teach_task",
                "steps": [
                    {"title": "1. Spusť nahrávanie", "icon": "🔴"},
                    {"title": "2. Vykonaj úlohu ručne", "icon": "🖱️"},
                    {"title": "3. Bot si uloží skill", "icon": "🧠"}
                ]
            },
            {
                "time_start": 18,
                "time_end": 35,
                "badge": "Učenie preferencií",
                "heading": "Bot si pamätá tvoj osobný štýl",
                "subheading": "Keď opravíš detail, nabudúce ho spraví automaticky správne.",
                "visual_type": "preferences",
                "examples": [
                    "\"Faktúry radšej spracúvam večer, nie ráno\"",
                    "\"Formát tabuľky vždy zoradiť podľa dátumu\"",
                    "\"Tón komunikácie: priateľský ale priamy\""
                ]
            },
            {
                "time_start": 35,
                "time_end": 55,
                "badge": "Automatizácia v cloude",
                "heading": "Rutiny: Bežia aj keď spíš",
                "subheading": "Triggery na základe času alebo prichádzajúcich udalostí.",
                "visual_type": "routines_list",
                "routines": [
                    {"time": "08:00 Ráno", "action": "Priprav ranný sumár prioritných emailov", "icon": "☀️"},
                    {"time": "Udalosť: Faktúra > 1000€", "action": "Automaticky priprav na schválenie", "icon": "💶"},
                    {"time": "Pondelok 09:00", "action": "Vygeneruj týždenný report stavu projektov", "icon": "📊"}
                ]
            },
            {
                "time_start": 55,
                "time_end": 74,
                "badge": "Reálny príklad z xAI",
                "heading": "Autonómny Feedback Loop",
                "subheading": "Boti sami opravujú nahlásené bugy ešte skôr, než človek otvorí ticket.",
                "visual_type": "quote_highlight",
                "quote": "\"To už nie je obyčajná automatizácia. To je plnohodnotný digitálny zamestnanec.\""
            }
        ]
    },
    {
        "id": 5,
        "title": "Guardrails a bezpečnosť",
        "duration": 60.6,
        "audio_file": "../audio/lekcia_05_guardrails.mp3",
        "scenes": [
            {
                "time_start": 0,
                "time_end": 18,
                "badge": "Základné pravidlo",
                "heading": "Agent je ako nový zamestnanec",
                "subheading": "Potrebuje presne definované hranice a pravidlá.",
                "visual_type": "security_intro",
                "message": "Dať botovi prístup k emailom bez pravidiel je obrovské riziko. Guardrails sú nevyhnutnosť."
            },
            {
                "time_start": 18,
                "time_end": 35,
                "badge": "3 Kľúčové otázky",
                "heading": "Nastavenie Hraníc",
                "subheading": "Odpovedz na tieto 3 otázky pre každého bota v tíme.",
                "visual_type": "security_zones",
                "zones": [
                    {"level": "Zelená zóna", "question": "Čo smie robiť bez pýtania?", "color": "#10b981"},
                    {"level": "Oranžová zóna", "question": "Na čo potrebuje tvoje schválenie?", "color": "#f59e0b"},
                    {"level": "Červená zóna", "question": "Čo nesmie urobiť NIKDY?", "color": "#ef4444"}
                ]
            },
            {
                "time_start": 35,
                "time_end": 48,
                "badge": "Human-in-the-Loop",
                "heading": "Tlačidlo 'SEND' máš len ty",
                "subheading": "Boti draftujú, pripravujú ponuky, ale finálne odoslanie riadiš ty.",
                "visual_type": "send_button_rule",
                "principle": "Bot, ktorý sa pýta na všetko, zdržuje. Bot, ktorý sa nepýta nikdy, je nebezpečný."
            },
            {
                "time_start": 48,
                "time_end": 61,
                "badge": "Cloud Bezpečnosť",
                "heading": "Bezpečnosť nie je nastavenie, je to návyk",
                "subheading": "Všetci boti zdieľajú jeden cloud počítač. Chráň heslá a citlivé dáta.",
                "visual_type": "security_checklist",
                "checklist": [
                    "Nedávaj prístup k veciam, ktoré bot nepotrebuje",
                    "Pravidelne kontroluj denník aktivít botov",
                    "Pri podozrení proces okamžite zastav"
                ]
            }
        ]
    },
    {
        "id": 6,
        "title": "Ako to celé spojiť a čo ďalej",
        "duration": 75.6,
        "audio_file": "../audio/lekcia_06_ako_to_spojit.mp3",
        "scenes": [
            {
                "time_start": 0,
                "time_end": 35,
                "badge": "Kompletný postup",
                "heading": "9 Krokov k Vlastnému AI Tímu",
                "subheading": "Stručný checklist implementácie od stiahnutia po škálovanie.",
                "visual_type": "nine_steps",
                "steps": [
                    "1. Stiahni Grok Bot macOS appku",
                    "2. Vytvor Chief of Staff bota",
                    "3. Pripoj Gmail a kalendár",
                    "4. Nechaj Chief of Staff navrhnúť tím",
                    "5. Schváľ a postav špecialistov",
                    "6. Nastav bezpečnostné guardrails",
                    "7. Nauč prvý skill cez Teach a Task",
                    "8. Vytvor cloud rutinu",
                    "9. Testuj, opravuj a postupne rozširuj"
                ]
            },
            {
                "time_start": 35,
                "time_end": 55,
                "badge": "Zlaté pravidlo",
                "heading": "Začni s 1 výborným botom",
                "subheading": "Multi-agent setupy zlyhávajú, ak človek postaví 6 priemerných botov naraz.",
                "visual_type": "golden_rule",
                "advice": "Opýtaj sa Chief of Staff: 'Akého jedného bota by si mi odporučil na začiatok?'"
            },
            {
                "time_start": 55,
                "time_end": 76,
                "badge": "Vízia 2026",
                "heading": "Nový spôsob ako uvažovať o práci",
                "subheading": "Nie 'aký prompt napíšem', ale 'akého človeka najmem'.",
                "visual_type": "author_outro",
                "outro_author": "Marian Stančík",
                "contact": "marianstancik@agentmail.to",
                "thanks": "Ďakujem za pozornosť!"
            }
        ]
    }
]

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="sk">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=1920, height=1080">
  <title>Lekcia {lesson_id}: {lesson_title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@500;700;800&display=swap" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
  <style>
    * {{
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }}
    html, body {{
      width: 1920px;
      height: 1080px;
      overflow: hidden;
      background: #06080d;
      color: #ffffff;
      font-family: 'Plus Jakarta Sans', sans-serif;
    }}
    .video-canvas {{
      position: relative;
      width: 1920px;
      height: 1080px;
      background: radial-gradient(circle at 15% 20%, rgba(99, 102, 241, 0.22) 0%, transparent 50%),
                  radial-gradient(circle at 85% 80%, rgba(6, 182, 212, 0.18) 0%, transparent 50%),
                  #06080d;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: 60px 80px;
    }}

    .grid-lines {{
      position: absolute;
      inset: 0;
      background-image: linear-gradient(to right, rgba(255, 255, 255, 0.03) 1px, transparent 1px),
                        linear-gradient(to bottom, rgba(255, 255, 255, 0.03) 1px, transparent 1px);
      background-size: 60px 60px;
      pointer-events: none;
    }}

    /* Top Bar */
    .top-bar {{
      position: relative;
      z-index: 10;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .course-badge {{
      display: inline-flex;
      align-items: center;
      gap: 12px;
      background: rgba(99, 102, 241, 0.18);
      border: 1px solid rgba(99, 102, 241, 0.4);
      color: #c7d2fe;
      padding: 12px 28px;
      border-radius: 999px;
      font-size: 20px;
      font-weight: 700;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      box-shadow: 0 0 20px rgba(99, 102, 241, 0.25);
    }}
    .pulse-dot {{
      width: 12px;
      height: 12px;
      background: #06b6d4;
      border-radius: 50%;
      box-shadow: 0 0 14px #06b6d4;
    }}
    .author-badge {{
      display: flex;
      align-items: center;
      gap: 14px;
      font-size: 22px;
      color: #94a3b8;
    }}
    .author-badge strong {{
      color: #fff;
    }}

    /* Dynamic Scene Container */
    .scene-viewport {{
      position: relative;
      flex: 1;
      margin: 40px 0;
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 10;
    }}

    .scene-card {{
      position: absolute;
      inset: 0;
      opacity: 0;
      visibility: hidden;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      text-align: center;
    }}

    .scene-card.active {{
      opacity: 1;
      visibility: visible;
    }}

    .scene-pill {{
      display: inline-block;
      background: rgba(6, 182, 212, 0.15);
      border: 1px solid rgba(6, 182, 212, 0.4);
      color: #67e8f9;
      padding: 8px 24px;
      border-radius: 999px;
      font-size: 18px;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      margin-bottom: 24px;
    }}

    .scene-heading {{
      font-size: 56px;
      font-weight: 900;
      line-height: 1.15;
      margin-bottom: 20px;
      background: linear-gradient(135deg, #ffffff 40%, #c7d2fe 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      max-width: 1400px;
    }}

    .scene-subheading {{
      font-size: 28px;
      color: #94a3b8;
      max-width: 1100px;
      line-height: 1.5;
      margin-bottom: 40px;
    }}

    /* Card Visual Layouts */
    .grid-3 {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 30px;
      width: 100%;
      max-width: 1400px;
    }}

    .feature-card {{
      background: rgba(18, 24, 38, 0.75);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 24px;
      padding: 36px 30px;
      text-align: center;
      backdrop-filter: blur(20px);
      box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
      transition: all 0.3s ease;
    }}
    .feature-icon {{
      font-size: 48px;
      margin-bottom: 16px;
    }}
    .feature-title {{
      font-size: 26px;
      font-weight: 800;
      margin-bottom: 10px;
      color: #fff;
    }}
    .feature-desc {{
      font-size: 19px;
      color: #94a3b8;
      line-height: 1.4;
    }}

    .stat-box {{
      background: linear-gradient(145deg, rgba(99, 102, 241, 0.15), rgba(18, 24, 38, 0.85));
      border: 2px solid rgba(99, 102, 241, 0.5);
      border-radius: 32px;
      padding: 50px 80px;
      box-shadow: 0 0 50px rgba(99, 102, 241, 0.3);
      display: inline-block;
    }}
    .stat-big {{
      font-size: 110px;
      font-weight: 900;
      color: #38bdf8;
      line-height: 1;
      font-family: 'JetBrains Mono', monospace;
      text-shadow: 0 0 30px rgba(56, 189, 248, 0.6);
    }}
    .stat-text {{
      font-size: 30px;
      font-weight: 700;
      color: #fff;
      margin-top: 15px;
    }}

    .quote-box {{
      background: rgba(99, 102, 241, 0.12);
      border-left: 6px solid #6366f1;
      border-radius: 0 24px 24px 0;
      padding: 40px 50px;
      font-size: 34px;
      font-weight: 700;
      color: #e2e8f0;
      max-width: 1200px;
      line-height: 1.5;
    }}

    /* Bottom Control Bar */
    .bottom-bar {{
      position: relative;
      z-index: 10;
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: rgba(15, 20, 32, 0.85);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 20px;
      padding: 16px 32px;
      backdrop-filter: blur(16px);
    }}

    .playback-info {{
      display: flex;
      align-items: center;
      gap: 20px;
    }}
    .btn-play {{
      width: 50px;
      height: 50px;
      border-radius: 50%;
      background: #6366f1;
      border: none;
      color: #fff;
      font-size: 22px;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 0 20px rgba(99, 102, 241, 0.6);
    }}
    .time-code {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 20px;
      color: #94a3b8;
    }}

    .progress-track {{
      flex: 1;
      margin: 0 30px;
      height: 8px;
      background: rgba(255, 255, 255, 0.1);
      border-radius: 4px;
      overflow: hidden;
      position: relative;
      cursor: pointer;
    }}
    .progress-bar {{
      height: 100%;
      width: 0%;
      background: linear-gradient(90deg, #6366f1, #06b6d4);
      border-radius: 4px;
    }}
  </style>
</head>
<body>

  <div class="video-canvas" id="canvas">
    <div class="grid-lines"></div>

    <!-- Top Bar -->
    <header class="top-bar">
      <div class="course-badge">
        <span class="pulse-dot"></span>
        Grok Bot AI Agent Tím • Lekcia {lesson_id}
      </div>
      <div class="author-badge">
        Lektor: <strong>Marian Stančík</strong> | ElevenLabs Custom Voice
      </div>
    </header>

    <!-- Scene Container -->
    <main class="scene-viewport" id="scene-viewport">
      {rendered_scenes}
    </main>

    <!-- Bottom Player Bar -->
    <footer class="bottom-bar">
      <div class="playback-info">
        <button class="btn-play" id="btn-play">▶</button>
        <span class="time-code" id="time-display">0:00 / {duration_str}</span>
      </div>

      <div class="progress-track" id="progress-track">
        <div class="progress-bar" id="progress-bar"></div>
      </div>

      <div style="font-size: 18px; color: #64748b; font-weight: 600;">
        1080p Master Video
      </div>
    </footer>

    <audio id="audio" src="{audio_file}" preload="auto"></audio>
  </div>

  <script>
    const scenesData = {scenes_json};
    const audio = document.getElementById('audio');
    const btnPlay = document.getElementById('btn-play');
    const timeDisplay = document.getElementById('time-display');
    const progressBar = document.getElementById('progress-bar');
    const progressTrack = document.getElementById('progress-track');
    const sceneElements = document.querySelectorAll('.scene-card');

    function formatTime(s) {{
      const m = Math.floor(s / 60);
      const sec = Math.floor(s % 60);
      return `${{m}}:${{sec < 10 ? '0' : ''}}${{sec}}`;
    }}

    function updateScene(currentTime) {{
      scenesData.forEach((s, idx) => {{
        const el = document.getElementById(`scene-${{idx}}`);
        if (currentTime >= s.time_start && currentTime < s.time_end) {{
          if (!el.classList.contains('active')) {{
            sceneElements.forEach(item => item.classList.remove('active'));
            el.classList.add('active');
            gsap.fromTo(el, {{ opacity: 0, y: 30, scale: 0.96 }}, {{ opacity: 1, y: 0, scale: 1, duration: 0.6, ease: "power3.out" }});
          }}
        }}
      }});
    }}

    audio.ontimeupdate = () => {{
      const cur = audio.currentTime;
      const dur = audio.duration || {duration_sec};
      timeDisplay.innerText = `${{formatTime(cur)}} / ${{formatTime(dur)}}`;
      progressBar.style.width = `${{(cur / dur) * 100}}%`;
      updateScene(cur);
    }};

    btnPlay.onclick = () => {{
      if (audio.paused) {{
        audio.play();
        btnPlay.innerText = '⏸';
      }} else {{
        audio.pause();
        btnPlay.innerText = '▶';
      }}
    }};

    progressTrack.onclick = (e) => {{
      const rect = progressTrack.getBoundingClientRect();
      const clickX = e.clientX - rect.left;
      const pct = clickX / rect.width;
      audio.currentTime = pct * (audio.duration || {duration_sec});
    }};

    audio.onended = () => {{
      btnPlay.innerText = '▶';
    }};

    // Init first scene
    updateScene(0);
  </script>
</body>
</html>
"""

def render_scene_html(scene, index):
    visual_type = scene.get("visual_type")
    content_html = ""

    if visual_type == "hero_intro":
        cards_html = "".join([f"""
            <div class="feature-card">
              <div class="feature-icon">{c['icon']}</div>
              <div class="feature-title">{c['title']}</div>
              <div class="feature-desc">{c['desc']}</div>
            </div>
        """ for c in scene.get("cards", [])])
        content_html = f'<div class="grid-3">{cards_html}</div>'

    elif visual_type == "comparison":
        left = scene["left_card"]
        right = scene["right_card"]
        content_html = f"""
            <div class="grid-3" style="grid-template-columns: 1fr 1fr; max-width: 1200px;">
              <div class="feature-card" style="border-color: rgba(239, 68, 68, 0.3);">
                <div class="scene-pill" style="background: rgba(239, 68, 68, 0.15); border-color: rgba(239, 68, 68, 0.4); color: #fca5a5;">{left['badge']}</div>
                <div style="text-align: left; margin-top: 10px; font-size: 22px; line-height: 2;">
                  {"".join([f'<div>❌ {p}</div>' for p in left['points']])}
                </div>
              </div>
              <div class="feature-card" style="border-color: rgba(99, 102, 241, 0.6); box-shadow: 0 0 35px rgba(99, 102, 241, 0.25);">
                <div class="scene-pill" style="background: rgba(99, 102, 241, 0.25); border-color: rgba(99, 102, 241, 0.6); color: #c7d2fe;">{right['badge']}</div>
                <div style="text-align: left; margin-top: 10px; font-size: 22px; line-height: 2;">
                  {"".join([f'<div>⚡ {p}</div>' for p in right['points']])}
                </div>
              </div>
            </div>
        """

    elif visual_type == "stats":
        content_html = f"""
            <div class="stat-box">
              <div class="stat-big">{scene['stat_number']}</div>
              <div class="stat-text">{scene['stat_label']}</div>
              <div style="margin-top: 20px; font-size: 20px; color: #94a3b8;">{scene.get('note', '')}</div>
            </div>
        """

    elif visual_type == "workflow_flow":
        flow_html = "".join([f"""
            <div class="feature-card" style="padding: 24px 20px;">
              <div style="font-size: 32px; font-weight: 900; color: #38bdf8; margin-bottom: 8px;">Krok {f['step']}</div>
              <div class="feature-title" style="font-size: 22px;">{f['title']}</div>
              <div class="feature-desc" style="font-size: 17px;">{f['desc']}</div>
            </div>
        """ for f in scene.get("flow", [])])
        content_html = f'<div class="grid-3" style="grid-template-columns: repeat(4, 1fr);">{flow_html}</div>'

    elif visual_type == "specialist_grid":
        specs = scene.get("specialists", [])
        specs_html = "".join([f"""
            <div class="feature-card" style="padding: 24px 18px;">
              <div class="feature-icon" style="font-size: 36px; margin-bottom: 8px;">{s['icon']}</div>
              <div class="feature-title" style="font-size: 20px;">{s['name']}</div>
              <div class="feature-desc" style="font-size: 16px;">{s['role']}</div>
            </div>
        """ for s in specs])
        content_html = f'<div class="grid-3" style="grid-template-columns: repeat(5, 1fr);">{specs_html}</div>'

    elif visual_type == "security_zones":
        zones_html = "".join([f"""
            <div class="feature-card" style="border-color: {z['color']}; box-shadow: 0 10px 30px {z['color']}33;">
              <div style="font-size: 24px; font-weight: 800; color: {z['color']}; margin-bottom: 12px;">{z['level']}</div>
              <div style="font-size: 24px; font-weight: 600; color: #fff;">{z['question']}</div>
            </div>
        """ for z in scene.get("zones", [])])
        content_html = f'<div class="grid-3">{zones_html}</div>'

    elif visual_type == "nine_steps":
        steps = scene.get("steps", [])
        steps_col1 = steps[:5]
        steps_col2 = steps[5:]
        content_html = f"""
            <div class="grid-3" style="grid-template-columns: 1fr 1fr; max-width: 1200px; text-align: left;">
              <div class="feature-card" style="text-align: left; font-size: 20px; line-height: 2;">
                {"".join([f'<div>🔹 {s}</div>' for s in steps_col1])}
              </div>
              <div class="feature-card" style="text-align: left; font-size: 20px; line-height: 2;">
                {"".join([f'<div>🔹 {s}</div>' for s in steps_col2])}
              </div>
            </div>
        """

    elif visual_type == "tools_connect":
        tools_html = "".join([f"""
            <div class="feature-card" style="border-top: 4px solid {t['color']};">
              <div class="feature-title">{t['name']}</div>
              <div class="feature-desc">{t['desc']}</div>
            </div>
        """ for t in scene.get("tools", [])])
        content_html = f'<div class="grid-3">{tools_html}</div>'

    elif visual_type == "routines_list":
        routines_html = "".join([f"""
            <div class="feature-card" style="display: flex; align-items: center; gap: 20px; text-align: left; padding: 24px 30px;">
              <div style="font-size: 40px;">{r['icon']}</div>
              <div>
                <div style="font-size: 22px; font-weight: 800; color: #38bdf8;">{r['time']}</div>
                <div style="font-size: 20px; color: #e2e8f0; margin-top: 4px;">{r['action']}</div>
              </div>
            </div>
        """ for r in scene.get("routines", [])])
        content_html = f'<div style="display: flex; flex-direction: column; gap: 20px; width: 100%; max-width: 1000px;">{routines_html}</div>'

    elif visual_type == "quote_highlight" or visual_type == "insight_card" or visual_type == "golden_rule":
        text = scene.get("quote") or scene.get("insight") or scene.get("advice")
        content_html = f'<div class="quote-box">💡 {text}</div>'

    elif visual_type == "author_outro":
        content_html = f"""
            <div class="stat-box" style="padding: 40px 60px;">
              <div style="font-size: 32px; font-weight: 800; color: #fff;">{scene.get('thanks', 'Ďakujem!')}</div>
              <div style="font-size: 24px; color: #38bdf8; margin-top: 10px;">Lektor: {scene.get('outro_author')}</div>
              <div style="font-size: 20px; color: #94a3b8; margin-top: 15px;">Email: <strong>{scene.get('contact')}</strong></div>
            </div>
        """

    else:
        content_html = f'<div class="quote-box">{scene.get("subheading", "")}</div>'

    return f"""
      <div class="scene-card" id="scene-{index}">
        <div class="scene-pill">{scene.get('badge', 'Lekcia')}</div>
        <h2 class="scene-heading">{scene.get('heading', '')}</h2>
        <p class="scene-subheading">{scene.get('subheading', '')}</p>
        {content_html}
      </div>
    """

def main():
    base_dir = os.path.join(os.getcwd(), "course_grok_bot", "videos")
    os.makedirs(base_dir, exist_ok=True)

    print("\n=======================================================")
    print("🎬 GENEROVANIE ANIMOVANÝCH VIDEO LEKCIÍ PRE GROK BOT")
    print("=======================================================\n")

    for lesson in LESSONS_DATA:
        lesson_id = lesson["id"]
        folder = os.path.join(base_dir, f"lesson_{lesson_id:02d}")
        os.makedirs(folder, exist_ok=True)

        scenes_rendered = "\n".join([render_scene_html(s, i) for i, s in enumerate(lesson["scenes"])])

        m = int(lesson["duration"] // 60)
        s = int(lesson["duration"] % 60)
        dur_str = f"{m}:{s:02d}"

        html_content = HTML_TEMPLATE.format(
            lesson_id=lesson_id,
            lesson_title=lesson["title"],
            duration_str=dur_str,
            duration_sec=lesson["duration"],
            audio_file=lesson["audio_file"],
            rendered_scenes=scenes_rendered,
            scenes_json=json.dumps(lesson["scenes"], ensure_ascii=False)
        )

        out_file = os.path.join(folder, "index.html")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(html_content)

        print(f"✅ Lekcia {lesson_id:02d}: Vytvorené video v {out_file}")

    print("\n=======================================================")
    print("✨ VŠETKÝCH 6 VIDEO LEKCIÍ JE PRIPRAVENÝCH!")
    print("=======================================================\n")

if __name__ == "__main__":
    main()
