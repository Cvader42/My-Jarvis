import re
import nltk
import random
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class IntentRecognizer:
    def __init__(self):
        self.intents = {
            "greeting": ["hello", "hi", "hey", "howdy"],
            "farewell": ["bye", "goodbye", "see you", "take care"],
            "thank_you": ["thank you", "thanks"],
            "weather": ["weather", "weather forecast", "how's the weather"],
            # Add more intents and their related keywords here
        }
        self.responses = {
            "greeting": ["Hello!", "Hi there!", "Hey! How can I assist you?"],
            "farewell": ["Goodbye!", "Take care!", "See you next time!"],
            "thank_you": ["You're welcome!", "My pleasure!", "Anytime!"],
            "weather": ["Checking the weather for you..."],
            # Add more intent-specific responses here
            "unknown": ["I'm not sure I understand.", "Could you rephrase that?", "I'm still learning."]
        }

    def get_intent(user_input):
    # ... Existing intent recognition logic ...

    # Check for beat generation command
    if "generate a beat" in user_input:
        return "generate_beat"

    # ... Other intent checks ...

    return None
    
    def preprocess_text(self, text):
        text = text.lower()
        tokens = word_tokenize(text)
        tokens = [word for word in tokens if word not in stopwords.words("english")]
        lemmatizer = WordNetLemmatizer()
        lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
        return " ".join(lemmatized_tokens)

    def recognize_intent(self, user_input):
        user_input = self.preprocess_text(user_input)
        max_similarity = 0
        recognized_intent = "unknown"

        for intent, keywords in self.intents.items():
            keyword_text = " ".join(keywords)
            keyword_text = self.preprocess_text(keyword_text)

            vectorizer = CountVectorizer().fit_transform([user_input, keyword_text])
            vectors = vectorizer.toarray()
            similarity = cosine_similarity(vectors[0].reshape(1, -1), vectors[1].reshape(1, -1))[0][0]

            if similarity > max_similarity:
                max_similarity = similarity
                recognized_intent = intent

        return recognized_intent

    def get_response(self, intent):
        response_list = self.responses.get(intent, self.responses["unknown"])
        return random.choice(response_list)

if __name__ == "__main__":
    nltk.download("punkt")
    nltk.download("stopwords")
    nltk.download("wordnet")

    recognizer = IntentRecognizer()

    while True:
        user_input = input("You: ")
        intent = recognizer.recognize_intent(user_input)
        response = recognizer.get_response(intent)
        print("Bot:", response)

