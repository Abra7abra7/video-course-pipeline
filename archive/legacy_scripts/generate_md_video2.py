import json

with open('video2_info.json', 'r', encoding='utf-8') as f:
    info = json.load(f)

with open('video2_transcript.json', 'r', encoding='utf-8') as f:
    snippets = json.load(f)

title = info['title']
video_id = info['id']
url = f"https://www.youtube.com/watch?v={video_id}"
channel = info['uploader']
duration_s = info['duration']
mins = int(duration_s // 60)
secs = int(duration_s % 60)

# Format transcript with timestamps
formatted_transcript = []
curr_chunk = []
curr_start = 0

for s in snippets:
    if not curr_chunk:
        curr_start = s['start']
    curr_chunk.append(s['text'].strip())
    if s['start'] - curr_start >= 30 or (len(' '.join(curr_chunk)) > 300 and s['text'].endswith(('.', '?', '!'))):
        m = int(curr_start // 60)
        sec = int(curr_start % 60)
        formatted_transcript.append(f"[{m:02d}:{sec:02d}] " + " ".join(curr_chunk))
        curr_chunk = []

if curr_chunk:
    m = int(curr_start // 60)
    sec = int(curr_start % 60)
    formatted_transcript.append(f"[{m:02d}:{sec:02d}] " + " ".join(curr_chunk))

# Write transcript file
transcript_content = f"""# YouTube Transcript: {title}

- **Video ID**: `{video_id}`
- **URL**: [{url}]({url})
- **Kanál**: {channel}
- **Dĺžka**: {mins}:{secs:02d} (1h 34m)
- **Dátum**: 2026

---

## Časové kapitoly (Chapters)
"""
for ch in info.get('chapters', []):
    st = ch['start_time']
    ch_m = int(st // 60)
    ch_s = int(st % 60)
    transcript_content += f"- `{ch_m:02d}:{ch_s:02d}` - {ch['title']}\n"

transcript_content += "\n---\n\n## Kompletný prepis (Transcript)\n\n" + "\n\n".join(formatted_transcript)

with open(f"youtube - {title.replace(':', ' -').replace('!', '')} - transcript ({video_id}).md", "w", encoding="utf-8") as f:
    f.write(transcript_content)

# Write Summary File
summary_content = f"""# YouTube: {title}

- **Video ID**: `{video_id}`
- **URL**: [{url}]({url})
- **Kanál**: {channel}
- **Dĺžka**: {mins}:{secs:02d} (1h 34m)
- **Kategória**: Geopolitika, AI, Ekonómia a Budúcnosť Spoločnosti (Deep Interview)

---

## 📌 Rýchle zhrnutie (TL;DR)
V tejto mimoriadne silnej epizóde podcastu *The Diary Of A CEO* diskutujú Steven Bartlett, Konstantin Kisin a ekonóm Steve Keen o kritickom bode západnej civilizácie. Rozoberajú stratu dôvery v politických lídrov, energetickú a klimatickú realitu, hrozbu masovej nezamestnanosti spôsobenej umelou inteligenciou a porovnávajú západný model s autoritárskou Čínou. Hlavné posolstvo: nachádzame sa v období tektonických zmien a jednotlivci sa musia pripraviť na adaptáciu, psychickú odolnosť a budovanie skutočných zručností.

---

## 🎯 4 Kľúčové Piliere Rozhovoru

### 1. Zlyhanie lídrov a riziko spoločenských nepokojov
- Západné inštitúcie strácajú legitimitu kvôli neplneniu sľubov a odtrhnutiu od reality bežných ľudí.
- Polarizácia, inflácia a rozpad strednej triedy vytvárajú podmienky pre občiansky nepokoj a radikalizáciu.

### 2. Umelá inteligencia (AI) a trh práce
- Nastáva bezprecedentná automatizácia kognitívnych aj manuálnych úloh.
- Metafora "V najlepšom prípade domáci miláčik, v najhoršom krava" ilustruje riziko straty ľudskej autonómie v technologickom svete, ak nedôjde k zodpovednej regulácii a vzdelaniu.

### 3. Geopolitika: Západ vs. Čína a lekcie zo Sovietskeho zväzu
- Konstantin Kisin spomína na svoje detstvo v ZSSR a varuje pred ideologickým dogmatizmom.
- Čínsky model pragmatického technologického štátu predstavuje zásadnú konkurenčnú výzvu pre západné demokracie.

### 4. Ako prežiť a prosperovať v novom svete
- Zamerať sa na veci pod vlastnou kontrolou (zdravie, rodina, lokálna komunita, kritické myslenie).
- Neustále celoživotné vzdelávanie a flexibilita v kariére namiesto spoliehania sa na štátne garancie.
"""

with open(f"youtube - {title.replace(':', ' -').replace('!', '')} ({video_id}).md", "w", encoding="utf-8") as f:
    f.write(summary_content)

print("Markdown summary and transcript files written successfully!")
