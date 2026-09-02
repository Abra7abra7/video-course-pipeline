import json

with open('video2_info.json', 'r', encoding='utf-8') as f:
    info = json.load(f)

with open('video2_transcript.json', 'r', encoding='utf-8') as f:
    snippets = json.load(f)

chapters = info.get('chapters', [])
print("=== CHAPTERS ===")
for ch in chapters:
    st = ch['start_time']
    mins = int(st // 60)
    secs = int(st % 60)
    print(f"- [{mins:02d}:{secs:02d}] {ch['title']}")

print(f"\nTotal transcript length: {len(snippets)} snippets")
