import tkinter as tk
import random
import time
from Dictionary import Dictionary



class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       firstLabel = tk.Label(self, font=('arial', 50, 'bold'), text="Welcome to my Window", fg = "Black", bd = 10, anchor = 'w')
       firstLabel.grid(row = 0, column = 0)
       list = [ ]
       self.localtime = time.asctime(time.localtime(time.time()))
       TimeLabel = tk.Label(self, font=('arial', 20, 'bold'), text=self.localtime, fg = "Black", bd = 10, anchor = 'w')
       TimeLabel.grid(row = 0, column = 6)

       self.text_Input = tk.StringVar()
       self.operator = " "
       txtDisplay = tk.Entry(self, font=('arial', 15), textvariable = self.text_Input, bd = 5, insertwidth=4, bg = "white", justify = 'right')
       txtDisplay.grid(columnspan=4, row = 3, column = 1)
       IDLabel = tk.Label(self, font=('arial', 20, 'bold'), text="Enter ID Number", fg = "Black", bd = 10, anchor = 'w')
       IDLabel.grid(columnspan=4, row = 1, column = 1)

       okayButton = tk.Button(self, padx=20, pady=16, bd = 4, fg = "black", font = ('arial', 15), text = "1", bg = "gray", command = lambda: buttonClick("1")).grid(row=4, column=1, sticky="ew")
       okayButton = tk.Button(self, padx=20, pady=16, bd = 4, fg = "black", font = ('arial', 15), text = "2", bg = "gray", command = lambda: buttonClick("2")).grid(row=4, column=2, sticky="ew")
       okayButton = tk.Button(self, padx=20, pady=16, bd = 4, fg = "black", font = ('arial', 15), text = "3", bg = "gray", command = lambda: buttonClick("3")).grid(row=4, column=3, sticky="ew")
       okayButton = tk.Button(self, padx=20, pady=16, bd = 4, fg = "black", font = ('arial', 15), text = "4", bg = "gray", command = lambda: buttonClick("4")).grid(row=5, column=1, sticky="ew")
       okayButton = tk.Button(self, padx=20, pady=16, bd = 4, fg = "black", font = ('arial', 15), text = "5", bg = "gray", command = lambda: buttonClick("5")).grid(row=5, column=2, sticky="ew")
       okayButton = tk.Button(self, padx=20, pady=16, bd = 4, fg = "black", font = ('arial', 15), text = "6", bg = "gray", command = lambda: buttonClick("6")).grid(row=5, column=3, sticky="ew")
       okayButton = tk.Button(self, padx=20, pady=16, bd = 4, fg = "black", font = ('arial', 15), text = "7", bg = "gray", command = lambda: buttonClick("7")).grid(row=6, column=1, sticky="ew")
       okayButton = tk.Button(self, padx=20, pady=16, bd = 4, fg = "black", font = ('arial', 15), text = "8", bg = "gray", command = lambda: buttonClick("8")).grid(row=6, column=2, sticky="ew")
       okayButton = tk.Button(self, padx=20, pady=16, bd = 4, fg = "black", font = ('arial', 15), text = "9", bg = "gray", command = lambda: buttonClick("9")).grid(row=6, column=3, sticky="ew")
       okayButton = tk.Button(self, padx=20, pady=16, bd = 4, fg = "black", font = ('arial', 15), text = "OK", bg = "gray", command = lambda: AddClick()).grid(row=7, column=1, sticky="ew")
       okayButton = tk.Button(self, padx=20, pady=16, bd = 4, fg = "black", font = ('arial', 15), text = "0", bg = "gray", command = lambda: buttonClick("0")).grid(row=7, column=2, sticky="ew")
       okayButton = tk.Button(self, padx=20, pady=16, bd = 4, fg = "black", font = ('arial', 15), text = "<-", bg = "gray", command = lambda: DeleteClick()).grid(row=7, column=3, sticky="ew")

       def buttonClick(numbers):
           global operator
           self.operator = self.operator + str(numbers)
           self.text_Input.set(self.operator)
           return;
           # shold pass choice password, and the password itself so that we can recall it later
       def OKClick(passChoice):
           global operator
       # get value and store in passChoice
           print(self.passChoice)
           # have an empty dictionary to save the password but not sure if it will create a new one each time....
           passwordKeys = {}
           # check that operator is not null
           if len(self.operator) > 0:
               passwordKeys = dict([(self.passChoice,self.operator)])
               print(passwordKeys)
           else:
               print('No value has been input')
               return;
       def DeleteClick():
           global operator
           self.operator = self.operator[:-1]
           self.text_Input.set(self.operator)
           return;

       def AddClick():
           global operator
           DC = Dictionary()
           DC.AddToArray(self.operator, list)
           DC.PrintList(list)
           self.operator = " "
           self.text_Input.set(self.operator)
           return;

class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 2")
       label.pack(side="top", fill="both", expand=True)

class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 3")
       label.pack(side="top", fill="both", expand=True)

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Page 1", command=p1.lift)
        b2 = tk.Button(buttonframe, text="Page 2", command=p2.lift)
        b3 = tk.Button(buttonframe, text="Page 3", command=p3.lift)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")


root = tk.Tk()
if __name__ == "__main__":

    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()
