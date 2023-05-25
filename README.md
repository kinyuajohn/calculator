# Scientific Calculator

This is a scientific calculator program implemented using the Tkinter library in Python. It provides a graphical user interface (GUI) for performing various mathematical calculations and includes speech recognition functionality. Here's a breakdown of the code:

1. Importing the necessary modules:

```
from tkinter import \*
import math
from pygame import mixer
import speech_recognition
import threading
```

2. Initializing the mixer module from Pygame for playing audio:
   `mixer.init()`

3. Defining a function that runs in a separate thread to handle audio processing:

```
def thread_func():
    t = threading.Thread(target=audio)
    t.daemon = True
    t.start()
```

4. Implementing the click function, which is triggered when a button on the calculator GUI is clicked:

```
def click(value): # Retrieve the current expression from the entry field
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
        # ... other button actions ...
        elif value == "=":
            # Evaluate the expression and assign the result to the answer
            answer = eval(ex)
        else:
            # Append the clicked button value to the expression
            entryField.insert(END, value)
            return

        # Update the entry field with the resulting answer
        entryField.delete(0, END)
        entryField.insert(0, answer)

    except SyntaxError:
        # Handle any syntax errors that may occur during evaluation
        pass

```

5. Defining additional mathematical functions for addition, subtraction, multiplication, division, modulus, least common multiple (LCM), and highest common factor (HCF).

6. Implementing a helper function to find numbers in a given list of text:

```
def find_numbers(text_list):
    numbers_in_text_list = []
    for number in text_list:
    try:
        numbers_in_text_list.append(float(number))
    except ValueError:
        pass
    return numbers_in_text_list
```

7. Implementing the audio function that performs speech recognition and processes the recognized speech:

```
def audio(): # Load and play an audio file using Pygame mixer
mixer.music.load("music1.mp3")
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
            mixer.music.load("music2.mp3")
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
```

8. Defining a dictionary of operations that maps recognized words to their corresponding functions.

9. Creating the main application window using Tkinter:

```
root = Tk()
root.title("Scientific Calculator")
root.configure(bg="dodgerblue3")
root.geometry("680x486+100+100")
```

10. Loading and displaying images for the calculator logo and microphone button using Tkinter's PhotoImage widget.

11. Creating an entry field widget to display the current expression and result:

```
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
```

12. Defining a list of button texts for the calculator.

13. Creating calculator buttons using Tkinter's Button widget, assigning the appropriate click function to each button:

```
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
```

14. Running the Tkinter event loop to start the application:
    `root.mainloop()`
