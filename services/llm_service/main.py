from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()  # Creates your API instance

class Query(BaseModel):
    prompt: str  # Defines expected input

@app.post("/generate")
async def generate_text(query: Query):
    return {
        "response": f"Mocked answer to: {query.prompt}"  # Always returns a dummy response
    }
