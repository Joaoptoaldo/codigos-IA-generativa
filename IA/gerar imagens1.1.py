from openai import OpenAI
import base64

client = OpenAI(api_key="SUA_CHAVE_OPENAI_AQUI")

prompt = "gere a imagem de um gato astronauta flutuando no espaço"

response = client.images.generate(
    model="gpt-image-1",
    prompt=prompt,
    size="1024x1024"
)

image_base64 = response.data[0].b64_json
image_bytes = base64.b64decode(image_base64)

with open("gato_espacial.png", "wb") as f:
    f.write(image_bytes)

print("Imagem gerada: gato_astronauta.png")
