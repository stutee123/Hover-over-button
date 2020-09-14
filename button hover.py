from tkinter import *

root=Tk()
root.title("Hover over button")
root.geometry("500x70")
def func():
    label = Label(root, text="The button just chnaged its color.")
    label.pack()

button = Button(root, text="Click", command=func)
button.pack()

def buttonenter(e):
    button.configure(bg="light green")
def buttonleave(e):
    button.configure(bg="SystemButtonface")

button.bind('<Enter>', buttonenter)
button.bind('<Leave>', buttonleave)

root.mainloop()
