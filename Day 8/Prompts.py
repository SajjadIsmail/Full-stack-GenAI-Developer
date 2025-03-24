from google import genai
from dotenv import load_dotenv
import os
load_dotenv()

client = genai.Client(api_key=os.getenv('GOOGLE_API_KEY'))

#Example of Zero shot prompting
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents='''Please choose the best explanation to the question:
                Question: How is snow formed?
                Explanation1: Snow is formed when water vapor in the air freezes into ice crystals in the
                atmosphere, which can combine and grow into snowflakes as they fall through the atmosphere and
                accumulate on the ground.
                Explanation2: Water vapor freezes into ice crystals forming snow.
                Answer:
            '''
)
print("ZERO SHOT PROMPTING")
print(response.text)

#Example of few shot prompting
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents='''Below are some examples showing a question, explanation, and answer format:
                
                Question: Why is sky blue?
                Explanation1: The sky appears blue because of Rayleigh scattering, which causes shorter blue
                wavelengths of light to be scattered more easily than longer red wavelengths, making the sky look
                blue.
                Explanation2: Due to Rayleigh scattering effect.
                Answer: Explanation2
                
                Question: What is the cause of earthquakes?
                Explanation1: Sudden release of energy in the Earth's crust.
                Explanation2: Earthquakes happen when tectonic plates suddenly slip or break apart, causing a
                release of energy that creates seismic waves that can shake the ground and cause damage.
                Answer: Explanation1
                
                Now, Answer the following question given the example formats above:
                
                Question: How is snow formed?
                Explanation1: Snow is formed when water vapor in the air freezes into ice crystals in the
                atmosphere, which can combine and grow into snowflakes as they fall through the atmosphere and
                accumulate on the ground.
                Explanation2: Water vapor freezes into ice crystals forming snow.
                Answer:
            '''
)
print("FEW SHOT PROMPTING")
print(response.text)