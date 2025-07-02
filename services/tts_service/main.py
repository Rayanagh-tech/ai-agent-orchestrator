from fastapi import FastAPI
from pydantic import BaseModel
import uuid

app = FastAPI()

class TTSRequest(BaseModel):
    text: str

@app.post("/synthesize")
async def synthesize_audio(req: TTSRequest):
    return {
        "audio_url": f"http://fake-server.com/audio/{uuid.uuid4()}.mp3",
        "message": f"Synthesized audio for: {req.text}"
    }
