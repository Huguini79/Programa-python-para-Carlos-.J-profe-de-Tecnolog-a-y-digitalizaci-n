import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.configure(bg='yellow')
root.geometry('660x550')
root.title('Programa por Hugo González Ruiz de 1 ESO D')
personas = []
def agregar():
    texto2 = texto.get('1.0', 'end-1c')
    personas.append(texto2);
def ale():
    per_ale = random.choice(personas)
    messagebox.showinfo('Persona aleatoria', f'Persona aleatoria: {per_ale}')
def borrar():
    personas.clear()
    messagebox.showinfo('Ok', 'Lista de personas eliminadas correctamente')
label = tk.Label(root, text='Bienvenido a mi programa en python por mí(Hugo)', height='2', width='60')
texto = tk.Text(root, height='2', width='25')
botónagreg = tk.Button(root, text='Agregar persona', height='2', width='40', command=agregar)
botónale = tk.Button(root, text='Mostrar persona aleatoria', height='2', width='50', command=ale)
botónborr = tk.Button(root, text='Borrar lista de personas', height='2', width='40', command=borrar)
label.grid(row=0, column=0, padx=10, pady=10)
texto.grid(row=1, column=0, padx=10, pady=10)
botónagreg.grid(row=2, column=0, padx=10, pady=10)
botónale.grid(row=3, column=0, padx=10, pady=10)
botónborr.grid(row=4, column=0, padx=10, pady=10)
root.mainloop()
