import tkinter as tk
from tkinter import font  as tkfont
import random
import time
from Dictionary import Dictionary
import sqlite3
from LoginDataBase import loginDB

class MyApplication(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MainView, LoginView):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginView")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class MainView(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # loginPage = LoginPage(self)
        self.controller = controller
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
        LogOutButton = tk.Button(self, padx=20, pady=16, bd = 4, fg = "black", font = ('arial', 15), text = "Logout", bg = "orange", command = lambda: controller.show_frame("LoginView")).grid(columnspa=3, row=8, column=1, sticky="ew")

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
        # loginPage.show()


class LoginView(tk.Frame):


    #print (LoginCredentials)
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # LoginCredentials = {
        #                 "hamzam":"9035712357",
        #                 "freddiev":"4692267036"
        #                 }
        self.usernametext = tk.StringVar()
        self.username = ""
        self.passwordtext = tk.StringVar()
        self.password = ""

        label = tk.Label(self, text="Login Page", font=('ariel',35, 'bold'))
        label.grid(columnspan=4, row = 0, column = 1)

        UsernameLabel = tk.Label(self, font=('arial', 20), text="Username: ", fg = "Black", bd = 10, anchor = 'w')
        UsernameLabel.grid(columnspan=4, row = 1, column = 1)

        PasswordLabel = tk.Label(self, font=('arial', 20), text="Password: ", fg = "Black", bd = 10, anchor = 'w')
        PasswordLabel.grid(columnspan=4, row = 2, column = 1)

        LoginButton = tk.Button(self, text="Login",command=lambda: CheckCredentials())
        LoginButton.grid(columnspan=3, row = 7, column = 5, sticky = "ew")

        UsernameInput = tk.Entry(self, font=('arial', 15), textvariable = self.usernametext, bd = 6, insertwidth=4, bg = "white", justify = 'right')
        UsernameInput.grid(columnspan=6, row = 1, column = 5)

        PasswordInput = tk.Entry(self, font=('arial', 15), show="*", textvariable = self.passwordtext, insertwidth=6, bd = 6, bg = "white", justify = 'right')
        PasswordInput.grid(columnspan=6, row = 2, column = 5)

        # FakeLabel = tk.Label(self, font=('arial', 12), text="   ", fg = "Red", bd = 10, anchor = 'w')
        # FakeLabel.grid(columnspan=6, row = 4, column = 5, sticky="ew")

        ErrorLabel = tk.Label(self, font=('arial', 12), text="Incorrect Username or Password", fg = "Red", bd = 10, anchor = 'w')
        ErrorLabel.grid_forget()

        def CheckCredentials():
            LogDB = loginDB()
            username = UsernameInput.get()
            password = PasswordInput.get()
            if LogDB.CheckDBCred(username, password):
                print('login successful')
                controller.show_frame("MainView")
                self.usernametext.set(self.username)
                self.passwordtext.set(self.password)
            else:
                ErrorLabel.grid(columnspan=6, row = 4, column = 5, sticky="ew")
            LogDB.___del___()


if __name__ == "__main__":
    root = MyApplication()
    root.wm_geometry("1500x1000")
    root.title("My Application")
    root.mainloop()
