from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import soundfile as sf
import io
import uuid

from kokoro_onnx import Kokoro
from kokoro_onnx.config import SAMPLE_RATE

# Step 1: Create app
app = FastAPI()

# Step 2: Add CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Step 3: Initialize Kokoro model
kokoro = Kokoro("kokoro-v1.0.onnx", "voices-v1.0.bin")

# Step 4: Define input model
class TextInput(BaseModel):
    sentence: str
    voice: str
    speed: float = 1.0

# Step 5: Define synthesize route
@app.post("/synthesize/")
async def synthesize_text(data: TextInput):
    try:
        # Generate audio in memory
        samples, _ = kokoro.create(data.sentence, voice=data.voice, speed=data.speed)

        # Save to disk (optional)
        filename = f"{uuid.uuid4().hex}.wav"
        sf.write(filename, samples, SAMPLE_RATE)

        # Stream to browser
        buffer = io.BytesIO()
        sf.write(buffer, samples, SAMPLE_RATE, format="WAV")
        buffer.seek(0)

        return StreamingResponse(
            buffer,
            media_type="audio/wav",
            headers={"Content-Disposition": f"inline; filename={filename}"}
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
