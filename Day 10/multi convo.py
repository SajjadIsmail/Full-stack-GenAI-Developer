from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv('GOOGLE_API_KEY'))
chat = client.chats.create(model="gemini-2.0-flash")

response = chat.send_message("My name is Sajjad Ismail")
print(response.text)

response = chat.send_message("What is my name")
print(response.text)

for message in chat.get_history():
    print(f'role - {message.role}',end=": ")
    print(message.parts[0].text)