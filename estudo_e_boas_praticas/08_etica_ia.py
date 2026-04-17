from openai import OpenAI

client = OpenAI(api_key="SUA_CHAVE_OPENAI_AQUI")

print("=== ÉTICA EM IA - BOAS MANEIRAS ===\n")

princípios = """
Princípios Éticos (baseado em Asilomar AI Principles):
1. Benefício humano: IA deve beneficiar todos.
2. Transparência: Modelos explicáveis.
3. Justiça: Evitar discriminação.
4. Privacidade: Proteger dados.
5. Responsabilidade: Accountability por decisões.
"""

print(princípios)

# Gerar checklist
prompt = """
Gere uma checklist de 10 itens para desenvolvimento ético de IA.
Formato: - [ ] Item descritivo
Inclua exemplos práticos.
"""

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": prompt}]
)

print("\n=== CHECKLIST ÉTICA GERADA PELA IA ===\n")
print(response.choices[0].message.content.strip())

