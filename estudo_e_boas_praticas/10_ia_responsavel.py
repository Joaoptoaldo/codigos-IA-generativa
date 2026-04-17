from openai import OpenAI

client = OpenAI(api_key="SUA_CHAVE_OPENAI_AQUI")

print("=== IA RESPONSÁVEL EM PRODUÇÃO ===\n")

praticas = """
Boas práticas para deployment:
1. Monitoramento contínuo (drift detection).
2. Rate limiting e segurança.
3. GDPR/Privacidade: Anonimização.
4. Human-in-the-loop para decisões críticas.
5. Documentação de limitações do modelo.
"""

print(praticas)

prompt = """
Gere um checklist para deploy responsável de um chatbot de IA.
Inclua segurança, escalabilidade e ética.
Formato numerado.
"""

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": prompt}]
)

print("\n=== CHECKLIST DEPLOY RESPONSÁVEL ===\n")
print(response.choices[0].message.content.strip())

