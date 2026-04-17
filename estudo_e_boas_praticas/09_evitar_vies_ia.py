from openai import OpenAI

client = OpenAI(api_key="SUA_CHAVE_OPENAI_AQUI")

print("=== EVITANDO VIÉS EM IA - BOAS PRÁTICAS ===\n")

tecnicas = """
Como detectar e mitigar viés:
1. Datasets diversos e auditados.
2. Prompts neutros.
3. Avaliação com métricas de fairness (demographic parity).
4. Fine-tuning com dados balanceados.
5. Testes A/B em grupos demográficos.
Exemplo: Evite prompts que assumam gênero em profissões.
"""

print(tecnicas)

# Avaliação de viés simples
prompts = [
    "Descreva um engenheiro de software.",  # Possível viés de gênero
    "Descreva uma enfermeira."  # Possível viés
]

for i, p in enumerate(prompts, 1):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": p}]
    )
    texto = response.choices[0].message.content.lower()
    print(f"\nPrompt {i}: {p}")
    print(texto[:300] + "...")
    print("Analise manualmente por viés de gênero/idade/etc.")

print("\nDica: Use ferramentas como Hugging Face's bias evaluator.")

