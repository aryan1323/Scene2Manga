from diffusers import (
    DiffusionPipeline,
    DPMSolverMultistepScheduler,
    StableDiffusionXLPipeline,
)
import torch
from config import settings
import base64, io


class DiffusionEngine:
    def __init__(self):
        self.pipe = StableDiffusionXLPipeline.from_pretrained(
            "cagliostrolab/animagine-xl-4.0",
            torch_dtype=torch.float16,
            use_safetensors=True,
            custom_pipeline="lpw_stable_diffusion_xl",
            add_watermarker=False,
        )
        self.pipe.scheduler = DPMSolverMultistepScheduler.from_config(
            self.pipe.scheduler.config
        )
        self.pipe.to(settings.DEVICE)

    def generate(self, prompt: str):
        result = self.pipe(
            prompt=prompt,
            num_inference_steps=25,
            guidance_scale=7.5,
            height=settings.IMAGE_HEIGHT,
            width=settings.IMAGE_WIDTH,
        )

        image = result.images[0]
        buffer = io.BytesIO()
        image.save(buffer, format="PNG")
        return base64.b64encode(buffer.getvalue()).decode()
