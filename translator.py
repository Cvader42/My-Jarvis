# translator.py

import deepl

class AdvancedTranslator:
    def __init__(self, api_key):
        self.translator = deepl.Translator(api_key)
    
    def translate(self, text, target_language):
        try:
            translation = self.translator.translate_text(text, target_lang=target_language)
            return translation
        except Exception as e:
            return f"Translation error: {str(e)}"

# Example usage
if __name__ == "__main__":
    import config
    advanced_translator = AdvancedTranslator(config.DEEPL_API_KEY)
    text_to_translate = "Hello, how are you?"
    target_language = "es"
    translated_text = advanced_translator.translate(text_to_translate, target_language)
    
    print(f"Original Text: {text_to_translate}")
    print(f"Translated Text ({target_language}): {translated_text}")
