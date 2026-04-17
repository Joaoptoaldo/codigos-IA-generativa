import os
from google.generativeai import GenerativeModel  # Corrigido import (era genai.Client, mas padrão é generativeai)

# Coloque sua API key aqui ou em variável de ambiente
os.environ["GEMINI_API_KEY"] = "coloque sua api key aqui"

model = GenerativeModel('gemini-1.5-flash', api_key=os.getenv("GEMINI_API_KEY"))

print("Exemplo de prompt (pergunta):")
prompt = "me explique a teoria da relatividade de forma simples"
response = model.generate_content(prompt)

print(response.text.strip())
print("\nAPI Gemini configurada com sucesso!")

