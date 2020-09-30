import speech_recognition as sr
from gtts import gTTS
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from io import BytesIO
import webbrowser


def sayword():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        # print('Say Something:')
        audio = r.listen(source)
        # print ('Done!')

    text = r.recognize_google(audio, language = 'hi-IN')
    return text


def say(text):
    tts = gTTS(text=text, lang='hi')
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    pygame.mixer.init()
    pygame.mixer.music.load(fp)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


say("आप मेरा नाम क्या रखना चाहेंगे")
name = sayword()
say(f"नमस्ते, मेरा नाम {name} है")
query = sayword()
print("listening...")
print(query)

if "यूट्यूब" in query:
    say("यूट्यूब खुल रहा है")
    open_google = webbrowser.get('windows-default').open('https://youtube.com')

