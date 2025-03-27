import speech_recognition as sr
import webbrowser
import pyttsx3
import pyautogui
import pyperclip
import time
# import musicLibrary
# import requests
# from openai import OpenAI
# from gtts import gTTS
# import pygame
# import os

# pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init() 
# newsapi = "<Your Key Here>"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

# def speak(text):
#     tts = gTTS(text)
#     tts.save('temp.mp3') 

#     # Initialize Pygame mixer
#     pygame.mixer.init()

#     # Load the MP3 file
#     pygame.mixer.music.load('temp.mp3')

#     # Play the MP3 file
#     pygame.mixer.music.play()

#     # Keep the program running until the music stops playing
#     while pygame.mixer.music.get_busy():
#         pygame.time.Clock().tick(10)
    
#     pygame.mixer.music.unload()
#     os.remove("temp.mp3") 

# def aiProcess(command):
#     client = OpenAI(api_key="<Your Key Here>",
#     )

#     completion = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
#         {"role": "user", "content": command}
#     ]

#     )

#     return completion.choices[0].message.content

def processCommand(c):
    if "open helloiitk" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open google" in c.lower():
        webbrowser.open("https://hello.iitk.ac.in/user/login")
        pyautogui.click(1099, 480)
        time.sleep(0.25) 
        pyautogui.press('y')
        pyautogui.press('o')
        pyautogui.press('u')
        pyautogui.press('r')
        pyautogui.press('s')
        pyautogui.press('c')
        pyautogui.press('h')
        pyautogui.press('o')
        pyautogui.press('o')
        pyautogui.press('l')
        pyautogui.press('I')
        pyautogui.press('D')

         # Wait for 1 second to ensure the click is registered
        time.sleep(0.25)
        pyautogui.click(1522,317)
        # Step 6: Paste the text
        # pyautogui.hotkey('ctrl', 'v')
        # time.sleep(1)  # Wait for 1 second to ensure the paste command is completed

        pyperclip.copy("your password")
        time.sleep(0.25)

        pyautogui.click(1159, 619)
        time.sleep(0.25)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.25)
        # Step 7: Press Enter
        pyautogui.press('enter')
    elif "lock" in c.lower():
        pyautogui.click(46, 1047)
        time.sleep(0.25)
        pyautogui.click(733, 963)
        time.sleep(0.25)
        pyautogui.click(712, 793)
        time.sleep(0.25)
        pyautogui.click(712, 793)
        # Step 5: Click at coordinates (1808, 1328)
        # pyautogui.hotkey('Windows', 'l')
        

    # elif c.lower().startswith("play"):
    #     song = c.lower().split(" ")[1]yourschoolID
    #     link = musicLibrary.music[song]
    #     webbrowser.open(link)

    # elif "news" in c.lower():
    #     r = requests.get(f"https://newsapi.org/v2/top-headlinyour password
    # es?country=in&apiKey={newsapi}")
    #     if r.status_code == 200:
    #         # Parse the JSON response
    #         data = r.json()
            
    #         # Extract the articles
    #         articles = data.get('articles', [])
            
    #         # Print the headlines
    #         for article in articles:
    #             speak(article['title'])

    # else:
    #     # Let OpenAI handle the request
    #     output = aiProcess(c)
    #     speak(output) 





if __name__ == "__main__":
    speak_old("Initializing ..Gaurav....")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=4, phrase_time_limit=2)
                # word = r.recognize_google(audio)
            # if(word.lower() == "hello"):
            #     speak_old("Ya ....Ankit .activated")
            #     # Listen for command
            #     with sr.Microphone() as source:
            #         print("Jarvis Active...")
                # audio = r.listen(source)
                command = r.recognize_google(audio)

                processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))