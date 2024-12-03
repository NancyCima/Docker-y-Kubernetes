from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()

class TextAnalysisResponse(BaseModel):
    original_text: str
    length: int
    word_count: int
    uppercase: str
    reversed: str

@app.get("/analyze_text", response_model=TextAnalysisResponse)
async def analyze_text(
    text: str = Query(..., description="El texto que deseas analizar")
):
    return TextAnalysisResponse(
        original_text=text,
        length=len(text),
        word_count=len(text.split()),
        uppercase=text.upper(),
        reversed=text[::-1]
    )
