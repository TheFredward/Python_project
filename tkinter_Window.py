from tkinter import*
import random
import time

window = Tk()                               #Parent Window
window.geometry("1600x800+0+0")
window.title("Testing Window")

FrameOne = Frame(window, width = 1600, bg="blue", relief=SUNKEN)
FrameOne.pack(side=TOP)

FrameTwo = Frame(window, height = 700, width = 800, bg="blue", relief=SUNKEN)
FrameTwo.pack(side=LEFT)

FrameThree = Frame(window, height = 700, cursor = "dot", width = 400, bg="light gray", relief=SUNKEN)
FrameThree.pack(side=RIGHT)
FrameFour = Frame(window, height = 700, cursor = "dot", width = 400, bg="light gray", relief=SUNKEN)
FrameFour.pack(side=TOP)

firstLabel = Label(FrameOne, font=('arial', 50, 'bold'), text="Welcome to my Window", fg = "Black", bd = 10, anchor = 'w')
firstLabel.grid(row = 0, column = 0)

localtime = time.asctime(time.localtime(time.time()))
TimeLabel = Label(FrameTwo, font=('arial', 20, 'bold'), text=localtime, fg = "Black", bd = 10, anchor = 'w')
TimeLabel.grid(row = 1, column = 0)

text_Input = StringVar()
operator = " "
txtDisplay = Entry(FrameThree, font=('arial', 15), textvariable = text_Input, bd = 5, insertwidth=4, bg = "white", justify = 'right')
txtDisplay.grid(columnspan=4, row = 0, column = 0)
IDLabel = Label(FrameFour, font=('arial', 20, 'bold'), text="Enter ID Number", fg = "Black", bd = 10, anchor = 'w')
IDLabel.grid(row = 0, column = 6)

def buttonClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)
    return;

def OKClick():

    return;

def DeleteClick():
    global operator
    operator = operator[:-1]
    text_Input.set(operator)
    return;


okayButton = Button(FrameThree, padx=20, pady=16, bd = 4, fg = "black", font = ('arial', 15), text = "1", bg = "gray", command = lambda: buttonClick("1")).grid(row=1, column=0, sticky="ew")
okayButton = Button(FrameThree, padx=20, pady=16, bd = 4, fg = "black", font = ('arial', 15), text = "2", bg = "gray", command = lambda: buttonClick("2")).grid(row=1, column=1, sticky="ew")
okayButton = Button(FrameThree, padx=20, pady=16, bd = 4, fg = "black", font = ('arial', 15), text = "3", bg = "gray", command = lambda: buttonClick("3")).grid(row=1, column=2, sticky="ew")
okayButton = Button(FrameThree, padx=20, pady=16, bd = 4, fg = "black", font = ('arial', 15), text = "4", bg = "gray", command = lambda: buttonClick("4")).grid(row=2, column=0, sticky="ew")
okayButton = Button(FrameThree, padx=20, pady=16, bd = 4, fg = "black", font = ('arial', 15), text = "5", bg = "gray", command = lambda: buttonClick("5")).grid(row=2, column=1, sticky="ew")
okayButton = Button(FrameThree, padx=20, pady=16, bd = 4, fg = "black", font = ('arial', 15), text = "6", bg = "gray", command = lambda: buttonClick("6")).grid(row=2, column=2, sticky="ew")
okayButton = Button(FrameThree, padx=20, pady=16, bd = 4, fg = "black", font = ('arial', 15), text = "7", bg = "gray", command = lambda: buttonClick("7")).grid(row=3, column=0, sticky="ew")
okayButton = Button(FrameThree, padx=20, pady=16, bd = 4, fg = "black", font = ('arial', 15), text = "8", bg = "gray", command = lambda: buttonClick("8")).grid(row=3, column=1, sticky="ew")
okayButton = Button(FrameThree, padx=20, pady=16, bd = 4, fg = "black", font = ('arial', 15), text = "9", bg = "gray", command = lambda: buttonClick("9")).grid(row=3, column=2, sticky="ew")
okayButton = Button(FrameThree, padx=20, pady=16, bd = 4, fg = "black", font = ('arial', 15), text = "OK", bg = "gray", command = lambda: OKClick()).grid(row=4, column=0, sticky="ew")
okayButton = Button(FrameThree, padx=20, pady=16, bd = 4, fg = "black", font = ('arial', 15), text = "0", bg = "gray", command = lambda: buttonClick("0")).grid(row=4, column=1, sticky="ew")
okayButton = Button(FrameThree, padx=20, pady=16, bd = 4, fg = "black", font = ('arial', 15), text = "<-", bg = "gray", command = lambda: DeleteClick()).grid(row=4, column=2, sticky="ew")


window.mainloop()
