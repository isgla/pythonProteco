from tkinter import *
ventana = Tk()
ventana.geometry("1000x600")
img = PhotoImage(file = "hola.gif")
etiqueta = Label(ventana, text="Hola").pack()
widget = Label(ventana, image=img).pack()
ventana.mainloop()