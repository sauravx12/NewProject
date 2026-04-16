from supadata import Supadata
import os
supadata = Supadata(api_key="sd_3657bac9e07a162981cec64c1fb6149d")

transcript = supadata.transcript(url="https://www.youtube.com/watch?v=mB0QuXEv_sg")
full_text = " ".join([chunk.text for chunk in transcript.content])

folder = "youtube_transcripts"
os.makedirs(folder, exist_ok=True)

video_id = url.split("v=")[-1]
file_path = os.path.join(folder, f"{video_id}.txt")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(full_text)

print(f"Transcript saved at: {file_path}")