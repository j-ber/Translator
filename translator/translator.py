"""
translator.py

This module provides functions for translating text between English and French.
"""

from deep_translator import MyMemoryTranslator


def translate_english_to_french(text):
    """
    Translates English text to French.
    Args:
        text (str): The text to be translated.
    Returns:
        str: The translated text in French.
    """
    translator = MyMemoryTranslator(source='en', target='fr')
    translation = translator.translate(text)
    return translation


def translate_french_to_english(text):
    """
    Translates French text to English.
    Args:
        text (str): The text to be translated.
    Returns:
        str: The translated text in English.
    """
    translator = MyMemoryTranslator(source='fr', target='en')
    translation = translator.translate(text)
    return translation

def main():
    # Test translation from English to French
    english_text = 'h'
    while(english_text != 'q'):
        english_text = input("Enter a sentence in English: ")
        french_translation = translate_english_to_french(english_text)
        print("English to French:")
        print(f"French: {french_translation}\n")

if __name__ == "__main__":
    main()
