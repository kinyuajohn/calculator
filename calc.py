from tkinter import *
import math
from pygame import mixer
import speech_recognition
import threading

# Initializing the mixer module from Pygame for playing audio
mixer.init()


# Defining a function that runs in a separate thread to handle audio processing
def thread_func():
    t = threading.Thread(target=audio)
    t.daemon = True
    t.start()


def click(value):
    # # Retrieve the current expression from the entry field
    ex = entryField.get()
    answer = ""

    # Perform the appropriate action based on the button value
    try:
        if value == "C":
            # Remove the last character from the expression
            ex = ex[0 : len(ex) - 1]
            entryField.delete(0, END)
            entryField.insert(0, ex)
            return

        elif value == "CE":
            # Clear the entire entry field
            entryField.delete(0, END)

        elif value == "√":
            # Calculate the square root of the expression
            answer = math.sqrt(eval(ex))

        elif value == "π":
            # Assign the value of pi to the answer
            answer = math.pi

        elif value == "cosθ":
            answer = math.cos(math.radians(eval(ex)))

        elif value == "sinθ":
            answer = math.sin(math.radians(eval(ex)))

        elif value == "tanθ":
            answer = math.tan(math.radians(eval(ex)))

        elif value == "2π":
            answer = 2 * math.pi

        elif value == "cosh":
            answer = math.cosh(eval(ex))

        elif value == "sinh":
            answer = math.sinh(eval(ex))

        elif value == "tanh":
            answer = math.tanh(eval(ex))

        elif value == chr(8731):
            answer = eval(ex) ** (1 / 3)

        elif value == "x\u02b8":
            entryField.insert(END, "**")
            return

        elif value == "x\u00B3":
            answer = eval(ex) ** 3

        elif value == "x\u00B2":
            answer = eval(ex) ** 2

        elif value == "ln":
            answer = math.log2(eval(ex))

        elif value == "deg":
            answer = math.degrees(eval(ex))

        elif value == "rad":
            answer = math.radians(eval(ex))

        elif value == "e":
            answer = math.e

        elif value == "log₁₀":
            answer = math.log10(eval(ex))

        elif value == "x!":
            answer = math.factorial(eval(ex))

        elif value == chr(247):
            entryField.insert(END, "/")
            return

        elif value == "=":
            # Evaluate the expression and assign the result to the answer
            try:
                answer = eval(ex)
            # print error when you divide a number by zero
            except ZeroDivisionError:
                answer = "Error: Division by zero"

        else:
            # Append the clicked button value to the expression
            entryField.insert(END, value)
            return

        # Update the entry field with the resulting answer
        entryField.delete(0, END)
        entryField.insert(0, answer)

    except (SyntaxError, ValueError):
        # Handle any syntax and value errors that may occur during evaluation
        pass


# Defining additional mathematical functions from audio


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero"


def mod(a, b):
    return a % b


def lcm(a, b):
    l = math.lcm(a, b)
    return l


def hcf(a, b):
    h = math.gcd(a, b)
    return h


# helper function to find numbers in a given list of text
def find_numbers(text_list):
    numbers_in_text_list = []
    for number in text_list:
        try:
            numbers_in_text_list.append(float(number))
        except ValueError:
            pass
    return numbers_in_text_list


# audio function that performs speech recognition
# and processes the recognized speech


def audio():
    # Load and play an audio file using Pygame mixer
    mixer.music.load("audio/music1.mp3")
    mixer.music.play()

    # Create a speech recognizer instance
    sr = speech_recognition.Recognizer()

    # Use the default system microphone as the audio source
    with speech_recognition.Microphone() as m:
        try:
            # Adjust for ambient noise and listen for user's voice
            sr.adjust_for_ambient_noise(m, duration=0.2)
            voice = sr.listen(m)

            # Convert the speech to text using Google's speech recognition service
            text = sr.recognize_google(voice)

            # Load and play another audio file using Pygame mixer
            mixer.music.load("audio/music2.mp3")
            mixer.music.play()

            # Split the recognized text into a list of words
            text_list = text.split(" ")
            print(text_list)

            # Check if any recognized word matches an operation and perform the operation
            for word in text_list:
                if word.upper() in operations.keys():
                    number_list = find_numbers(text_list)
                    print(number_list)
                    result = operations[word.upper()](number_list[0], number_list[1])
                    entryField.delete(0, END)
                    entryField.insert(END, result)

                else:
                    pass
        except:
            pass


# Defining a dictionary of operations that maps recognized words to their corresponding functions.

# fmt: off
operations = {
    'ADD':add,'ADDITION':add,'SUM':add,'PLUS':add, '+':add,
    'SUBTRACTION':sub , 'DIFFERENCE':sub , 'MINUS':sub , 'SUBTRACT':sub, '-':sub,
    'PRODUCT': mul, 'MULTIPLICATION': mul,'MULTIPLY': mul, 'TIMES': mul, '*': mul,
    'DIVISION': div, 'DIV': div, 'DIVIDE': div, '/': div,
    'LCM':lcm , 'HCF':hcf,
    'MOD':mod ,'REMAINDER':mod , 'MODULUS':mod 
}
# fmt:on

# Creating the main application window
root = Tk()
root.title("Scientific Calculator")
root.configure(bg="dodgerblue3")
root.geometry("680x486+100+100")

# Loading and displaying images for the calculator logo
# and microphone button using Tkinter's PhotoImage widget.
logoImage = PhotoImage(file="images/logo.png")
logoLabel = Label(root, image=logoImage, bg="dodgerblue3")
logoLabel.grid(row=0, column=0)

micImage = PhotoImage(file="images/microphone.png")
micButton = Button(
    root,
    image=micImage,
    bg="dodgerblue3",
    bd=0,
    activebackground="dodgerblue3",
    command=thread_func,
)
micButton.grid(row=0, column=7)

# Creating an entry field widget to display the current expression and result
entryField = Entry(
    root,
    font=("arial", 20, "bold"),
    bg="dodgerblue3",
    fg="white",
    bd=10,
    relief=SUNKEN,
    width=30,
)
entryField.grid(row=0, column=0, columnspan=8)

# Defining a list of button texts for the calculator
# fmt: off
button_text_list = [
    "C", "CE", "√", "+", "π", "cosθ", "tanθ", "sinθ",
    "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh",
    "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2",
    "7", "8", "9", chr(247), "ln", "deg", "rad", "e",
    "0", ".", "%", "=", "log₁₀", "(", ")", "x!"
]
# fmt: on

# Creating calculator buttons using Tkinter's Button widget,
# assigning the appropriate click function to each button
row_value = 1
column_value = 0
for i in button_text_list:
    button = Button(
        root,
        width=5,
        height=2,
        bd=2,
        relief=SUNKEN,
        text=i,
        bg="dodgerblue3",
        fg="white",
        font=("arial", 18, "bold"),
        activebackground="dodgerblue3",
        command=lambda button=i: click(button),
    )
    button.grid(row=row_value, column=column_value, pady=1)
    column_value += 1
    if column_value > 7:
        row_value += 1
        column_value = 0

# Running the Tkinter event loop to start the application
root.mainloop()
