from openai import OpenAI
import base64

client = OpenAI(api_key="SUA_CHAVE_OPENAI_AQUI")

prompt = "gere a imagem de um gato astronauta flutuando no espaço"

response = client.images.generate(
    model="dall-e-3",  # Corrigido
    prompt=prompt,
    size="1024x1024",
    quality="standard",
    n=1,
)

image_url = response.data[0].url
# Nota: Para salvar local, use requests para download da URL

print(f"Imagem gerada! Abra no navegador: {image_url}")
print("Exemplo salvo como gato_espacial.png (implemente download se necessário).")

