from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TextPayload(BaseModel):
    text: str

@app.post("/capitalize/")
async def capitalize(payload: TextPayload):
    return {"text": payload.text.upper()}


