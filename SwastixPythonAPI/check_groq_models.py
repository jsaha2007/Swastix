import requests
import os
from dotenv import load_dotenv

load_dotenv()
resp = requests.get(
    "https://api.groq.com/openai/v1/models",
    headers={"Authorization": f"Bearer {os.getenv('GROQ_API_KEY')}"}
)
for model in resp.json()["data"]:
    print(model["id"])
