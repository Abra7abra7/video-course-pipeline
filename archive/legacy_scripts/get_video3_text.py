import json
from youtube_transcript_api import YouTubeTranscriptApi

try:
    ytt = YouTubeTranscriptApi()
    fetched = ytt.fetch("ijlkO_U1grY")
    raw = [{'text': item.text, 'start': item.start, 'duration': item.duration} for item in fetched]
    with open('video3_transcript.json', 'w', encoding='utf-8') as f:
        json.dump(raw, f, ensure_ascii=False, indent=2)
    print(f"Transcript fetched: {len(raw)} items.")
except Exception as e:
    print("Transcript fetch error:", e)

with open('video3_transcript.json', 'r', encoding='utf-8') as f:
    snippets = json.load(f)

text = " ".join([s['text'] for s in snippets])
with open('video3_text.txt', 'w', encoding='utf-8') as f:
    f.write(text)
print("Transcript text saved. Total characters:", len(text))
