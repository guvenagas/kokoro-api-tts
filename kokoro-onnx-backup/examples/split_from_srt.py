import os
import srt
import csv
import wave
import contextlib
from pydub import AudioSegment

# Config
audio_file = "lazziya1.wav"
srt_file = "lazziya1.srt"
output_dir = "segments"
metadata_file = "metadata.csv"

# Create output folder
os.makedirs(output_dir, exist_ok=True)

# Load audio
audio = AudioSegment.from_wav(audio_file)

# Load subtitles
with open(srt_file, "r", encoding="utf-8") as f:
    subs = list(srt.parse(f.read()))

# Create segments + metadata
with open(metadata_file, "w", newline="", encoding="utf-8-sig") as csvfile:
    writer = csv.writer(csvfile, delimiter="|")
    for i, sub in enumerate(subs, start=1):
        start_ms = int(sub.start.total_seconds() * 1000)
        end_ms = int(sub.end.total_seconds() * 1000)
        segment_audio = audio[start_ms:end_ms]
        
        filename = f"segment_{i:03}.wav"
        segment_path = os.path.join(output_dir, filename)
        segment_audio.export(segment_path, format="wav")

        # Write to metadata file
        writer.writerow([filename, sub.content.strip()])
        print(f"Created {filename}")
