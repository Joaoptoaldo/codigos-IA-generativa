from openai import OpenAI

client = OpenAI(api_key="SUA_CHAVE_OPENAI_AQUI")

print("=== DICAS PARA ESTUDAR IA EFETIVAMENTE ===\n")

dicas_fixas = """
1. Pratique código todo dia (Kaggle, LeetCode ML).
2. Leia papers no arXiv/paperswithcode.
3. Participe de comunidades (Reddit r/MachineLearning, Discord HF).
4. Faça projetos reais (clone ChatGPT simples).
5. Entenda matemática: álgebra linear, probabilidade.
"""

print(dicas_fixas)

# Plano personalizado
nivel = "iniciante"  # Mude aqui
tempo = "6 meses"

prompt = f"""
Crie dicas personalizadas + plano de {tempo} para {nivel} em IA generativa.
Foco em prática, recursos grátis e projetos.
Saída em português.
"""

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": prompt}]
)

print("\n=== PLANO PERSONALIZADO GERADO ===\n")
print(response.choices[0].message.content.strip())

