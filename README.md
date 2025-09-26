# IA Generativa

Este repositório é voltado para **exemplos práticos de Inteligência Artificial Generativa**, incluindo geração de texto, imagens e código.

---


## Exemplo simples em Python (texto)

```python
from openai import OpenAI

client = OpenAI(api_key="SUA_CHAVE_OPENAI_AQUI")

prompt = "Escreva uma pequena história sobre qualquer coisa"

response = client.chat.completions.create(
    model="gpt-5",
    messages=[{"role": "user", "content": prompt}]
)

print(response.choices[0].message.content)


