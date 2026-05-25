import pyttsx3
engine = pyttsx3.init()
print("Welcome to robospeaker")
while True:
    x = input("Enter what you want me to speak: ")
    if x.lower() == "q":
        print("Terminated!!")
        break
    engine.say(x)
    engine.runAndWait()