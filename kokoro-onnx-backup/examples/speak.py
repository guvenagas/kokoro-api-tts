import soundfile as sf
from kokoro_onnx import Kokoro
from kokoro_onnx.config import SAMPLE_RATE

# Initialize the model
kokoro = Kokoro("kokoro-v1.0.onnx", "voices-v1.0.bin")

# Choose your voice and sentence
voice = "af_bella"
sentence = """ heeeeeeelllllppppp
"""

# Generate audio
samples, _ = kokoro.create(sentence, voice=voice, speed=1.0)

# Save to WAV
sf.write(f"test.wav", samples, SAMPLE_RATE)
print(f"Created {voice}.wav")
