# Exemplos, Estudos, e Boas Práticas de IA 

Este repositório reúne exemplos práticos e boas práticas para trabalhar com Inteligência Artificial Generativa, especialmente com modelos como OpenAI (GPT, DALL-E) e Google Gemini. 

## Estrutura 

- **basicos/**: Exemplos práticos de uso de APIs de IA generativa.
  - `01_configurar_api_gemini.py`: Como configurar e testar a API Gemini do Google.
  - `02_text_to_sql_buscar_livros.py`: Geração de SQL a partir de perguntas em linguagem natural usando OpenAI.
  - `03_gerar_imagens_dalle.py`: Geração de imagens com DALL-E (OpenAI).
  - `04_text_to_sql_possui_livro.py`: Exemplo de consulta SQL para verificar pessoas com livros cadastrados.
  - `05_text_to_sql_filtrar_genero.py`: Geração de SQL para filtrar pessoas por gênero e status.

- **estudo_e_boas_praticas/**: Materiais de apoio, dicas e boas práticas.
  - `06_recursos_estudo_ia.py`: Sugestões de cursos, livros e recursos para estudar IA.
  - `0701_engenharia_prompts.py` e `0702_engenharia_prompts.py`: Dicas e exemplos de engenharia de prompts.
  - `08_etica_ia.py`: Princípios éticos e checklist para desenvolvimento responsável.
  - `09_evitar_vies_ia.py`: Técnicas para detectar e mitigar vieses em IA.
  - `10_ia_responsavel.py`: Boas práticas para deploy responsável de IA.
  - `11_dicas_estudo_ia.py`: Dicas para estudar IA de forma eficiente e plano de estudos personalizado.

## Temas Abordados

- **Configuração de APIs**: Exemplos de como conectar e autenticar com as principais APIs de IA generativa.
- **Geração de SQL com LLMs**: Como transformar perguntas em linguagem natural em queries SQL usando modelos de linguagem.
- **Geração de Imagens**: Exemplos de prompts e manipulação de imagens geradas por IA.
- **Engenharia de Prompts**: Dicas para criar prompts mais eficazes, exemplos de before/after e boas práticas.
- **Ética, Viés e Responsabilidade**: Checklists, princípios e técnicas para garantir o uso seguro, justo e responsável de IA.
- **Estudo e Aprendizado**: Recursos recomendados, planos de estudo e dicas para quem está começando ou quer se aprofundar.

## Como Utilizar

1. **Pré-requisitos**:
   - Python 3.8+
   - Instalar dependências: `openai`, `google-generativeai` (ou `google.generativeai`)
   - Chaves de API válidas para OpenAI e/ou Google Gemini (substitua os placeholders nos scripts)

2. **Executando os exemplos**:
   - Edite o arquivo desejado e insira sua chave de API.
   - Execute com `python nome_do_arquivo.py`.
   - Siga as instruções impressas no terminal.

3. **Adaptação**:
   - Os exemplos são didáticos e podem ser adaptados para outros contextos, bancos de dados ou modelos.

## Boas Práticas

- Nunca compartilhe suas chaves de API publicamente.
- Revise e adapte prompts para o seu contexto.
- Sempre avalie resultados de IA criticamente, especialmente em aplicações sensíveis.
- Consulte os arquivos de boas práticas para dicas de ética, viés e segurança.

## Licença

Material criado para fins educacionais. Sinta-se livre para usar, adaptar e compartilhar, citando a fonte quando possível.