from openai import OpenAI

client = OpenAI(api_key="SUA_CHAVE_OPENAI_AQUI")

print("=== RECURSOS PARA ESTUDO DE IA ===\n")

# Lista manual de recursos recomendados
recursos = """
1. Cursos Gratuitos:
   - Machine Learning (Andrew Ng) - Coursera
   - Deep Learning Specialization (Andrew Ng) - Coursera
   - CS231n: CNNs for Visual Recognition (Stanford)

2. Livros:
   - 'Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow' - Aurélien Géron
   - 'Deep Learning' - Ian Goodfellow et al.
   - 'Python Machine Learning' - Sebastian Raschka

3. Papers Essenciais:
   - Attention is All You Need (Transformers)
   - Generative Adversarial Nets (GANs)

4. Plataformas:
   - Hugging Face Courses
   - fast.ai Practical Deep Learning
"""

print(recursos)

# Gerar plano personalizado
pergunta = "Crie um plano de estudos de 3 meses para iniciantes em IA generativa, focando em Python e LLMs."
prompt = f"""
Baseado nos recursos acima, gere um plano detalhado de 3 meses para iniciantes em IA.

Plano deve incluir:
- Semanas 1-4: Fundamentos
- Semanas 5-8: LLMs e Prompting
- Semanas 9-12: Projetos práticos

Seja específico com links e tarefas.
"""

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": prompt}]
)

print("\n=== PLANO DE ESTUDOS GERADO PELA IA ===\n")
print(response.choices[0].message.content.strip())

