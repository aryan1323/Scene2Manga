from langchain_community.tools import tool
from models.llama_engine import LLaMAEngine
from models.diffusion_engine import DiffusionEngine

llama = LLaMAEngine("llama3")
diffusion = DiffusionEngine()


@tool
def expand_prompt(scene: str) -> str:
    """Expand scene text into a detailed manga-style diffusion prompt."""
    return llama.expand_prompt(scene)


@tool
def generate_manga(prompt: str) -> str:
    """Generate a manga-style image (base64) using Animagine XL diffusion model."""
    return diffusion.generate(prompt)


# Export tool list for agent usage
TOOLS = [expand_prompt, generate_manga]
