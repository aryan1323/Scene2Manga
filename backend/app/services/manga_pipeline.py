from langchain.Tools import expand_prompt, generate_manga


def manga_pipeline(scene_text: str):
    expanded = expand_prompt.run(scene_text)
    prompt = expanded + "\n\nStyle: black-and-white manga, screentones, sharp lineart."
    image = generate_manga.run(prompt)

    return {"expanded_prompt": prompt, "image_base64": image}
