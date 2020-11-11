import speech_recognition as sr
import pyttsx3
import random
import serial
import numpy as np

engine = pyttsx3.init()
r = sr.Recognizer()
ser = None

random = random.randint(1,5)

joke1 = "As my two sons were climbing into the back seat of our car, Eric, five, yelled, I call the left side! That didn’t sit well with Ron, four. No, I want the left side! I want the left side! No, I want the left side! Intervening, I said, Since Eric is older, he can have the left side. Thanks, Dad! said Eric. Which side is left?"
joke2 = "What english word has three consecutive double letters?"
joke3 = "Thinking no one could hear me as I loaded a UPS tractor trailer, I began to whistle. I was really getting into it when a coworker in the next trailer poked his head in. You know, I always used to wish I could whistle, he said. Now I just wish you could."
joke4 = "There were two muffins in an oven. One muffin says, it is really hot in here. The other muffin says, Ahh! A talking muffin!"
joke5 = "There are two ducks in a pond. One duck says quack quack. The other duck says I was about to say that"
joke6 = "I invented a new word: Plagiarism!"
joke7 = "Did you hear about the mathematician who’s afraid of negative numbers? He’ll stop at nothing to avoid them"


def sendData(floor):
    print("func called")
    with serial.Serial('/dev/cu.usbmodem14101', 9600) as ser:
        x = ser.readline()
        print(x)

        ser.write(floor.encode())

        y = ser.readline()
        print(y)

        ser.close()

with sr.Microphone() as source:
    print("State Floor :")
    engine.say("State What Floor You Would Like To Go To")
    engine.runAndWait()
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))

        if text == "first floor":
            print("Going to first floor")
            engine.say("Going To First Floor")
            engine.runAndWait()
            sendData("first")
        elif text == "second floor":
            print("Going to second floor")
            engine.say("Going To Second Floor")
            engine.runAndWait()
            sendData("second")
        elif text == "third floor":
            print("Going to third floor")
            engine.say("Going To Third Floor")
            engine.runAndWait()
            sendData("third")
        elif text == "fourth floor":
            print("Going to fourth floor")
            engine.say("Going To Fourth Floor")
            engine.runAndWait()
            sendData("fourth")

    #    elif text == "tell me a riddle":
        #    if random == 1:
            #    print("Only one color, but not one size, stuck at the bottom, yet easily flies; present in sun, but not in rain; doing no harm, and feeling no pain. What am I?")

        #    elif random == 2:
        #        print("Poor people have it. Rich people need it. If you eat it, you’ll get sick or maybe die. What is it?")
        #    elif random == 3:
        #        print("What word in the English language does the following: the first two letters signify a male, the first three letters signify a female, the first four letters signify a great, while the entire world signifies a great woman. What is the word?")
        #    elif random == 4:
        #        print("I have keys, but no locks and space, and no rooms. You can enter, but you can’t go outside. What am I?")
        #    elif random == 5:
        #        print("What are the next three letters in this combination? OTTFFSS ")
        #    elif random == 6:
        #        print ("What comes once in a minute, twice in a moment, but never in a thousand years?")
        #    elif random == 7:
        #        print("You can carry it everywhere you go, and it does not get heavy. What is it?")

    #    elif text == "tell me a joke":
    #        print("this works")
    #        if random == 1:
    #            print(joke1)
        #        engine.say(joke1)
        #        engine.runAndWait()
    #        elif random == 2:
    #            print(joke2)
    #            engine.say(joke2)
    #            engine.runAndWait()
    #        elif random == 3:
    #            print(joke3)
            #    engine.say(joke3)
        #        engine.runAndWait()
        #    elif random == 4:
        #        print(joke4)
            #    engine.say(joke4)
        #        engine.runAndWait()
    #        elif random == 5:
        #        print(joke5)
        #        engine.say(joke5)
        #        engine.runAndWait()
        #    elif random == 6:
        #            print(joke6)
        #            engine.say(joke6)
        #            engine.runAndWait()
        #    elif random == 7:
        #        print(joke7)
        #        engine.say(joke7)
        #        engine.runAndWait()
        #    elif random == 8:
        #        print(joke8)
        #        engine.say(joke8)
        #        engine.runAndWait()

        else:
            engine.say("Invalid Floor. Try Again")
            engine.runAndWait()

    except:
        print("Sorry could not recognize what you said")
        #engine.say("Invalid Floor. Try Again")
        #engine.runAndWait()
