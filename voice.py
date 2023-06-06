from translate import Translator

# Create an instance of the Translator class
translator = Translator(to_lang="ta")

# Specify the source and destination languages
source_lang = 'en'  # Source language code (e.g., 'en' for English)
dest_lang = 'fr'   # Destination language code (e.g., 'fr' for French)

# Text to translate
text_to_translate = "Good Morning"

# Translate the text
translated_text = translator.translate(text_to_translate)

# Print the translated text
print(translated_text)
