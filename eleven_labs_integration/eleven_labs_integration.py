"""
Module to integrate with the Eleven Labs Text-to-Speech API.
"""

from config import ELEVEN_LABS_API_KEY
import requests

def generate_speech(text):
    """
    Generate speech from the given text using the Eleven Labs API.
    """
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
        with open("output.mp3", "wb") as output_file:
            output_file.write(response.content)
        print("Speech generated and saved as 'output.mp3'")
    else:
        print("Error:", response.text)

# Example usage
if __name__ == "__main__":
    input_text = "Hello, this is a test speech."
    generate_speech(input_text)
