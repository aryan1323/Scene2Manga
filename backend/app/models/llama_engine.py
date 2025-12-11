from langchain_community.llms import Ollama


class LLaMAEngine:
    def __init__(self, model_name="llama3"):
        self.llm = Ollama(model=model_name)

    def expand_prompt(self, scene: str) -> str:
        prompt = f"""
You are a world-class manga art director.
Expand the following scene into a highly detailed manga-style prompt suitable for a diffusion model.

Scene: {scene}

Requirements:
- manga style
- dynamic lighting
- screentones
- high contrast black & white
- specify camera angle, action, emotions

Expanded Prompt:
"""
        return self.llm.invoke(prompt)
