from fastapi import FastAPI
from pydantic import BaseModel
import httpx

app = FastAPI()

class TextPayload(BaseModel):
    text: str

@app.post("/transform-text/")
async def transform_text(payload: TextPayload):
    try:
        async with httpx.AsyncClient() as client:
            # Step 1: Capitalizer Agent (local)
            cap_res = await client.post(
                "https://text-transformer-chain-1.onrender.com/",
                json=payload.dict()
            )
            cap_res.raise_for_status()
            capitalized = cap_res.json()["text"]

            # Step 2: Reverse Agent (local)
            rev_res = await client.post(
                "https://text-transformer-chain.onrender.com/",
                json={"text": capitalized}
            )
            rev_res.raise_for_status()
            reversed_text = rev_res.json()["text"]
        return {"text": reversed_text}
    except Exception as e:
        return {"error": str(e)}

