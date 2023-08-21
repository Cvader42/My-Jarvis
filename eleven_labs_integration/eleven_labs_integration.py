# eleven_labs_integration.py
from config import ELEVEN_LABS_API_KEY
import requests

def generate_speech(text):
    url = "https://api.eleven-labs.com/tts"
    headers = {
        "Authorization": f"Bearer {ELEVEN_LABS_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "text": text
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        with open("output.mp3", "wb") as f:
            f.write(response.content)
        print("Speech generated and saved as 'output.mp3'")
    else:
        print("Error:", response.text)

