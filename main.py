import requests
from bs4 import BeautifulSoup
import pyttsx3

engine = pyttsx3.init('sapi5')

voice = engine.getProperty('voices')  # getting details of current voice

engine.setProperty('voice', voice[0].id)
def speak(audio):
    engine.say(audio)

    engine.runAndWait()  # Without this command, speech will not be audible to us.

speak("Welcome To Code Scraper By Zeeshan Khalid ......... Okay Write Full Domain Name With http://")
while True:

    url = input('Write The Name Of The WebSite You Want To Scrap (q to quit) :')

    if ('.com' not in url):
        print('write the Correct domain name')

    if url == '.com' or len(url) > 63:
        print('Refine Your Query')
    if (url == 'q'):
        print('Thanks For Your Using !!!')
        exit()

    if 'http://' not in url:
        try:
            print('Also Write http:// In The Starting')
        except:
            print('Put An http:// In The Starting')
    if 'http://' in url:
        context = requests.get(url)
        r = requests.get(url)
        html = r.content
        # print(html)
        soup = BeautifulSoup(html, 'html.parser')
        print(soup.prettify)
