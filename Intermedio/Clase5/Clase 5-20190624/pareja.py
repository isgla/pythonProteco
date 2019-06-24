from tkinter import *
ventana = Tk()
ventana.title("Cuestionario de la pareja ideal")
ventana.geometry("500x500")

def eleccion():
	if opcion.get()==1:
		mensaje.set("Eres bien interesad@")

	elif opcion.get()==2:
		mensaje.set("Tienes muy buenos gustos")

	elif opcion.get()==3:
		mensaje.set("Ayyyy mi vida")

	elif opcion.get()==4:
		mensaje.set("Que bonito, engorden juntos")

#Recuperar la opción seleccionada por el usuario
opcion = IntVar()
#Mensaje mostrado en pantalla
mensaje = StringVar()
#Decorando pantalla
etiqueta1 = Label(ventana, text="¿Qué ves en el/ella?").place(x=20, y=40)
etiqueta2 = Label(ventana, textvariable=mensaje).place(x=20,y=170)

op1 = Radiobutton(ventana, text="Tiene dinero", value=1, variable=opcion).place(x=20,y=60)
op1 = Radiobutton(ventana, text="Es ingenier@", value=2, variable=opcion).place(x=20,y=80)
op1 = Radiobutton(ventana, text="Tiene bonitos sentimientos", value=3, variable=opcion).place(x=20,y=120)

op1 = Radiobutton(ventana, text="Tiene buen apetito", value=4, variable=opcion).place(x=20,y=150)

boton = Button(ventana, text="Intentar", command=eleccion).place(x = 20, y=190)

ventana.mainloop()
