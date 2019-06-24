from tkinter import *
ventana = Tk()
ventana.geometry("1000x600")
img = PhotoImage(file="puppy.gif")
etiqueta = Label(ventana, text="Puppy").pack()
widget =Label(ventana, image=img).pack()

ventana.mainloop()