from openai import OpenAI

client = OpenAI(api_key="SUA_CHAVE_OPENAI_AQUI")

print("=== ENGENHARIA DE PROMPTS - BOAS PRÁTICAS ===\n")

dicas = """
Boas práticas:
1. Seja específico e forneça contexto.
2. Use Chain-of-Thought (CoT): 'Pense passo a passo'.
3. Few-Shot: Dê exemplos.
4. Role-playing: 'Você é um professor de física'.
5. Especifique formato de saída (JSON, lista).
6. Iterativo: Refine baseado em respostas.
"""

print(dicas)

# Exemplo Before/After
prompt_ruim = "explique relatividade"
prompt_bom = "Você é um professor. Explique a teoria da relatividade especial de Einstein passo a passo, para uma criança de 12 anos. Use analogias simples."

response_ruim = client.chat.completions.create(model="gpt-4o", messages=[{"role": "user", "content": prompt_ruim}])
response_bom = client.chat.completions.create(model="gpt-4o", messages=[{"role": "user", "content": prompt_bom}])

print("\nPrompt Ruim:")
print(response_ruim.choices[0].message.content[:200] + "...")

print("\nPrompt Bom (com CoT e role):")
print(response_bom.choices[0].message.content.strip())

