import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DIFFUSION_MODEL_ID: str = os.getenv(
        "DIFFUSION_MODEL_ID", "Linaqruf/animagine-xl-3.1"
    )
    DEVICE: str = os.getenv("DEVICE", "cuda")
    IMAGE_HEIGHT: int = 1024
    IMAGE_WIDTH: int = 1024


settings = Settings()
