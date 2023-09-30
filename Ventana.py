import tkinter as tk

# Crea la ventana
ventana = tk.Tk()

# Establece el título de la ventana
ventana.title("Mi primera ventana")

# Establece el tamaño de la ventana
ventana.geometry("500x500")

# Moificar el color de la ventana
ventana.config(bg= "red")

# Boton creado (lugar donde estara, lo que se muestra en el boton)
Boton = tk.Button(ventana, text="Hola mundo")

# agregado a la ventana
Boton.pack()
# Muestra la ventana
ventana.mainloop()
