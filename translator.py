from translate import Translator

class AdvancedTranslator:
    def __init__(self):
        self.translator = Translator(to_lang="en")
    
    def translate(self, text, target_language):
        try:
            translation = self.translator.translate(text, to_lang=target_language)
            return translation
        except Exception as e:
            return f"Translation error: {str(e)}"

# Example usage
if __name__ == "__main__":
    advanced_translator = AdvancedTranslator()
    text_to_translate = "Hello, how are you?"
    target_language = "es"
    translated_text = advanced_translator.translate(text_to_translate, target_language)
    
    print(f"Original Text: {text_to_translate}")
    print(f"Translated Text ({target_language}): {translated_text}")

