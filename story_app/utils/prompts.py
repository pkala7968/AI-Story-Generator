STORY_PROMPT = """
User prompt:
{user_prompt}

Produce a short imaginative short story (300-500 words) based on the above prompt. Keep it coherent and evocative.
"""

CHAR_DESC_PROMPT = """
Based on this short story:
{story}

Write a detailed character description for the protagonist:
- Name (optional)
- Age/appearance (clothing/pose)
- Personality (3-5 key traits)
- Distinctive features (scars, tattoos, accessories)
Keep the description concise but rich (150-250 words).
"""

BG_DESC_PROMPT = """
You are given this short story:
{story}

Your task is to write a **precise, realistic background/scene description** in **150-250 words**.

Requirements:
- Base all details directly on the story — no unrelated objects or settings.
- Describe the physical environment first (location, terrain, architecture, vegetation).
- Include time of day, lighting conditions, and color tones.
- Mention weather or atmospheric elements if relevant.
- Focus on spatial arrangement: what's in the foreground, midground, and background.
- Include notable props or structures that define the setting.
- Avoid describing characters, creatures, or actions — only the scene.
- Make the description clear and visually easy to imagine.
"""

CHAR_IMG_PROMPT = """
Based on this character description:
{char_desc}

Generate an image of the character. Make sure:
- The character is the main focus
- The background is simple or transparent
- The character's pose and expression match their personality
"""

BG_IMG_PROMPT = """
You are given this background description:
{bg_desc}

Generate an image of ONLY the environment.

Strict requirements:
- The scene must be **centered and balanced** so a character can be placed in the middle foreground later without obstructing key details.
- No characters, animals, or people — environment only.
- Keep important landmarks or visual focal points slightly in the background.
- Ensure depth and perspective (foreground → midground → background).
- Lighting, weather, and mood must exactly match the description.
- Maintain realistic proportions and coherent visual logic.
"""