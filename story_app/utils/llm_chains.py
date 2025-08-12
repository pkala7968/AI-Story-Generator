import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from .prompts import STORY_PROMPT, CHAR_DESC_PROMPT, BG_DESC_PROMPT
import warnings

warnings.filterwarnings("ignore")

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

hf_llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.7,
    max_output_tokens=512,
)

story_chain = LLMChain(
    llm=hf_llm,
    prompt=PromptTemplate(template=STORY_PROMPT, input_variables=["user_prompt"])
)

char_chain = LLMChain(
    llm=hf_llm,
    prompt=PromptTemplate(template=CHAR_DESC_PROMPT, input_variables=["story"])
)

bg_chain = LLMChain(
    llm=hf_llm,
    prompt=PromptTemplate(template=BG_DESC_PROMPT, input_variables=["story"])
)

def generate_story_and_descriptions(user_prompt):
    story_text = story_chain.run(user_prompt=user_prompt)
    char_desc = char_chain.run(story=story_text)
    bg_desc = bg_chain.run(story=story_text)
    return story_text, char_desc, bg_desc

if __name__ == "__main__":
    story, char_desc, bg_desc = generate_story_and_descriptions("generate story about a pickle who became a rapper")
    print(story)
    print("*"*20)
    print(char_desc)
    print("*"*20)
    print(bg_desc)