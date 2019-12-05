print('Say Something')
#importing libraries
import speech_recognition as sr
from googlesearch import *
import webbrowser

#Listening to speech
r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source)

#Speech to Text
try:
    query=r.recognize_google(audio)
    print(query)
except Exception:
    print('Something went wrong')

#Searching the text in Chrome    
chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
    webbrowser.open("https://google.com/search?q=%s" % query)