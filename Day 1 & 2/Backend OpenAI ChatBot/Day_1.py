# from openai import OpenAI
# from fastapi import FastAPI
# import os
# from dotenv import load_dotenv
# from fastapi.middleware.cors import CORSMiddleware
# import uvicorn
#
# load_dotenv()
# app = FastAPI()
#
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:3000"],  # Replace "*" with your frontend URL in production
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
#
# Op = os.getenv('OPENAI_KEY')
#
# @app.get('/GreetingMessage')
# def chat():
#     client = OpenAI(api_key=Op)
#     completion = client.chat.completions.create(
#         model="gpt-4-0613",
#         messages=[
#             {"role": "system", "content": 'Give a interactive greeting message to the user'}
#         ]
#     )
#     return completion.choices[0].message.content
#
# if __name__ == "__main__":
#     uvicorn.run(app,host="localhost",port=8000)
#
#

from openai import OpenAI
from fastapi import FastAPI
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from pydantic import BaseModel

load_dotenv()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Replace "*" with your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Op = os.getenv('OPENAI_KEY')

class question(BaseModel):
    question : str

@app.post('/GreetingMessage')
def chat(Request : question):
    message = Request.question
    client = OpenAI(api_key=Op)
    completion = client.chat.completions.create(
        model="gpt-4-0613",
        messages=[
            {"role": "system", "content": 'Answer the following the question asked by the user'},
            {"role": "user","content":message}
        ]
    )
    return completion.choices[0].message.content

if __name__ == "__main__":
    uvicorn.run(app,host="localhost",port=8000)