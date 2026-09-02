import json
import os
from youtube_transcript_api import YouTubeTranscriptApi
import yt_dlp

video_id = "Y43T7VQGtOs"
url = f"https://www.youtube.com/watch?v={video_id}"

ydl_opts = {
    'skip_download': True,
    'getcomments': True,
    'extractor_args': {'youtube': {'max_comments': ['20', 'all', '10', '0']}}
}

print(f"Fetching metadata for {video_id}...")
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(url, download=False)

title = info.get('title')
uploader = info.get('uploader')
duration = info.get('duration')
description = info.get('description', '')
chapters = info.get('chapters', [])
comments = info.get('comments', [])

with open('video2_info.json', 'w', encoding='utf-8') as f:
    json.dump({
        'id': video_id,
        'title': title,
        'uploader': uploader,
        'duration': duration,
        'description': description,
        'chapters': chapters,
        'comments': comments
    }, f, ensure_ascii=False, indent=2)

print(f"Title: {title}")
print(f"Uploader: {uploader}")
print(f"Duration: {duration}s")
print(f"Chapters count: {len(chapters)}")

try:
    ytt = YouTubeTranscriptApi()
    fetched = ytt.fetch(video_id)
    raw = [{'text': item.text, 'start': item.start, 'duration': item.duration} for item in fetched]
    with open('video2_transcript.json', 'w', encoding='utf-8') as f:
        json.dump(raw, f, ensure_ascii=False, indent=2)
    print(f"Fetched {len(raw)} transcript snippets.")
except Exception as e:
    print(f"Transcript error: {e}")
