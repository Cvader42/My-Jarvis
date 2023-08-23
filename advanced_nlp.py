import transformers
import spacy


class AdvancedNLP:
    def __init__(self):
        self.sentiment_analyzer = transformers.pipeline("sentiment-analysis")
        self.nlp = spacy.load("en_core_web_sm")

        # Additional features
        self.question_answerer = transformers.pipeline("question-answering",
                                                       question_types=["factoid"])
        self.summarization_model = transformers.pipeline("summarization")

    def analyze_sentiment(self, text):
        """
        Analyze sentiment of the given text.
        """
        sentiment = self.sentiment_analyzer(text)[0]
        sentiment_label = "POSITIVE" if sentiment["label"] == "LABEL_1" else "NEGATIVE"
        sentiment_score = sentiment["score"]
        return f"Sentiment: {sentiment_label} (Score: {sentiment_score:.4f})"

    def extract_named_entities(self, text):
        """
        Extract named entities from the given text.
        """
        doc = self.nlp(text)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        return entities

    def answer_question(self, question, context):
        """
        Answer the given question based on the given context.
        """
        return self.question_answerer(question=question, context=context)[0]["answer"]

    def summarize_text(self, text):
        """
        Summarize the given text.
        """
        return self.summarization_model(text)[0]["summary"]


if __name__ == "__main__":
    nlp = AdvancedNLP()
    input_text = "I'm extremely excited about the upcoming event with amazing speakers."

    sentiment_analysis = nlp.analyze_sentiment(input_text)
    named_entities = nlp.extract_named_entities(input_text)

    print(sentiment_analysis)
    print("Named Entities:")
    for entity, label in named_entities:
        print(f"{entity} - {label}")

    question = "What is the sentiment of the text?"
    context = input_text
    answer = nlp.answer_question(question, context)
    print(f"Answer: {answer}")

    summarized_text = nlp.summarize_text(input_text)
    print(f"Summary: {summarized_text}")
