from tkinter import *

#Primero haces el lienzo
ventana = Tk()
ventana.geometry("500x200")#w x h

def quitar():
	ventana.destroy()

boton = Button(ventana, text= "Click me!", bg="white", fg="#C254E9")
boton.place(x=250, y=250, width=180, height=180)

boton2 = Button(ventana, text="Exit", command=quitar)
boton2.place(x=20, y=70, width=180, height=25)

ventana.mainloop()
