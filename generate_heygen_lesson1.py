import os
import sys
import time
import requests
from dotenv import load_dotenv

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

load_dotenv()

API_KEY = os.getenv("HEYGEN_API_KEY")
# Využijeme tvojho avatara "Marian Stancik"
AVATAR_ID = "647a256e6dc74e93aba9e53bba326ce3"

headers = {
    "X-Api-Key": API_KEY,
    "accept": "application/json"
}

def upload_audio_to_heygen(file_path):
    print(f"📤 Nahrávam audio do HeyGen: {file_path}")
    url = "https://upload.heygen.com/v1/asset"
    headers_upload = {
        "X-Api-Key": API_KEY,
        "Content-Type": "audio/mpeg"
    }
    with open(file_path, "rb") as f:
        resp = requests.post(url, headers=headers_upload, data=f)
    
    if resp.status_code == 200:
        asset_id = resp.json().get("data", {}).get("asset_id") or resp.json().get("data", {}).get("id")
        print(f"✅ Audio úspešne nahraté! Asset ID: {asset_id}")
        return asset_id
    else:
        print(f"❌ Chyba pri nahrávaní audia: {resp.status_code} - {resp.text}")
        return None

def generate_avatar_video(audio_asset_id, output_mp4, test_title="Lekcia 1 Avatar"):
    print(f"🎬 Spúšťam generovanie HeyGen avatara pre {test_title}...")
    url = "https://api.heygen.com/v2/video/generate"
    
    payload = {
        "video_inputs": [
            {
                "character": {
                    "type": "avatar",
                    "avatar_id": AVATAR_ID,
                    "avatar_style": "normal"
                },
                "voice": {
                    "type": "audio",
                    "audio_asset_id": audio_asset_id
                },
                "background": {
                    "type": "color",
                    "value": "#000000"
                }
            }
        ],
        "dimension": {
            "width": 720,
            "height": 720
        },
        "test": False
    }

    resp = requests.post(url, headers=headers, json=payload)
    if resp.status_code != 200:
        print(f"❌ Chyba pri generovaní videa: {resp.status_code} - {resp.text}")
        return None

    video_id = resp.json().get("data", {}).get("video_id")
    print(f"🚀 Video zaradené do fronty v HeyGen! Video ID: {video_id}")
    print("⏳ Čakám na vyrenderovanie videa (status polling)...")

    # Poll status
    status_url = f"https://api.heygen.com/v1/video_status.get?video_id={video_id}"
    for attempt in range(60):
        time.sleep(10)
        s_resp = requests.get(status_url, headers=headers)
        if s_resp.status_code == 200:
            s_data = s_resp.json().get("data", {})
            status = s_data.get("status")
            print(f"Status [{attempt+1}/60]: {status}")
            if status == "completed":
                video_url = s_data.get("video_url")
                print(f"🎉 HeyGen video hotové! URL: {video_url}")
                # Stiahnuť video
                v_content = requests.get(video_url).content
                os.makedirs(os.path.dirname(output_mp4), exist_ok=True)
                with open(output_mp4, "wb") as f:
                    f.write(v_content)
                print(f"💾 Video uložené do: {output_mp4}")
                return output_mp4
            elif status == "failed":
                print(f"❌ Renderovanie zlyhalo: {s_data.get('error')}")
                return None
        else:
            print(f"⚠️ Chyba pri kontrole statusu: {s_resp.status_code}")

    return None

if __name__ == "__main__":
    audio_path = "course_grok_bot/audio/lekcia_01_co_je_grok_bot.mp3"
    out_video = "course_grok_bot/assets/avatar_lesson_01.mp4"
    
    asset_id = upload_audio_to_heygen(audio_path)
    if asset_id:
        generate_avatar_video(asset_id, out_video)
