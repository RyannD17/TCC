from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

pergunta = input("Digite sua pergunta: ")

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=pergunta
)

print(response.text)
