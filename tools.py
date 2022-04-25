from tkinter import *
window = Tk()
window.title("Test")
window.geometry("400x200")
C = Canvas(window, bg="blue", height=250, width=300)
coord = 10, 50, 240, 210
arc = C.create_arc(coord, start=0, extent=150, fill="red")
C.pack()
window.mainloop()
