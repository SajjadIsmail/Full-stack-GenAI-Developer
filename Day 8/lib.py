from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import SystemMessage, HumanMessage

load_dotenv()

class PromptLibrary:
    def __init__(self):
        self.prompts = {
            "dentist": "Analyze dental symptoms and suggest possible causes and treatments.Answer only to dental symptoms",
            "cardiologist": "Explain necessary tests and provide emergency steps for heart-related symptoms.Answer only to cardiologist symptoms",
            "dermatologist": "Analyze skin conditions and recommend suitable treatments.Answer only to dermatologist symptoms",
            "general_physician": "Provide treatment recommendations for common illnesses and vaccination guidance.Answer only to general_physician symptoms",
        }

    def get_prompt(self, category: str) -> str:
        try:
            return self.prompts[category]
        except KeyError:
            raise ValueError(f"Invalid category '{category}'.")


prompt_library = PromptLibrary()
print(list(prompt_library.prompts.keys()))

# Example Integration
category = input("Enter the category from the above list: ")

if category not in list(prompt_library.prompts.keys()):
    print("INVALID")

prompt_library = PromptLibrary()
prompt_text = prompt_library.get_prompt(category)

model = ChatGoogleGenerativeAI(api_key = os.getenv('GOOGLE_API_KEY'),
    model="gemini-1.5-flash",
    temperature=0.7,
)
content = input("Tell me your issues: ")

messages = [SystemMessage(content=prompt_text),
            HumanMessage(content=content)]
result = model.invoke(messages)
print(result.content)
