##from tkinter import *
import tkinter  as tk

ventana = tk.Tk()
#Titulo en la ventana
ventana.title("Botones")
ventana.geometry("1000x600")
boton1 = tk.Button(ventana, text = "Boton1", font = ("Calibri",20)).grid(row=0, column=0)
boton2 = tk.Button(ventana, text = "Boton2", font = ("Calibri",20)).grid(row=0, column=1)
boton3 = tk.Button(ventana, text = "Boton3", font = ("Calibri",20)).grid(row=0, column=2)
boton4 = tk.Button(ventana, text = "Boton4", font = ("Calibri",20)).grid(row=1, column=0)
boton5 = tk.Button(ventana, text = "Boton5", font = ("Calibri",20)).grid(row=1, column=1)
boton6 = tk.Button(ventana, text = "Boton6", font = ("Calibri",20)).grid(row=1, column=2)

ventana.mainloop()