from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class Query(BaseModel):
    prompt: str

@app.post("/generate")
async def generate_text(query: Query):
    return {
        "response": f"Mocked answer to: {query.prompt}"
    }
