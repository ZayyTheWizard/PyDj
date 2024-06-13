import pathlib
import textwrap
import os

from dotenv import load_dotenv
import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

load_dotenv()

# Load API key
genai.configure(api_key=os.getenv('API_KEY'))

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

def main():
    model = genai.GenerativeModel('gemini-1.5-flash')

    response = model.generate_content("Write rap abouts bees as if written by rapper 'Lil Wayne'")

    print(response.text)

if __name__ == '__main__':
    main()