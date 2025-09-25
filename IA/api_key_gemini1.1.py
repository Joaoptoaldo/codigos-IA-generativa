import os
from google import genai

os.environ["GEMINI_API_KEY"] = "coloque sua api key aqui"

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

print("exemplo de prompt(pergunta):")
prompt = "me explique a teoria da relatividade de forma simples"
response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)

print(response.candidates[0].content.parts[0].text.strip())