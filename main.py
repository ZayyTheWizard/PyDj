from DjHandler.DjScriptWriter import HandleChatResponse
from DjHandler.DjVoice import HandleVoiceResponse
import json

def main():
  """
  Main Handler Will probebly change to a API end point but for testing purposes It's Here
  """
  with open('lyrics.txt', 'r') as lyrics:
    lyric = lyrics.read()

  with open('prompt.json', 'r') as file:
    data = json.load(file)

  data['Song Data']['Lyrics'] = lyric

  data = json.dumps(data)
  response = HandleChatResponse(data)

  HandleVoiceResponse(response)

if __name__ == '__main__':
    main()