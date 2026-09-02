import shutil
import os

src = r"C:\Users\mstancik\.gemini\antigravity-ide\brain\fc31706c-be20-4f0f-b924-713da2fc26ae\.user_uploaded\media_1787743071313.jpg"

targets = [
    r"c:\Users\mstancik\Desktop\projekty_a_vyvoj\youtube-to-markdown\assets\user_avatar.jpg",
    r"c:\Users\mstancik\Desktop\projekty_a_vyvoj\youtube-to-markdown\hermes-viral-video\assets\user_avatar.jpg",
    r"c:\Users\mstancik\Desktop\projekty_a_vyvoj\youtube-to-markdown\hermes-architecture-video\assets\user_avatar.jpg",
    r"c:\Users\mstancik\Desktop\projekty_a_vyvoj\youtube-to-markdown\apodex-goldie-video\assets\user_avatar.jpg",
    r"c:\Users\mstancik\Desktop\projekty_a_vyvoj\youtube-to-markdown\doac-kisin-video\assets\user_avatar.jpg"
]

for t in targets:
    os.makedirs(os.path.dirname(t), exist_ok=True)
    shutil.copyfile(src, t)
    print(f"Copied avatar to {t} ({os.path.getsize(t)} bytes)")
