import json
import yt_dlp
from youtube_transcript_api import YouTubeTranscriptApi

video_id = "ijlkO_U1grY"
url = f"https://www.youtube.com/watch?v={video_id}"

ydl_opts = {'skip_download': True}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(url, download=False)
    title = info.get('title')
    uploader = info.get('uploader')
    duration = info.get('duration')
    description = info.get('description', '')
    chapters = info.get('chapters', [])

print(f"Title: {title}")
print(f"Uploader: {uploader}")
print(f"Duration: {duration}s")
print(f"Chapters: {chapters}")
print(f"Description snippet:\n{description[:500]}")

try:
    ytt = YouTubeTranscriptApi()
    fetched = ytt.fetch(video_id)
    raw = [{'text': item.text, 'start': item.start, 'duration': item.duration} for item in fetched]
    with open('video3_transcript.json', 'w', encoding='utf-8') as f:
        json.dump(raw, f, ensure_ascii=False, indent=2)
    print(f"Fetched {len(raw)} transcript entries.")
except Exception as e:
    print(f"Transcript error: {e}")
