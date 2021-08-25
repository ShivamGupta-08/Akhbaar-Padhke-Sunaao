import json
import requests


def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    news = requests.get("https://newsapi.org/v2/everything?sources=the-times-of-india&language=en&apiKey=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    news_call = news.text
    jso = json.loads(news_call)
    art = jso['articles']
    for index,head_lines in enumerate(art):
        print(index,head_lines['title'])
        speak(head_lines['title'])
        if index != 19:
            print("Next headline")
            speak("Next headline")
            break
    print("Thanks for coming")
    speak("Thanks for coming")
