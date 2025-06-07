# 🎙️ Kokoro TTS API – FastAPI wrapper for local voice synthesis

This is a local-ready Text-to-Speech API built using **[Kokoro ONNX](https://huggingface.co/spaces/Kokoro-ai/Kokoro)** and served with **FastAPI**.  
It allows real-time voice synthesis with multiple voices, and supports generating your own custom voice embeddings from training data.

---

## 🚀 Features

- 🗣️ Use pre-trained Kokoro voices (e.g., `af_bella`)
- 🧠 Add your own voice by recording and training
- ⚡ FastAPI backend with `/synthesize` POST endpoint
- 🔊 Output streamed as `.wav` file
- 🧩 Runs locally (no internet, no GPU needed)

---

## 📦 Installation

```bash
git clone https://github.com/guvenagas/kokoro-api-tts.git
cd kokoro-api-tts

# Optional: create virtual environment
python -m venv venv
venv\Scripts\activate   # On Windows

# Install requirements
pip install -r requirements.txt


** Running the API**
 
uvicorn examples.voiceAPI:app --reload
Then open your browser at:
  
http://localhost:8000/docs
You’ll see an interactive Swagger UI where you can POST text and get back a voice .wav file.

📤 Synthesizing Voice
Sample request:
 
POST /synthesize/
{
  "sentence": "Merhaba dünya",
  "voice": "af_bella",
  "speed": 1.0
}
Returns: audio/wav stream.

🛠️ Create Your Own Voice
🎙️ Record ~7–10 min of clean audio

📝 Transcribe using Whisper:

 
whisper lazziya1.wav --model medium --output_format srt --language tr
🧠 Use our Python script to split and generate segments/ and metadata.csv

🔬 Train an embedding using tools like Resemblyzer

🧩 Add your .npy vector to the voice pack (JSON or .bin)

🎉 Use it via "voice": "my_custom_voice"

📁 Structure
 
kokoro-api-tts/
├── examples/
│   └── voiceAPI.py        # FastAPI server
├── whisper/               # Transcription + segmenting
├── segments/              # Sentence audio clips
├── metadata.csv           # Text file with filenames
├── voices.wav             # Embedding file (or .bin/.json)
├── requirements.txt
├── README.md
⚠️ Notes
GitHub warns about large .wav files (>50MB). You can add those to .gitignore or use Git LFS.

If using Turkish audio: be sure to set --language tr during Whisper transcription.

🙏 Credits
Built with Kokoro ONNX

Based on StyleTTS2 architecture
