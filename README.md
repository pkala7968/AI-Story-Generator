# AI Story Generator
## Overview

This project is a Django web application integrated with LangChain to generate creative stories and corresponding AI-generated images. The app accepts a user prompt (text or optional audio transcription), generates a short story, detailed character and background descriptions, and produces a combined scene image by merging character and background AI-generated images.

---

## Features

- User input: Text prompt for the story.
- LangChain orchestration with separate chains for:
  - Story and descriptions generation (story, character description, background description).
  - Character image generation based on character description.
  - Background image generation based on background description.
- AI image generation using free/open-source models (e.g., Stable Diffusion via Hugging Face).
- Image merging using PIL.
- Displays:
  - Generated short story
  - Character description
  - Combined scene image

---

## Getting Started

### Prerequisites

- Python 3.8+
- Git

### Installation

1. Clone the repository:
```bash
git clone https://github.com/pkala7968/AI-Story-Generator.git
cd mystory
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# On Linux/Mac
source venv/bin/activate  
# On Windows
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a .env file in the project root with and set the required API keys:
```ini
GOOGLE_API_KEY=your_gemini_api_key
HF_TOKEN=your_huggingface_access_token
```

5. Run Django migrations:
```bash
python manage.py migrate
```

6. Start the development server:
```bash
python manage.py runserver
```

7. Open your browser and navigate to `http://localhost:8000`

---

## Check It Out! 👇
[input](story_app/static/imgs/input.png)
---
[output1](story_app/static/imgs/op1.png)
[output2](story_app/static/imgs/op2.png)
[output3](story_app/static/imgs/op3.png)
