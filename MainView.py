import tkinter as tk
import random
import time

LARGE_FONT = ("Verdana", 12)
class MainView(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        #SP = StartPage(self)

        self.frames = { }

        frame = StartPage(container, self)
        #frame = MainPage(container, self)
        self.frames[StartPage] = frame
        #self.frames[MainPage] = frame
        #self.frames[MainPage] = MainPage(container, self)

        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        buttonframe = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        label = tk.Label(self, text = "Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        MP = MainPage(controller, self)
        b1 = tk.Button(buttonframe, text="Page 1", command=MP.lift)
        MP.place(in_=buttonframe, x=0, y=0, relwidth=1, relheight=1)
        b1.pack(side="left")

class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # FrameOne = tk.Frame(self,height = 0, width = 1600, bg="blue")
        # FrameOne.pack(side="top")
        #
        # FrameTwo = tk.Frame(self, height = 700, width = 800, bg="blue")
        # FrameTwo.pack(side="left")
        #
        # FrameThree = tk.Frame(self, height = 700, cursor = "dot", width = 400, bg="light gray")
        # FrameThree.pack(side="right")
        # FrameFour = tk.Frame(self, height = 700, cursor = "dot", width = 400, bg="light gray")
        # FrameFour.pack(side="top")

        firstLabel = tk.Label(self, font=('arial', 50, 'bold'), text="Welcome to my Window", fg = "Black", bd = 10, anchor = 'w')
        firstLabel.grid(row = 0, column = 0)

        self.localtime = time.asctime(time.localtime(time.time()))
        TimeLabel = tk.Label(self, font=('arial', 20, 'bold'), text=self.localtime, fg = "Black", bd = 10, anchor = 'w')
        TimeLabel.grid(row = 1, column = 0)

        self.text_Input = tk.StringVar()
        operator = " "
        txtDisplay = tk.Entry(self, font=('arial', 15), textvariable = self.text_Input, bd = 5, insertwidth=4, bg = "white", justify = 'right')
        txtDisplay.grid(columnspan=4, row = 0, column = 0)
        IDLabel = tk.Label(self, font=('arial', 20, 'bold'), text="Enter ID Number", fg = "Black", bd = 10, anchor = 'w')
        IDLabel.grid(row = 0, column = 6)


app = MainView()
app.mainloop()
