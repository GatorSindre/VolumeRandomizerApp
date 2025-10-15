import tkinter as tk
import random

labelNumber = 0

def Random_1_10():
    num = random.randrange(1, 10)
    MainDisplay.config(text=num)
def Random_0_1():
    num = random.random()
    MainDisplay.config(text=num)
def RandText():
    placeholder = list("0123456789")
    for i in range(0, 10):
        num = random.randrange(0, 25)
        num += 65
        placeholder[i] = chr(num)
    placeholder = "".join(placeholder)
    MainDisplay.config(text=placeholder)

app = tk.Tk()
app.title("Random Number Generator")

MainDisplay = tk.Label(app, text=0)
MainDisplay.pack()

Button_1_10 = tk.Button(app, text="Random 1-10", command=Random_1_10)
Button_1_10.pack()

Button_0_1 = tk.Button(app, text="Random 0-1", command=Random_0_1)
Button_0_1.pack()

Button_RandText = tk.Button(app, text="Random Text", command=RandText)
Button_RandText.pack()

app.mainloop()