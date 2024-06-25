import random
import re
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser

responses = {
    "hi": ["Hello! How can I assist you today?", "Hi there! What can I do for you?", "Greetings! What can I help you with?"],
    "how are you": ["I'm doing well, thank you for asking! How can I assist you?", "I'm fine, thanks! What can I do for you?", "I'm feeling great today! What can I help you with?"],
    "what is your name": ["My name is Jarvis, and I'm here to assist you!", "I'm Jarvis, your personal assistant!", "I'm called Jarvis, how can I help you today?"],
    "what time is it": ["It's currently {time}.", "The time is {time}.", "It's {time} right now."],
    "what is the weather like": ["The weather is {weather}.", "It's currently {weather}.", "The weather outside is {weather}."],
    "what is the capital of {country}": ["The capital of {country} is {capital}.", "The capital city of {country} is {capital}.", "The capital of {country} is {capital}, did you need more information about {country}?"],
    "tell me a joke": ["Why don't scientists trust atoms? Because they make up everything!", "Why was the computer cold? Because it left its Windows open!", "Why don't oysters give to charity? Because they're shellfish!"],
    "who is": ["I'm not sure, would you like me to search for information about {person}?", "I think {person} might be {description}. Would you like me to look up more information?", "I'm not familiar with {person}. Would you like me to find more information?"],
    "search for": ["Sure, what would you like me to search for?", "Of course! What do you want me to look up?", "No problem, what should I search for?"],
    "bye": ["Goodbye!", "Bye!", "See you later!"],
    "default": ["I'm sorry, I don't understand.", "Could you please rephrase that?", "I'm not sure what you mean."],
}

time_regex = re.compile(r"what time is it")
weather_regex = re.compile(r"what is the weather like")
capital_regex = re.compile(r"what is the capital of (.*)")
who_is_regex = re.compile(r"who is (.*)")
search_regex = re.compile(r"search for (.*)")

recognizer = sr.Recognizer()
engine = pyttsx3.init()

recognizer.device_index = 2

def get_response(user_input):
    user_input = user_input.lower().strip()
    
    # Check if input matches regular expressions
    time_match = re.match(time_regex, user_input)
    weather_match = re.match(weather_regex, user_input)
    capital_match = re.match(capital_regex, user_input)
    who_is_match = re.match(who_is_regex, user_input)
    search_match = re.match(search_regex, user_input)
        
    if time_match:
        # Replace {time} placeholder
        current_time = datetime.datetime.now().strftime("%H:%M")
        return random.choice(responses["what time is it"]).format(time=current_time)
    elif weather_match:
        # Replace {weather} placeholder
        current_weather = "sunny"
        return random.choice(responses["what is the weather like"]).format(weather=current_weather)
    elif capital_match:
        # Replace {country} and {capital} placeholders
        country = capital_match.group(1)
        capital = "unknown"
        return random.choice(responses["what is the capital of {country}"]).format(country=country, capital=capital)
    elif who_is_match:
        # Replace {person} and {description} placeholders using Wikipedia API
        person = who_is_match.group(1)
        try:
            description = wikipedia.summary(person, sentences=1)
        except wikipedia.exceptions.PageError:
            description = "not found"
        return random.choice(responses["who is"]).format(person=person, description=description)
    elif search_match:
        query = search_match.group(1)
        engine.say(f"Opening Google search for {query}")
        engine.runAndWait()
        search_url = f"https://www.google.com/search?q={query}"
        webbrowser.open(search_url)
        return None
    elif user_input in responses:
       return random.choice(responses[user_input])
    else:
        return random.choice(responses["default"])
    
def get_voice_input():
    # Use microphone to record user input
    with sr.Microphone(device_index=recognizer.device_index) as source:
        print("Say something!")
        audio = recognizer.listen(source)
    
    try:
        user_input = recognizer.recognize_google(audio)
        print(f"You said: {user_input}")
    except sr.UnknownValueError:
        user_input = None
        print("Sorry, I did not understand.")
    except sr.RequestError as e:
        user_input = None
        print(f"Sorry, could not request results from Google Speech Recognition service; {e}")
    
    return user_input

def speak(response):

    engine.say(response)
    engine.runAndWait()

def main():

    speak("Hello! I am Jarvis, your personal assistant. How can I assist you today?")
    
    while True:

       user_input = get_voice_input()
        
       if user_input:
            response = get_response(user_input)
            
            if response:
                speak(response)
            
            if "bye" in user_input:
                speak("Goodbye! Have a great day!")
                break

if __name__ == "__main__":
    main()
