from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

def HandleVoiceResponse(Input: str):
    try:
        client = OpenAI(api_key=os.getenv('API_KEY'))

        speech_file_path = "speech.mp3"
        response = client.audio.speech.create(
            model="tts-1",
            voice="onyx",
            input=Input
        )
        response.stream_to_file(speech_file_path)
    except Exception as e:
        return f"Error: {e}"