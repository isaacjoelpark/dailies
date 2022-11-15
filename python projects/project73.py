import sys
try:
    import pyttsx3
except ImportError:
    sys.exit()

tts = pyttsx3.init()

print("text to speech editor")

print("enter the text to speak, or quit to quit")
while True:
    text = input('> ')
    if text.upper() == 'QUIT':
        print("Thanks for Playing!")
        sys.exit()
    
    tts.say(text)
    tts.runAndWait()