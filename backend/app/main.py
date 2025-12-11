from fastapi import FastAPI
from routes.generate import router

app = FastAPI(title="Scene to Manga Generator (Ollama + SDXL)")

app.include_router(router, prefix="/api")


@app.get("/health")
def health():
    return {"status": "ok"}
