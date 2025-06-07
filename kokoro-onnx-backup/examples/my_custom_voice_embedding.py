from resemblyzer import VoiceEncoder, preprocess_wav
from pathlib import Path
import numpy as np
import os

encoder = VoiceEncoder()
wav_paths = list(Path("segments").glob("*.wav"))
embeddings = []

for path in wav_paths:
    wav = preprocess_wav(path)
    embed = encoder.embed_utterance(wav)
    embeddings.append(embed)

# Average over all embeddings
avg_embedding = np.mean(embeddings, axis=0)

# Save as .npy or reshape to (511, 1, 256) if needed
np.save("my_custom_voice_embedding.npy", avg_embedding)
