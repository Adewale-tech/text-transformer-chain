from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TextPayload(BaseModel):
    text: str

@app.post("/transform-text/")
async def transform_text(payload: TextPayload):
    async with httpx.AsyncClient() as client:
        # Capitalizer
        cap_res = await client.post("http://capitalizer_agent:8001/capitalize/", json=payload.dict())
        capitalized = cap_res.json()["text"]

        # Reverse
        rev_res = await client.post("http://reverse_agent:8002/reverse/", json={"text": capitalized})
        reversed_text = rev_res.json()["text"]

    return {"text": reversed_text}
