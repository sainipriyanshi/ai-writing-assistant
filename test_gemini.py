import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

response = client.models.generate_content(
    model="gemini-flash-latest",
    contents="Reply with exactly: Gemini connection successful",
    config=types.GenerateContentConfig(temperature=0.0),
)

print(response.text)