from tkinter import *
import math


def click(value):
    ex = entryField.get()
    answer = ""

    try:
        if value == "C":
            ex = ex[0 : len(ex) - 1]
            entryField.delete(0, END)
            entryField.insert(0, ex)
            return

        elif value == "CE":
            entryField.delete(0, END)

        elif value == "√":
            answer = math.sqrt(eval(ex))

        elif value == "π":
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
            answer = eval(ex)

        else:
            entryField.insert(END, value)
            return

        entryField.delete(0, END)
        entryField.insert(0, answer)

    except SyntaxError:
        pass


def audio():
    print()


root = Tk()
root.title("Scientific Calculator")
root.configure(bg="dodgerblue3")
root.geometry("680x486+100+100")

logoImage = PhotoImage(file="logo.png")
logoLabel = Label(root, image=logoImage, bg="dodgerblue3")
logoLabel.grid(row=0, column=0)

micImage = PhotoImage(file="microphone.png")
micButton = Button(
    root,
    image=micImage,
    bg="dodgerblue3",
    bd=0,
    activebackground="dodgerblue3",
    command=audio,
)
micButton.grid(row=0, column=7)

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

# fmt: off
button_text_list = [
    "C", "CE", "√", "+", "π", "cosθ", "tanθ", "sinθ",
    "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh",
    "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2",
    "7", "8", "9", chr(247), "ln", "deg", "rad", "e",
    "0", ".", "%", "=", "log₁₀", "(", ")", "x!"
]
# fmt: on

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


root.mainloop()
