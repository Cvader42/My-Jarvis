import os
import webbrowser
import speech_recognition as sr

def search_on_youtube(query):
    search_url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(search_url)

def play_song_from_folder(folder_path):
    songs = os.listdir(folder_path)
    if not songs:
        return "No songs found in the folder."
    
    song_index = 0  # Change this to select a different song
    if 0 <= song_index < len(songs):
        song_path = os.path.join(folder_path, songs[song_index])
        os.startfile(song_path)
        return f"Playing {songs[song_index]}"
    else:
        return "Invalid song index."

def main():
    print("Welcome to Voice-Controlled YouTube Player!")
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Say 'YouTube' to search on YouTube or 'Play' to play a local song:")
        user_input = recognize_speech(recognizer, source)
        
        if "youtube" in user_input:
            print("What do you want to search on YouTube?")
            query = recognize_speech(recognizer, source)
            search_on_youtube(query)
        elif "play" in user_input:
            print("Do you want to play a local song? Say 'Yes' or 'No'")
            play_choice = recognize_speech(recognizer, source)
            
            if "yes" in play_choice:
                print("Please provide the path to your music folder:")
                folder_path = recognize_speech(recognizer, source)
                response = play_song_from_folder(folder_path)
                print(response)
            else:
                print("What do you want to play on YouTube?")
                query = recognize_speech(recognizer, source)
                search_on_youtube(query)
        else:
            print("Invalid command.")

def recognize_speech(recognizer, source):
    try:
        print("Listening...")
        audio = recognizer.listen(source, timeout=5)
        print("Processing...")
        user_input = recognizer.recognize_google(audio)
        print(f"Recognized: {user_input}")
        return user_input.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")
        return ""
    except sr.RequestError:
        print("Sorry, I'm having trouble processing your request.")
        return ""

if __name__ == "__main__":
    main()
