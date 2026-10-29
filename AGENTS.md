# AGENTS.md — Video Course Pipeline

Instructions for any coding agent (Jules, OpenCode, Hermes, Grok Bot, Claude, Codex, …). Read the **Agent quick guide** first; the detailed Slovak manual follows below it.

## Agent quick guide

### Project

- **Purpose:** Marián Stančík's automated "video factory" — course portals, AI voice-over (ElevenLabs), HeyGen avatar, and multi-format exports (16:9, 9:16, 1:1) for YouTube, TikTok, Reels, Instagram and LinkedIn.
- **Owner:** Marián Stančík (GitHub `Abra7abra7`). Content is published on his own channels; client videos (e.g. `apodex-goldie-video/`) belong to the respective client. TODO: confirm client ownership per video folder.
- **No hosting / no preview deploy** — outputs are local files.

### Stack

- Python 3 scripts (`pipeline.py`, `voice_engine.py`, `generate_*.py`, `render_course_videos.py`, `export_all_platforms.py`, `build_animated_lessons.py`). No `requirements.txt` — TODO: confirm Python dependencies (and ffmpeg for exports).
- Node: root `package.json` only has `puppeteer-core` (used by `capture_scenes.mjs`).
- Each `*-video/` folder is a **HyperFrames** project with its own `AGENTS.md`/`CLAUDE.md` — follow those inside that folder.

### Commands

```bash
python pipeline.py --action export --input <video.mp4> --name <name>   # 16:9 + 9:16 + 1:1 into exports/
python pipeline.py --action voice --text "<text>" --name <name>        # ElevenLabs voice-over (paid API!)
python pipeline.py --action sync-avatar --target course_grok2          # copy HeyGen avatar into a course
python -m http.server 8080                                             # preview course portals locally
# inside a HyperFrames folder, e.g. hermes-viral-video/:
npm run dev | npm run check | npm run render
```

There is **no test suite**. Minimum check: the script you touched runs on a small sample, `npm run check` passes in any HyperFrames folder you changed, and the course portal loads locally.

### Structure

```
pipeline.py, voice_engine.py, *.py     # pipeline scripts
course_grok_bot/, course_grok2/        # finished course portals (index.html, audio/, videos/)
*-video/                               # HyperFrames video projects (one per video)
exports/                               # rendered MP4s
archive/                               # legacy one-off scripts and data — read-only
brand_config.json                      # brand settings
.agents/skills/                        # hyperframes-cli, youtube-to-markdown skills
```

### Conventions & project-specific rules

- Content and docs are **Slovak**; code identifiers English.
- **Paid APIs (ElevenLabs, HeyGen):** do not generate voice/avatar output without explicit approval; env var names: `ELEVENLABS_API_KEY`, `ELEVENLABS_VOICE_ID`, `HEYGEN_API_KEY` (in `.env`, git-ignored).
- Do not commit new large media (MP4/MP3/WAV renders) unless the task asks for it; never commit `__pycache__/` or `.pyc`.
- Respect copyright of third-party source videos/transcripts; nothing is published without Marián's approval.

### Working rules (mandatory for every agent: Jules, OpenCode, Hermes, Grok Bot, Claude, Codex, …)

- **Branch + Pull Request only.** Create a feature branch (`feat/…`, `fix/…`, `docs/…`, `seo/…`), open a PR and wait for review. **Never push or force-push to `main`/the default branch** and never merge your own PR.
- **No secrets in git.** Never commit `.env*`, API keys, tokens, passwords, private keys, server IP addresses, SSH details or personal data. Use the hosting platform's environment variables; reference variables by **name only**. If you find a secret in the repo, stop and report it — do not copy it anywhere.
- **GDPR / privacy first.** Treat any personal data (leads, customers, patients, form submissions) as confidential. No new trackers, cookies, analytics, third-party scripts or data processors without explicit approval; keep privacy/cookie pages consistent with what the code actually does.
- **The client owns the domain, the content and the data.** Do not change DNS, domains, hosting settings, payment settings, legal texts or published client content without explicit approval.
- **No destructive changes without approval.** No deleting pages/data/files in bulk, no history rewrites, no dependency major-version upgrades, no production deploys, no outgoing emails/posts from tests.
- **Invent nothing.** If a fact (price, company detail, legal statement, metric) is not in the repo or the task, leave a `TODO: confirm` instead of guessing.
- **Small, focused diffs.** Reuse existing patterns and dependencies; do not add a new dependency if an existing one covers the need.

### Definition of Done

1. The changed scripts/projects run on a sample (see *Commands*); HyperFrames `npm run check` passes where relevant.
2. No preview deploy exists for this repo — attach a short sample output description or screenshot in the PR instead.
3. The PR description contains a summary, what was run, and any `TODO: confirm` items.
4. Nothing is published until Marián approves (**ÁNO**) and merges the PR.

---

# Detailed manual (Slovak, original)

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
