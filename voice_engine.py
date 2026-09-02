import os
import sys
import asyncio
from dotenv import load_dotenv

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

load_dotenv()

def generate_voice(text: str, output_path: str, speed_pct: int = 6):
    """
    Vygeneruje hlasový komentár:
    - Ak je nastavený ELEVENLABS_API_KEY a ELEVENLABS_VOICE_ID, použije tvoj originálny hlas z ElevenLabs.
    - Ak kľúč ešte nie je nastavený, použije kvalitný slovenský hlas cez Edge-TTS ako bezplatný fallback.
    """
    eleven_key = os.getenv("ELEVENLABS_API_KEY", "").strip()
    voice_id = os.getenv("ELEVENLABS_VOICE_ID", "").strip()

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)

    if eleven_key and eleven_key != "your_elevenlabs_api_key_here" and voice_id and voice_id != "your_voice_id_here":
        try:
            print(f"🎙️ Generujem hlas cez ElevenLabs (Voice ID: {voice_id})...")
            import requests
            url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
            headers = {
                "xi-api-key": eleven_key,
                "Content-Type": "application/json"
            }
            payload = {
                "text": text,
                "model_id": "eleven_multilingual_v2",
                "voice_settings": {
                    "stability": 0.5,
                    "similarity_boost": 0.8,
                    "style": 0.0,
                    "use_speaker_boost": True
                }
            }
            response = requests.post(url, json=payload, headers=headers, timeout=120)
            if response.status_code == 200:
                with open(output_path, "wb") as f:
                    f.write(response.content)
                print(f"✅ Hlas z ElevenLabs úspešne vygenerovaný: {output_path}")
                return output_path
            else:
                print(f"⚠️ ElevenLabs API vrátilo chybu {response.status_code}: {response.text}")
        except Exception as e:
            print(f"⚠️ Chyba pri ElevenLabs, prepínam na lokálny fallback: {e}")

    # Fallback cez bezplatný Edge-TTS
    print("🎙️ Používam bezplatný slovenský neural hlas (Edge-TTS)...")
    import edge_tts
    async def _edge():
        voice = 'sk-SK-LukasNeural'
        rate = f"+{speed_pct}%"
        comm = edge_tts.Communicate(text, voice, rate=rate)
        await comm.save(output_path)
    asyncio.run(_edge())
    print(f"✅ Hlas úspešne vygenerovaný (Edge-TTS): {output_path}")
    return output_path

if __name__ == "__main__":
    test_text = "Toto je testovací slovenský hlas pre moju novú video fabriku."
    generate_voice(test_text, "assets/test_voice.mp3")
