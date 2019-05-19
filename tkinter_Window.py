from tkinter import*
import random
import time
from Dictionary import Dictionary

'''This is going to focus on the multi_window concept and focus on getting windows from different files within the same folder and properly displaying them'''
window = Tk()                               #Parent Window
window.geometry("1600x800+0+0")
window.title("Testing Window")
list = []
DC = Dictionary();
# class FrameSetup():
#     mRelief = SUNKEN
#     def __init__(self,mWindow,mHeight, mWidth,mBg):
#         self.mWindow = mWindow
#         self.mWidth = mWidth
#         self.mHeight = mHeight
#         self.mBg = mBg
#     def setFrame(self):
#         Frame(mWindow, height = self.mHeight,width = self.mWidth, bg=self.mBg, relief=mRelief)

FrameOne = Frame(window,height = 0, width = 1600, bg="blue", relief=SUNKEN)
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
#DC = Dictionary(operator)
def buttonClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

    return;
# shold pass choice password, and the password itself so that we can recall it later
def OKClick(passChoice):
    global operator
    # get value and store in passChoice
    print(passChoice)
    # have an empty dictionary to save the password but not sure if it will create a new one each time....
    passwordKeys = {}
    # check that operator is not null

    if len(operator) > 0:
        passwordKeys = dict([(passChoice,operator)])
        print(passwordKeys)
    else:
        print('No value has been input')
        return;
def DeleteClick():
    global operator
    operator = operator[:-1]
    text_Input.set(operator)
    return;

def AddClick():
    global operator
    DC.AddToArray(operator, list)
    DC.PrintList(list)
    operator = " "
    text_Input.set(operator)
    return;

class CreateButton():
    """Doc: Class that will be used to create numerical keys and later alphabet keys to display and save the values in dictionaries so that they can be refered back via keys (for the time being)"""
    # local variables in create button class
    vark = StringVar(window)
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
        # the enterButton specially made due to the command being different as well as the deleteButton. The OkClick should pass the passwordSelected choice but doesn't at the moment...only passses the firstLabel
    def enterButton(self):
        okayButton = Button(self.frameNmbr, padx = self.padx, pady = self.pady, bd = self.bd, fg = self.fg, font = self.mFont, text = self.mText, bg = self.mBg, command = lambda:  OKClick(mPassChoice)).grid(row=self.mRow, column= self.mColumn, sticky="ew")
    def deleteButton(self):
        okayButton = Button(self.frameNmbr, padx = self.padx, pady = self.pady, bd = self.bd, fg = self.fg, font = self.mFont, text = self.mText, bg = self.mBg, command = lambda: DeleteClick()).grid(row= self.mRow, column= self.mColumn, sticky="ew")
    def AddButton(self):
        okayButton = Button(self.frameNmbr, padx = self.padx, pady = self.pady, bd = self.bd, fg = self.fg, font = self.mFont, text = self.mText, bg = self.mBg, command = lambda: AddClick()).grid(row= self.mRow, column= self.mColumn, columnspan=3, sticky="ew")
    # dropDownMenu used to select password save position for retrival later on
    def dropDownMenu(self):
        vark = StringVar(window)
        PASSCHOICE = ['Select Password','pass1','pass2','pass2']
        vark.set(PASSCHOICE[0])
        w = OptionMenu(window,vark,*PASSCHOICE)
        w.pack()
        # made mPasschoice global due to scope issues, need to correct this later on or problems will occur, such as other methods/functions being able to access this variables
        global mPassChoice
        mPassChoice = vark.get()



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
okayButtonAdd = CreateButton(FrameThree, "Add", 5, 0)
okayButton_bckspc = CreateButton(FrameThree,"<-",4,2)
# create a password select dropdown menu as a CreateButton
passwordSelect = CreateButton(FrameThree,'Select Password',5,1)
passwordSelect.dropDownMenu()
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
okayButtonAdd.AddButton()
okayButton_bckspc.deleteButton()
window.mainloop()
