import os
import torch
import speech_recognition as sr
from intents import get_intent
from models.davinci_model import DavinciModel
from models.function_model import FunctionModel
from models.llama_model import LlamaModel
from models.curie_model import CurieModel
from models.retriever_model import RetrieverModel
from knowledge import KnowledgeGraph
from calendar import Calendar
from translator import translate
from speech_recognition import listen
from text_to_speech import speak
from dialog import DialogManager
from sentiment import analyze_sentiment
from advanced_actions import perform_advanced_action
from advanced_nlp import extract_entities
from advanced_dialog import manage_advanced_dialog
from email_integration import read_emails
from messaging_integration import read_messages
from api_keys import (
    GOOGLE_CUSTOM_SEARCH_KEY,
    OPENWEATHERMAP_KEY,
    NEWS_API_KEY,
    # ... Other imported keys
)
from music_integration import play_music
from smart_reminders import ReminderManager
from social_media import post_to_twitter, post_to_facebook, post_to_instagram, post_to_linkedin
from language_translation import translate_text
from travel_information import get_flight_info, get_travel_suggestions, get_hotel_recommendations
from shopping_assistance import search_products, compare_prices, add_to_cart
from recipe_suggestions import get_recipe_suggestions
from personal_finance_tracking import get_account_balance, track_expenses, get_investment_performance
from health_fitness_tracking import track_exercise_routines, suggest_workouts, provide_health_tips

from whisper_asr import transcribe_audio

recognizer = sr.Recognizer()

def execute_command(command):
    try:
        os.system(command)
        return "Command executed successfully."
    except Exception as e:
        return f"Error: {e}"

def main():
    print("Welcome to Your Voice Assistant!")

    knowledge = KnowledgeGraph()
    calendar = Calendar()
    dialog_manager = DialogManager()
    reminder_manager = ReminderManager()  # Initialize the ReminderManager

    while True:
        # Speech Recognition using Whisper ASR
        audio_file_path = listen()
        user_input = transcribe_audio(audio_file_path)
        
        # Advanced Dialog Management
        user_input = manage_advanced_dialog(user_input, dialog_manager)

        # Extract Entities using Advanced NLP
        entities = extract_entities(user_input)

        # Perform Advanced Actions
        if "perform" in user_input:
            response = perform_advanced_action(entities)
        else:
            response = "I'm here to assist you."

        # Regular Voice Assistant Functionality
        if "exit" in user_input:
            print("Exiting...")
            break
        elif "execute" in user_input:
            command = user_input.split("execute")[-1].strip()
            if not command:
                print("No command specified. Please try again.")
            else:
                output = execute_command(command)
                print(output)
        elif "knowledge" in user_input:
            results = knowledge.query(user_input)
            if results:
                response = f"Here is what I know: {results}"
            else:
                response = "I'm not sure about that."
        elif "event" in user_input:
            response = calendar.process_input(user_input)
        elif "translate" in user_input:
            translated = translate_text(user_input)
            response = f"Translated: {translated}"
        elif "speak" in user_input:
            speak(response)
        elif "sentiment" in user_input:
            sentiment = analyze_sentiment(user_input)
            response = f"The sentiment is {sentiment}."
        # Add your other feature-specific conditionals here
        elif "play music" in user_input:
            track_name = user_input.replace("play music", "").strip()
            response = play_music(track_name)
        elif "post to twitter" in user_input:
            message = user_input.replace("post to twitter", "").strip()
            response = post_to_twitter(message)
        elif "post to facebook" in user_input:
            message = user_input.replace("post to facebook", "").strip()
            response = post_to_facebook(message)
        else:
            response = "I didn't catch that. Can you please repeat?"
        elif "post to twitter" in user_input:
          message = user_input.replace("post to twitter", "").strip()
          response = post_to_twitter(message)
        elif "post to facebook" in user_input:
          message = user_input.replace("post to facebook", "").strip()
          response = post_to_facebook(message)
        elif "post to instagram" in user_input:
          message = user_input.replace("post to instagram", "").strip()
          response = post_to_instagram(message)
       elif "post to linkedin" in user_input:
          message = user_input.replace("post to linkedin", "").strip()
          response = post_to_linkedin(message)
       elif "translate" in user_input:
          translated = translate_text(user_input)
          response = f"Translated: {translated}"
      elif "speak" in user_input:
        speak(response)
      elif "sentiment" in user_input:
        sentiment = analyze_sentiment(user_input)
        response = f"The sentiment is {sentiment}."


