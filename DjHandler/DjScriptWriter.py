import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

sysPrompt: str = "You are a Dj bot who introduces songs and sets the mood. \
    Create a short 2-3 sentence script personalized to user when given information in json format based on listener. \
        In the Json be sure to cater to Dj Bot speacial instructions and the Example."

def HandleChatResponse(prompt: str) -> str:
    try:
        client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

        MODEL = "gpt-3.5-turbo"
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
            {"role": "system", "content": sysPrompt},
            {"role": "user", "content": prompt},
            ],
            temperature=0.3,
        )

        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"
