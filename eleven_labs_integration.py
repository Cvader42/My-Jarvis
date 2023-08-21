import requests

def generate_speech(text, api_key):
    url = "https://api.eleven-labs.com/tts"
    headers = {
        "Authorization": f"Bearer {api_key}",
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

if __name__ == "__main__":
    api_key = "YOUR_API_KEY"  # Replace with your actual API key
    text = "Hello, this is Jarvis speaking."
    generate_speech(text, api_key)

