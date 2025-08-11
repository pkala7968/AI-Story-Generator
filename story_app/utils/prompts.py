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
Based on this short story:
{story}

Write a detailed background/scene description:
- Location / environment
- Time of day / lighting
- Atmosphere / mood
- Important props or architectural features
Keep this clear (150-250 words).
"""