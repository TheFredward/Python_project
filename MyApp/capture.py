import cv2, time
# import tkinter as well as messagebox to display ErrorLabel
import tkinter as tk
from tkinter.messagebox import showinfo

class capture():

    def __init__(self):
        # initalize camera
        self.video=cv2.VideoCapture(0)
        # create a wndow to display error, using topLevel to show it on top of the mainApp
        win = tk.Toplevel()
        win.wm_title("Error")
        l = tk.Label(win, text='ErrorLabel')
        # display in the center of the mainApp screen
        l.grid(row=0, column=0)

        # Determine if the camera is available\
        if self.video is None or not self.video.isOpened():
            showinfo("Error","Camera not available, use other credentials" )

    def get_frame(self):
        a=0
        while True:
            a = a + 1
            check, frame = self.video.read()

            print(check)
            print(frame)

            cv2.imshow("capturing", frame)

            # cv2.waitKey(0)

            key=cv2.waitKey(1)

            if key == ord('q'):
                break

        print(a)

        self.video.release()
        cv2.destroyAllWindows()
