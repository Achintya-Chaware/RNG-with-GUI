import tkinter
import random
import time

set = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
x = 0

def func():
    time.sleep(1)
    if (len(set) == 0):
       disp.set("Limit Reached!")
    else:
        a = random.randint(0, len(set)-1)
        disp.set(str(set[a]))
        set.pop(a)


gui = tkinter.Tk()
gui.title("Random Number Generator")
disp = tkinter.StringVar()
label = tkinter.Label(gui, textvariable = disp, height = 2, width = 20, font = ("Helvetica", "152", "bold"))
label.pack()
B = tkinter.Button(gui, text ="Generate a Random Number", command = func, height = 3, width = 25, font = ("Helvetica", "24", "bold"), relief = tkinter.GROOVE)
B.pack()
gui.mainloop()

