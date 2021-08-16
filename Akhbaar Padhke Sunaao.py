import json
import requests


def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    news = requests.get("https://newsapi.org/v2/everything?sources=the-times-of-india&language=en&apiKey=661cdc6a59aa40d680cb5deb0410713f")
    news_call = news.text
    jso = json.loads(news_call)
    art = jso['articles']

    for head_lines in art:

        print(head_lines['title'])
        speak(head_lines['title'])
        speak("Next headline")
    speak("Thanks for coming")
