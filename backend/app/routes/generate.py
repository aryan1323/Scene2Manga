from fastapi import APIRouter
from pydantic import BaseModel
from services.manga_pipeline import manga_pipeline

router = APIRouter()


class GenerateRequest(BaseModel):
    scene_text: str


class GenerateResponse(BaseModel):
    expanded_prompt: str
    image_base64: str


@router.post("/generate", response_model=GenerateResponse)
async def generate(req: GenerateRequest):
    return manga_pipeline(req.scene_text)
