from tkinter import *
ventana = Tk()
#AnchoxAlto
def quitar():
	ventana.destroy()

ventana.geometry("500x200")
boton = Button(ventana, text="Presioname", bg="red", fg="black")
boton.place(x=20, y=50, width=180, height=25)

boton2 = Button(ventana, text="Salir", command=quitar)
boton2.place(x=20, y=70, width=180, height=25)

ventana.mainloop()

