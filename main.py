import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime

r = sr.Recognizer()

def record_audio(ask = False):
    # listens to audio
    # converts audio to string using recognize_google
    with sr.Microphone() as source:
        if ask:
            amy_speak(ask) 
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            amy_speak('Sorry, I did not get that')
        except sr.RequestError:
            amy_speak('Sorry, my speech service is down')
        return voice_data

def amy_speak(audio_string):
    # text to speech, creates audio file
    # speaks, deletes audio file
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    # difference responses
    if 'what is your name' in voice_data:
        amy_speak('My name is Amy')
    if 'what time is it' in voice_data:
        amy_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        amy_speak('Here is what I found for ' + search)
    if 'find location' in voice_data:
        location = record_audio('What is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        amy_speak('Here is the location of ' + location)
    if 'exit' in voice_data:
        exit()

time.sleep(1)
amy_speak('How can I help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)
