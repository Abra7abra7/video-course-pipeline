# 🤖 AGENTS.md — Master Dokumentácia & Brand Manuál Automatickej Video Fabriky

Vitaj v hlavnej dokumentácii automatizovanej fabriky na tvorbu kurzov, interaktívnych aplikácií a multi-platformových videí (YouTube, TikTok, Reels, Shorts, Instagram, LinkedIn).

Tento dokument slúži ako **kompletný referenčný sprievodca**, architektonický manuál a návod na customizáciu celého systému.

---

## 📑 Obsah

1. [Architektúra Systému & End-to-End Workflow](#1-architektúra-systému--end-to-end-workflow)
2. [Ako Boli Vytvorené Kurzy (Grok Bot & Grok 2)](#2-ako-boli-vytvorené-kurzy-grok-bot--grok-2)
3. [Sprievodca Customizáciou (Brand Manual & Dizajn)](#3-sprievodca-customizáciou-brand-manual--dizajn)
   - [Vizuálne Efekty & Animácie](#a-vizuálne-efekty--animácie)
   - [Farebná Paleta & Pozadia](#b-farebná-paleta--pozadia)
   - [Typografia & Písma](#c-typografia--písma)
   - [Flowcharty, Karty a Diagramy](#d-flowcharty-karty-a-diagramy)
   - [Hovoriaci AI Avatar & HeyGen Nastavenia](#e-hovoriaci-ai-avatar--heygen-nastavenia)
4. [Multi-Platformová Export Pipeline (YouTube, TikTok, Instagram)](#4-multi-platformová-export-pipeline-youtube-tiktok-instagram)
5. [Prehľad Súborov v Repozitári](#5-prehľad-súborov-v-repozitári)

---

## 1. Architektúra Systému & End-to-End Workflow

Celý proces tvorby kurzu alebo videa je 100% programovateľný a prebieha v 4 fázach:

```
┌────────────────────────────────────────────────────────┐
│ 1. SCENÁR & OSNOVA (Text / Markdown / JSON)            │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│ 2. AI DABING (ElevenLabs REST API / voice_engine.py)   │
│    ↳ Vlastný naklonovaný hlas (Voice ID)               │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│ 3. DYNAMICKÝ SCENE ENGINE & HOVORIACI AVATAR           │
│    ↳ Real-time web video / GSAP časové značky          │
│    ↳ HeyGen video digital twin (150px kruhový výrez)   │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│ 4. INTERAKTÍVNY PORTÁL & MULTI-EXPORT (pipeline.py)    │
│    ↳ Webový prehrávač (localhost:8080)                 │
│    ↳ 16:9 Landscape (YouTube / LMS)                    │
│    ↳ 9:16 Vertical (TikTok / Reels / Shorts)           │
│    ↳ 1:1 Square (Instagram / LinkedIn Feed)           │
└────────────────────────────────────────────────────────┘
```

---

## 2. Ako Boli Vytvorené Kurzy (Grok Bot & Grok 2)

V repozitári máme 2 plnohodnotné referenčné kurzy:

### A. Kurz 1: Grok Bot AI Agent Tím (`course_grok_bot/`)
- **Téma:** Praktický návod podľa workshopu Lauren Tan (SpaceX AI) o nasadení Chief of Staff agenta a 5 špecialistov.
- **Komponenty:**
  - `course_grok_bot/audio/` – 6 MP3 súborov vygenerovaných cez ElevenLabs + `full_course_grok_bot.mp3`.
  - `course_grok_bot/assets/` – `heygen_avatar.mp4` a portrét.
  - `course_grok_bot/index.html` – Webový kurzový portál so synchrónnym prepínaním scén.

### B. Kurz 2: Grok 2 & Multi-Agent Architektúra (`course_grok2/`)
- **Téma:** Hĺbkový technický rozbor (Dual-Brain Kernel, Tool Execution Bus, AST Parser, Swarm P2P Protocol, Zero-Trust RBAC).
- **Extra komponenty:**
  - **Interaktívny Architektonický Inšpektor** – Klikateľné moduly s reálnym JSON-RPC a Python AST kódmi.
  - **Web Audio spektrálny analyzátor** pre animovanú svetelnú auru okolo avatara.

---

## 3. Sprievodca Customizáciou (Brand Manual & Dizajn)

Všetky vizuálne parametre sú centralizované v CSS premenných a HTML/JS štruktúre.

### a) Vizuálne Efekty & Animácie
- **Svetelná aura okolo avatara (`.avatar-glow-ring`):**
  ```css
  background: radial-gradient(circle, var(--primary) 0%, var(--accent-cyan) 60%, transparent 80%);
  filter: blur(10px);
  ```
- **Live pulzujúci ekvalizér (`.audio-equalizer .eq-bar`):**
  - V reálnom čase reaguje na hlasitosť reči pomocou matematickej sínusoidy a Web Audio API.
- **Plynulé prechody scén (`.scene-view`):**
  - Využívajú moderný cubic-bezier prechod: `transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);`

### b) Farebná Paleta & Pozadia
Všetky farby sú definované v `:root`:
```css
:root {
  --bg-dark: #04060a;          /* Hlboké vesmírne tmavé pozadie */
  --bg-surface: #0b0f19;       /* Povrch kariet a modulov */
  --bg-card: rgba(15, 21, 35, 0.85); /* Glassmorphism karty */
  --primary: #6366f1;          /* Hlavná Indigo farba brandu */
  --primary-glow: rgba(99, 102, 241, 0.45);
  --accent-cyan: #06b6d4;      /* Cyberpunk tyrkysová pre dáta a highlighty */
  --accent-green: #10b981;     /* Zelená pre úspech a aktívny status */
  --accent-amber: #f59e0b;     /* Oranžová pre upozornenia */
  --accent-red: #ef4444;       /* Červená pre chyby a kritické zóny */
}
```

### c) Typografia & Písma
Projekt používa prémiové Google Fonts:
1. **`Plus Jakarta Sans`** – Hlavné čitateľné písmo pre UI, popisy a odseky.
2. **`Outfit`** – Geometrické, výrazné písmo pre hlavné nadpisy lekcií (`.scene-title`).
3. **`JetBrains Mono`** – Monospace písmo pre čísla, časové kódy a technický inšpektor.

### d) Flowcharty, Karty a Diagramy
V JavaScriptovom poli `LESSONS` môžete pre každú scénu definovať rôzne typy vizuálov:
- **Karty (`boxes`):** Ikona, nadpis a stručný popis (automaticky sa usporiadajú do mriežky).
- **Veľká štatistika (`heroStat`):** Zvýraznené veľké číslo (`90%`, `10x`, `24/7`) s popisom.
- **Bezpečnostné zóny:** 🟢 Zelená (čítanie), 🟡 Oranžová (draft), 🔴 Červená (schválenie človekom).

### e) Hovoriaci AI Avatar & HeyGen Nastavenia
Avatar beží v pravom dolnom rohu (`.avatar-bubble-widget`):
- **Rozmer kruhu:** `150px × 150px`, `border-radius: 50%`, s neónovým orámovaním.
- **Zdroj videa:** `assets/heygen_avatar.mp4` (náhľad: `assets/heygen_avatar.jpg`).
- **Ako zmeniť avatara:**
  1. Ak chcete nového avatara z HeyGen, vložte nové MP4 video do `course_grok2/assets/heygen_avatar.mp4`.
  2. Spustite synchronizáciu: `python pipeline.py --action sync-avatar --target course_grok2`.

---

## 4. Multi-Platformová Export Pipeline (YouTube, TikTok, Instagram)

Všetky exporty sú zjednotené v skripte **`pipeline.py`**.

### Príkazy:

#### 1. Multi-Export existujúceho videa pre všetky sociálne siete:
```bash
python pipeline.py --action export --input exports/1_tiktok_reels_shorts_9x16.mp4 --name hermes_promo
```
Vygeneruje 3 súbory do priečinka `exports/`:
- `exports/hermes_promo_16x9.mp4` (YouTube / Monitor / Web)
- `exports/hermes_promo_9x16.mp4` (TikTok / Reels / Shorts s rozostreným pozadím)
- `exports/hermes_promo_1x1.mp4` (Instagram / LinkedIn Feed)

#### 2. Vygenerovanie nového hlasu cez ElevenLabs:
```bash
python pipeline.py --action voice --text "Vitajte v novej lekcii nášho kurzu." --name nova_lekcia
```

#### 3. Spustenie lokálneho servera pre náhľad kurzov:
```bash
python -m http.server 8080
```
- Kurz Grok 2: [http://localhost:8080/course_grok2/](http://localhost:8080/course_grok2/)
- Kurz Grok Bot: [http://localhost:8080/course_grok_bot/](http://localhost:8080/course_grok_bot/)

---

## 5. Prehľad Súborov v Repozitári

```
youtube-to-markdown/
├── .env                                  # API kľúče (ElevenLabs, HeyGen)
├── AGENTS.md                             # Tento master manuál a šablóna
├── pipeline.py                           # Hlavná zjednotená pipeline pre exporty a tvorbu
├── voice_engine.py                       # Core hlasový generátor (ElevenLabs REST API)
│
├── course_grok2/                         # 🎓 Pokročilý kurz Grok 2 (Deep-Dive Architektúra)
│   ├── index.html                        # Interaktívny webový portál s HeyGen avatarom
│   ├── KURZ_GROK2_ARCHITEKTURA.md        # Kompletný sylabus lekcií
│   ├── assets/                           # heygen_avatar.mp4, heygen_avatar.jpg
│   └── audio/                            # Vygenerované lekcie MP3 + full master track
│
├── course_grok_bot/                      # 🎓 Kurz Grok Bot (AI Agent Tím)
│   ├── index.html                        # Webový prehrávač s HeyGen avatarom
│   ├── KURZ_GROK_BOT.md                  # Kompletný skript lekcií
│   ├── assets/                           # heygen_avatar.mp4, user_avatar.jpg
│   └── audio/                            # MP3 lekcie 1 až 6 + full track
│
├── exports/                              # 🎬 Vyrenderované MP4 videá pre sociálne siete
│   ├── 1_tiktok_reels_shorts_9x16.mp4
│   ├── 2_youtube_linkedin_twitter_16x9.mp4
│   └── 3_instagram_linkedin_feed_1x1.mp4
│
├── assets/                               # Globálne grafické podklady a fotka avatara
└── archive/                              # Bezpečne archivované jednorazové skripty a dáta
```

---

*Tento systém je navrhnutý ako modulárna, škálovateľná a plne programovateľná fabrika na AI obsah.*
