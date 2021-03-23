import tkinter as tk 
import RPi.GPIO as GPIO
import time
#pin setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

MorseCodeGUI = tk.Tk()
MorseCodeGUI.title("Mose Code Generator") #set name
MorseCodeGUI.geometry("400x200") #set size
MorseDict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '_': '..--.-'}

#dash
def Dash():
    GPIO.output(7, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(7, GPIO.LOW)
    time.sleep(0.5)
#dot
def Dot():
    GPIO.output(7, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(7, GPIO.LOW)
    time.sleep(0.5)

def MorseButton():
    stringtxt = txtvar.get().upper()
    print(stringtxt)
    if len(stringtxt) > 12: #check how long the string is, if its over 12 characters then print that the string is too long
        print("too long, max 12 characters")
    else:
        #do morse code
        for letter in stringtxt: #for each letter of the string the user types
            print("Letter: " + letter + " Morse Code: " + MorseDict[letter])
            for dashdot in MorseDict[letter]: #for each dash and dot in the dictionary
                if(dashdot == '.'):
                    Dot()
                else:
                    Dash()


txtvar = tk.StringVar()

txtbox = tk.Entry(MorseCodeGUI, width = 15, textvariable = txtvar)
txtbox.grid(column = 0, row = 0)

entrybutton = tk.Button(MorseCodeGUI, text="Enter",bg="green", command=MorseButton)
entrybutton.grid(column = 1, row = 0)