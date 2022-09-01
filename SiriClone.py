import pyttsx3
import wikipedia
import speech_recognition
import webbrowser

engine = pyttsx3.init("sapi5")
voices =  engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)

def open_in_browser (url):
    chrome_path ="C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    webbrowser. get (chrome_path).open(url)

def speech(text):
    print("Text to read: ",text)
    engine.setProperty('rate', 150)
    engine.setProperty('volume',0.5)
    engine.say(text)
    engine.runAndWait()
    print("Task Completed !!")

def take_command():
    r = speech_recognition.Recognizer()
    text = None
    while text is None:
        with speech_recognition.Microphone() as mic:
            speech("Hello ! What's your command! ")
            r.pause_threshold = 0.5
            r.energy_threshold = 500
            r.non_speaking_duration = 0.3
            audio = r.listen(mic)
            try:
                text = r.recognize_google(audio, language='en-IN')
                print("You said: ", text)
            except Exception as e:
                print(e)
                speech("Please repeat again !!")
                text = None
    return text

if __name__ == '__main__':
    query = str(take_command()).lower()
    if 'search' in query and 'wikipedia' in query:
        words = query.split(" ")
        stop_words = ['search', 'wikipedia', 'on', ' in ', ' for ']
        query_to_search = [word for word in words if word not in stop_words]
        search_query = " ".join(query_to_search)
        result = wikipedia.summary(search_query,sentences=2)
        speech(result)
    elif 'search' in query and 'google' in query:
        stop_words = ['search', 'google', 'in', 'on', 'for']
        query_to_search = query.split()
        result = [word for word in query_to_search if word.lower() not in stop_words]
        while len(result) == 0:
            speech("What should I search on google?")
        query = take_command().lower()
        query_to_search = query.split()
        result = [word for word in query_to_search if word.lower() not in stop_words]
        search_query = ' '.join(result)
        open_in_browser(f'https://www.google.com/search?q={search_query.replace(" ", "+")}')
        speech(f"Here is the result from Google for {search_query}")
    elif 'play' in query and 'youtube' in query:
        stop_words = ['play', 'youtube', 'in', 'on', 'for']
        query_to_search = query.split()
        result = [word for word in query_to_search if word.lower() not in stop_words]
        while len(result) == 0:
            speech("What should I play on youtube?")
        query = take_command().lower()
        query_to_search = query.split()
        resultwords = [word for word in query_to_search if word.lower() not in stop_words]
        search_query = ' '.join(resultwords)
        open_in_browser(f'https://www.youtube.com/search?q={search_query.replace(" ", "+")}')
        speech(f"Here is the result from Youtube for {search_query}")
    else:
        print("Command not recognised! ")
