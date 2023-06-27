import os
import openai
from config import apikey
import win32com.client
import speech_recognition as sr
import webbrowser
import datetime

chatStr = ""
speaker = win32com.client.Dispatch("SAPI.SpVoice")

def ai(prompt):
    openai.api_key = apikey
    text = f"Openai response for prompt: {prompt} \n********************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: wrap this inside a try catch block
    # print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # with open(f"Openai/prompt- {random.randint(1,2343434356)}","w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()},text", "w") as f:
        f.write(text)

def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"Friday: {query}\n Friday: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: wrap this inside a try catch block
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]




def say(text):
    speaker.Speak(text)

def wishme():
    hour = int(datetime.datetime.now().hour)
    if 12 > hour >= 0:
        say("Good Morning Chakri!")
    elif 16 > hour >= 12:
        say("Good Afernoon Chakri!")
    elif 20 > hour >= 16:
        say("Good Evening Chakri!")
    else:
        say("complet your work and have a great sleep Chakri")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("recognising...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some error occurred. Sorry from Friday"

s = "Hello I am Friday AI"
say(s)
wishme()
while True:
    print("Listening...")
    query = takeCommand()
    sites = [["youtube","http://www.youtube.com"],["wikipedia","http://www.wikipedia.com"],["google","https://www.google.com"],["leetcode","https://leetcode.com/"],["chatgpt","https://chat.openai.com/"]]
    for site in sites:
        if f"open {site[0]}" in query.lower():
            say(f"Opening {site[0]} Chakri...")
            webbrowser.open(site[1])
            exit()
    if "the time" in query.lower():
        strfTime = datetime.datetime.now().strftime("%H:%M:%S")
        say(f"Chakri the time is {strfTime}")
    elif "Using artificial intelligence".lower() in query.lower():
        ai(prompt = query)
    elif "Friday Stop".lower() in query.lower():
        say("thank you Chakri,I hope you had a good time with me, byee")
        exit()
    elif "reset chat".lower() in query.lower():
        chatStr = ""
    else:
        print("chatting")
        chat(query)