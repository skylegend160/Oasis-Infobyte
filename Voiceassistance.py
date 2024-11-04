import speech_recognition as aa
import pyttsx3
import datetime
import pywhatkit
import wikipedia

listener = aa.Recognizer()

machine = pyttsx3.init()

def talk(text):
        machine.say(text)
        machine.runAndWait()

def input_instruction():
    global instruction
    try:
        with aa.Microphone() as origin:
            print("listening........")
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            if "shilpi" in instruction:
                instruction = instruction.replace('shilpi', "")
                print(instruction)
                  
    except:
        pass
    return instruction
    
def play_shilpi():
    
    instruction = input_instruction()
    print(instruction)
    if "play" in instruction:
        song = instruction.replace('play', "")
        talk("playing" + song)
        pywhatkit.playonyt(song)
        
    elif 'time'   in instruction:
        time = datetime.datetime.now().strftime('%H:%M:%S')
        talk('Current time is ' + time)
        
    elif 'date' in instruction:
        date = datetime.datetime.nom().strftime('%d /%m /%y')
        talk("Today is " + date)
        
    elif 'how are you' in instruction:
        talk("I am good, how are you?")
        
    elif 'what is your name' in instruction:
        talk("My name is Shilpi, what can i do for you")
    
    elif 'who is' in instruction:
        human = instruction.replace('who is ', "")
        info = wikipedia.summary(human, 1)
        print(info)
        talk(info)
        
    else:
        talk("I cant understand what you are saying")
play_shilpi()