
from translate import Translator
from gtts import gTTS
import os
from playsound import playsound

def translate_and_play(sentence, target_language):
    # Translate the sentence to the target language
    translator = Translator(to_lang=target_language)
    translation = translator.translate(sentence)
    translated_text = translation
    return translated_text



sentence = "Good Morning"
target_language = "ml"  # Malayalam language code

text = translate_and_play(sentence, target_language)

speak = gTTS(text=text, lang="en", slow=False)

speak.save("captured_voice.mp3")

# Using OS module to run the translated voice.
playsound('captured_voice.mp3')
os.remove('captured_voice.mp3')

# Printing Output
print(text)