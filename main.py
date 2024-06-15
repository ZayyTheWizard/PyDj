from dj_response_handler import HandleChatResponse 
import json

def main():
  with open('prompt.json', 'r') as file:
    data = json.load(file)

  data = json.dumps(data)

  response = HandleChatResponse(data)

  print(response)

if __name__ == '__main__':
    main()