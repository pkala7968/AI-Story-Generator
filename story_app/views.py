from django.shortcuts import render
from .utils.llm_chains import generate_story_and_descriptions
from .utils.imggen import generate_character_image, generate_background_image, merge_images
import os

def index(request):
    return render(request, 'index.html')

def result(request):
    if request.method == "POST":
        user_prompt = request.POST.get("prompt", "")

        # Generate story + descriptions
        story, char_desc, bg_desc = generate_story_and_descriptions(user_prompt)

        # Generate images
        char_img = generate_character_image(char_desc)
        bg_img = generate_background_image(bg_desc)
        merge_images(char_img, bg_img)  # Saves final_scene.png in static dir

        # Static path to final image
        image_url = '/static/story_app/images/final_scene.png'

        return render(request, 'result.html', {
            'story': story,
            'image_url': image_url
        })
    else:
        return render(request, 'index.html')
