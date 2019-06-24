#from tkinter import *
import tkinter as tk
ventana = tk.Tk()
ventana.title("Botones")
ventana.geometry("1000x600")
boton1 = tk.Button(ventana,text="Boton1", activebackground = "black").grid(row=0, column=0)
boton2 = tk.Button(ventana,text="Boton2", activebackground = "black").grid(row=0, column=1)
boton3 = tk.Button(ventana,text="Boton3", font=("Arial",30)).grid(row=0, column=2)
boton4 = tk.Button(ventana,text="Boton4", padx=40, pady=10).grid(row=1, column=0)
boton5 = tk.Button(ventana,text="Boton5").grid(row=1, column=1)
boton6 = tk.Button(ventana,text="Boton6").grid(row=1, column=2)

ventana.mainloop()
