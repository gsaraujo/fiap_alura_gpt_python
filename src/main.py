from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

resposta = cliente.chat.completions.create(
    messages=[
        {
            "role":"system",
            "content" : "Cite o produto e uma descrição básica."
        },
        {
            "role":"user",
            "content" : "Cite 3 produtos que posso encontrar em uma cozinha"
        }
    ],
    model="gpt-6-astra"
)

print(resposta.choices[0].message.content)