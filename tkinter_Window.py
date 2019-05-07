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
    # check that operator is not null
    if operator is '':
        level = Toplevel()
        displayString = Label(level,text= operator, height = 800,width = 400)
        displayString.pack()
    else:
        return;

def DeleteClick():
    global operator
    operator = operator[:-1]
    text_Input.set(operator)
    return;

class CreateButton():
    """Doc: Class that will be used to create numerical keys and later alphabet keys to display and save the values in dictionaries so that they can be refered back via keys (for the time being)"""
    # local variables in create button class
    padx = 20
    pady = 16
    bd = 4
    fg = "black"
    mFont = ('arial',15)
    mBg = 'gray'
    def __init__(self,frameNmbr,mText,mRow,mColumn):
        self.frameNmbr = frameNmbr
        self.mText = mText
        self.mRow = mRow
        self.mColumn = mColumn
    def passButtonVal(self):
        okayButton = Button(self.frameNmbr, padx = self.padx, pady = self.pady, bd = self.bd, fg = self.fg, font = self.mFont, text = self.mText, bg = self.mBg, command = lambda: buttonClick(self.mText)).grid(row=self.mRow, column = self.mColumn, sticky="ew")
    def enterButton(self):
        okayButton = Button(self.frameNmbr, padx = self.padx, pady = self.pady, bd = self.bd, fg = self.fg, font = self.mFont, text = self.mText, bg = self.mBg, command = lambda:  OKClick()).grid(row=self.mRow, column= self.mColumn, sticky="ew")
    def deleteButton(self):
        okayButton = Button(self.frameNmbr, padx = self.padx, pady = self.pady, bd = self.bd, fg = self.fg, font = self.mFont, text = self.mText, bg = self.mBg, command = lambda: DeleteClick()).grid(row= self.mRow, column= self.mColumn, sticky="ew")
# okayButton = Button(FrameThree, padx=20, pady=16, bd = 4, fg = "black", font = ('arial', 15), text = "1", bg = "gray", command = lambda: buttonClick("1")).grid(row=1, column=0, sticky="ew")
# okayButton = Button(FrameThree, padx=20, pady=16, bd = 4, fg = "black", font = ('arial', 15), text = "2", bg = "gray", command = lambda: buttonClick("2")).grid(row=1, column=1, sticky="ew")
# okayButton = Button(FrameThree, padx=20, pady=16, bd = 4, fg = "black", font = ('arial', 15), text = "3", bg = "gray", command = lambda: buttonClick("3")).grid(row=1, column=2, sticky="ew")
# okayButton = Button(FrameThree, padx=20, pady=16, bd = 4, fg = "black", font = ('arial', 15), text = "4", bg = "gray", command = lambda: buttonClick("4")).grid(row=2, column=0, sticky="ew")
# okayButton = Button(FrameThree, padx=20, pady=16, bd = 4, fg = "black", font = ('arial', 15), text = "5", bg = "gray", command = lambda: buttonClick("5")).grid(row=2, column=1, sticky="ew")
# okayButton = Button(FrameThree, padx=20, pady=16, bd = 4, fg = "black", font = ('arial', 15), text = "6", bg = "gray", command = lambda: buttonClick("6")).grid(row=2, column=2, sticky="ew")
# okayButton = Button(FrameThree, padx=20, pady=16, bd = 4, fg = "black", font = ('arial', 15), text = "7", bg = "gray", command = lambda: buttonClick("7")).grid(row=3, column=0, sticky="ew")
# okayButton = Button(FrameThree, padx=20, pady=16, bd = 4, fg = "black", font = ('arial', 15), text = "8", bg = "gray", command = lambda: buttonClick("8")).grid(row=3, column=1, sticky="ew")
# okayButton = Button(FrameThree, padx=20, pady=16, bd = 4, fg = "black", font = ('arial', 15), text = "9", bg = "gray", command = lambda: buttonClick("9")).grid(row=3, column=2, sticky="ew")
# okayButton = Button(FrameThree, padx=20, pady=16, bd = 4, fg = "black", font = ('arial', 15), text = "OK", bg = "gray", command = lambda: OKClick()).grid(row=4, column=0, sticky="ew")
# okayButton = Button(FrameThree, padx=20, pady=16, bd = 4, fg = "black", font = ('arial', 15), text = "0", bg = "gray", command = lambda: buttonClick("0")).grid(row=4, column=1, sticky="ew")
# okayButton = Button(FrameThree, padx=20, pady=16, bd = 4, fg = "black", font = ('arial', 15), text = "<-", bg = "gray", command = lambda: DeleteClick()).grid(row=4, column=2, sticky="ew")
# initialize all buttons using CreateButton class and pass the necessary values that are needed
okayButton1 = CreateButton(FrameThree,"1",1,0)
okayButton2 = CreateButton(FrameThree,"2",1,1)
okayButton3 = CreateButton(FrameThree,"3",1,2)
okayButton4 = CreateButton(FrameThree,"4",2,0)
okayButton5 = CreateButton(FrameThree,"5",2,1)
okayButton6 = CreateButton(FrameThree,"6",2,2)
okayButton7 = CreateButton(FrameThree,"7",3,0)
okayButton8 = CreateButton(FrameThree,"8",3,1)
okayButton9 = CreateButton(FrameThree,"9",3,2)
okayButton = CreateButton(FrameThree,"OK",4,0)
okayButton0 = CreateButton(FrameThree,"0",4,1)
okayButton_bckspc = CreateButton(FrameThree,"<-",4,2)
okayButton1.passButtonVal()
okayButton2.passButtonVal()
okayButton3.passButtonVal()
okayButton4.passButtonVal()
okayButton5.passButtonVal()
okayButton6.passButtonVal()
okayButton7.passButtonVal()
okayButton8.passButtonVal()
okayButton9.passButtonVal()
okayButton.enterButton()
okayButton0.passButtonVal()
okayButton_bckspc.deleteButton()
window.mainloop()
