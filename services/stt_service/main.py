from fastapi import FastAPI, UploadFile, File
import uuid

app = FastAPI()

@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    return {"transcription": f"Mock transcription for {file.filename}", "id": str(uuid.uuid4())}
