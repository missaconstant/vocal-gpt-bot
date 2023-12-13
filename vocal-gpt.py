#!/usr/bin/env python3
import speech_recognition as sr
import openai
import pyttsx3

openai.api_key = 'YOUR_OPEN_API_KEY'
engine = pyttsx3.init()

# list our microphones
def listMicrophone():
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))


# obtain audio from the microphone
def voiceToText():
    r = sr.Recognizer()
    with sr.Microphone(1) as source:    
        print("Say something!")
        audio = r.listen(source)
        text = r.recognize_google(audio, None, language='fr-FR')
        print("J'ai dit: \"{0}\"".format(text))
    return text


# get answer from openai api
def getChatGPTAnswer(text: str):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt = text,
        temperature = 0,
        max_tokens = 100,
        top_p = 1.0,
        frequency_penalty = 0.2,
        presence_penalty = 0.0,
    )
    res: str = response.choices[0].text
    print(res.strip())
    return res.strip()


# read text to audio
def readText(text):
    engine.say(text)
    engine.runAndWait()

while True:
    textToTalk = voiceToText()
    
    if len(textToTalk) != 0:
        chatAnswer = getChatGPTAnswer(textToTalk)
        readText(chatAnswer)
    
