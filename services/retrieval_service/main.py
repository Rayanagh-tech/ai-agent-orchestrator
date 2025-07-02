from fastapi import FastAPI
from pydantic import BaseModel
import uuid

app = FastAPI()

class Query(BaseModel):
    question: str

@app.post("/retrieve")
async def retrieve_documents(query: Query):
    return {
        "context": f"Mock context related to: '{query.question}'",
        "source": "document1.txt",
        "retrieval_id": str(uuid.uuid4())
    }
