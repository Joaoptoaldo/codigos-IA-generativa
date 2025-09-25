from openai import OpenAI

client = OpenAI(api_key="SUA_CHAVE_OPENAI_AQUI")

schema = """
Tabelas e colunas disponíveis:

Tabela: book
Colunas:
- id (bigint)
- title (longtext)
- author (longtext)
- launch_date (date)
- price (decimal)
"""

pergunta = "quais são os livros que custam menos de 50 reais e foram lançados depois de 2020?"

prompt = f"""
Você é um gerador de SQL para MySQL.

Com base no esquema abaixo, gere apenas o SQL que responde a pergunta.

Esquema:
{schema}

Pergunta:
{pergunta}
"""

response = client.chat.completions.create(
    model="gpt-5",
    messages=[
        {"role": "system", "content": "Você é um gerador de SQL para MySQL."},
        {"role": "user", "content": prompt}
    ]
)

sql_bruto = response.choices[0].message.content.strip()

if sql_bruto.startswith('```sql'):
    sql_bruto = sql_bruto[6:]
if sql_bruto.startswith('```'):
    sql_bruto = sql_bruto[3:]
if sql_bruto.endswith('```'):
    sql_bruto = sql_bruto[:-3]

print(sql_bruto)
