"""
Module to implement the AdvancedNLP class for advanced natural language processing tasks.
"""

import transformers
import spacy

class AdvancedNLP:
    """
    Class to perform advanced natural language processing tasks using transformers and spaCy.
    """

    def __init__(self):
        self.sentiment_analyzer = transformers.pipeline("sentiment-analysis")
        self.nlp = spacy.load("en_core_web_sm")
    
    def analyze_sentiment(self, text):
        """
        Analyze sentiment of the given text.
        """
        sentiment = self.sentiment_analyzer(text)[0]
        sentiment_label = "Positive" if sentiment['label'] == 'LABEL_1' else "Negative"
        sentiment_score = sentiment['score']
        return f"Sentiment: {sentiment_label} (Score: {sentiment_score:.4f})"
    
    def extract_named_entities(self, text):
        """
        Extract named entities from the given text.
        """
        doc = self.nlp(text)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        return entities

# Example usage
if __name__ == "__main__":
    nlp = AdvancedNLP()
    input_text = "I'm extremely excited about the upcoming event with amazing speakers."
    
    sentiment_analysis = nlp.analyze_sentiment(input_text)
    named_entities = nlp.extract_named_entities(input_text)
    
    print(sentiment_analysis)
    print("Named Entities:")
    for entity, label in named_entities:
        print(f"{entity} - {label}")
