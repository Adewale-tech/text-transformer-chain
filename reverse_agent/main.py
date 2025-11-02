from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TextPayload(BaseModel):
    text: str

@app.post("/reverse/")
async def reverse(payload: TextPayload):
    words = payload.text.split()
    reversed_text = " ".join(reversed(words))
    return {"text": reversed_text}
