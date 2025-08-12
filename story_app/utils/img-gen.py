from PIL import Image, ImageOps
import numpy as np
from llm_chains import generate_story_and_descriptions
from prompts import CHAR_IMG_PROMPT, BG_IMG_PROMPT
from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

load_dotenv()
HF_TOKEN  = os.getenv("HF_TOKEN")

# client = InferenceClient(provider="fal-ai", api_key=HF_TOKEN)
client = InferenceClient(provider="nebius",api_key=HF_TOKEN)

OUTPUT_DIR = "images"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# model_id = "Qwen/Qwen-Image"
model_id = "black-forest-labs/FLUX.1-dev"

def generate_character_image(char_desc, output_path=os.path.join(OUTPUT_DIR, "character.png")):
    prompt = CHAR_IMG_PROMPT.format(char_desc=char_desc)
    try:
        # text_to_image returns a PIL.Image for supported providers/models
        image = client.text_to_image(prompt, model=model_id)
    except Exception as e:
        # helpful error for debugging (rate limit, permission, network, etc.)
        raise RuntimeError(f"Failed to generate character image: {e}") from e

    if not isinstance(image, Image.Image):
        raise RuntimeError("Unexpected response type from InferenceClient.text_to_image()")
    image.save(output_path)
    return image

def generate_background_image(bg_desc, output_path=os.path.join(OUTPUT_DIR, "background.png")):
    prompt = BG_IMG_PROMPT.format(bg_desc=bg_desc)
    try:
        image = client.text_to_image(prompt, model=model_id)
    except Exception as e:
        raise RuntimeError(f"Failed to generate background image: {e}") from e

    if not isinstance(image, Image.Image):
        raise RuntimeError("Unexpected response type from InferenceClient.text_to_image()")
    image.save(output_path)
    return image

def merge_images(foreground_img, background_img, output_path=os.path.join(OUTPUT_DIR, "final_scene.png")):
    # Ensure both images are RGBA for transparency handling
    foreground_img = foreground_img.convert("RGBA")
    background_img = background_img.convert("RGBA")

    # White background removal
    data = np.array(foreground_img)
    r, g, b, a = data.T

    # Define white threshold (tweakable)
    white_areas = (r > 240) & (g > 240) & (b > 240)
    data[..., :-1][white_areas.T] = (0, 0, 0)  # Make RGB black
    data[..., -1][white_areas.T] = 0           # Make alpha transparent

    foreground_img = Image.fromarray(data)

    # Resize foreground to fit background  
    fg_max_width = int(background_img.width * 0.8)
    fg_max_height = int(background_img.height * 0.8)
    foreground_img.thumbnail((fg_max_width, fg_max_height), Image.LANCZOS)

    # Center position
    x = (background_img.width - foreground_img.width) // 2
    y = (background_img.height - foreground_img.height) // 2

    # Paste with alpha mask  
    background_img.paste(foreground_img, (x, y), mask=foreground_img)

    # Save and return merged image
    background_img.save(output_path)
    return background_img

if __name__ == "__main__":
    story, char_desc, bg_desc = generate_story_and_descriptions(
        "generate story about a pickle who became a rapper"
    )

    print("Generating character image...")
    char_img = generate_character_image(char_desc)

    print("Generating background image...")
    bg_img = generate_background_image(bg_desc)

    print("Merging images...")
    merged_scene = merge_images(char_img, bg_img)

    print("\nStory:\n", story)
    print("\nCharacter Description:\n", char_desc)
    print("\nBackground Description:\n", bg_desc)