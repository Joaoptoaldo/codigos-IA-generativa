from openai import OpenAI

client = OpenAI(api_key="SUA_CHAVE_OPENAI_AQUI")

print("=== ENGENHARIA DE PROMPTS ===\n")

print("""
Dicas:
1. Específico + contexto
2. Chain-of-Thought
3. Few-shot examples
""")

prompt_bom = "Você é professor. Explique relatividade para criança de 12 anos, passo a passo."

response = client.chat.completions.create(model="gpt-4o", messages=[{"role": "user", "content": prompt_bom}])

print("\nExemplo bom:")
print(response.choices[0].message.content.strip())

