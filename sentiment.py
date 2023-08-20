import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

class SentimentAnalyzer:
    def __init__(self):
        nltk.download('vader_lexicon')  # Download the required lexicon
        self.sia = SentimentIntensityAnalyzer()

    def analyze_sentiment(self, text):
        sentiment_score = self.sia.polarity_scores(text)
        sentiment = self.get_sentiment_label(sentiment_score)
        return sentiment, sentiment_score

    def get_sentiment_label(self, sentiment_score):
        compound_score = sentiment_score['compound']
        if compound_score >= 0.05:
            return "Positive"
        elif compound_score <= -0.05:
            return "Negative"
        else:
            return "Neutral"

if __name__ == "__main__":
    text = input("Enter the text to analyze sentiment: ")
    analyzer = SentimentAnalyzer()
    sentiment, sentiment_score = analyzer.analyze_sentiment(text)
    
    print("Sentiment:", sentiment)
    print("Sentiment Scores:", sentiment_score)

