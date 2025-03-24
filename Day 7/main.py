from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import SystemMessage, HumanMessage
import uvicorn
import os
from pinecone import Pinecone

load_dotenv()

app = FastAPI()
KEY = os.getenv("GOOGLE_API_KEY")
pc = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class text(BaseModel):
    message: str


class query(BaseModel):
    query: str


@app.post('/chatmodel')
async def openai(request: text):
    text = request.message
    model = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro",
        temperature=1,
        max_tokens=200
    )

    messages = [SystemMessage(content="Complete the sentence"),
                HumanMessage(content=text)]
    result = model.invoke(messages)
    return result.content


def retrieve_knowledge(query):
    o = []
    index = pc.Index("example-index")
    # Search in Uploaded Documents (VectorDB)
    query_embedding = pc.inference.embed(
        model="multilingual-e5-large",
        inputs=query,
        parameters={
            "input_type": "query"
        }
    )
    # Search the index for the three most similar vectors
    results = index.query(
        namespace='example-namespace',
        vector=query_embedding[0].values,
        top_k=3,
        include_metadata=True,
        include_values=False
    )

    for match in results['matches']:
        o.append(match['metadata']['text'])
    return o


@app.post('/faq')
async def faq_ans(request: query):
    query = request.query
    knowledge = retrieve_knowledge(query)
    my_str = ' '.join(knowledge)

    base_information = '''Q: What is LangChain?
    A: LangChain is a framework designed to simplify the process of building applications that utilize language models.
    Q: How do I set up my environment?
    A: Follow the instructions in the "Getting Started" section above. Ensure you have Python 3.10 or 3.11 installed, install Poetry, clone the repository, install dependencies, rename the .env.example file to .env, and activate the Poetry shell.
    Q: I am getting an error when running the examples. What should I do?
    A: Ensure all dependencies are installed correctly and your environment variables are set up properly. If the issue persists, seek help in the Skool community or open an issue on GitHub.
    Q: Can I contribute to this repository?
    A: Yes! Contributions are welcome. Please open an issue or submit a pull request with your changes.
    Q: Where can I find more information about LangChain?
    A: Check out the official LangChain documentation and join the Skool community for additional resources and support.'''

    combined_context = f"{base_information}\n{my_str}"

    model = ChatGoogleGenerativeAI(key=KEY, model="gemini-1.5-pro", temperature=0)
    messages = [
        SystemMessage(content=''''You are a helpful assistant that answers user queries based on the provided context. 
                                The context consists of FAQs and additional information. Always try to answer from the context if relevant.
                                If a question is unrelated to the provided context, respond with "IRRELEVANT." Ensure factual accuracy in your responses.'''),
        HumanMessage(content=f"Context: {combined_context}\nQuestion: {query}")
    ]

    result = model.invoke(messages)
    return result.content

if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8000)

