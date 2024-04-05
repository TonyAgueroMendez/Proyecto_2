# This is a sample Python script.
import tkinter
import sys
# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
ventana= tkinter.Tk()

# Configurar el título de la ventana
ventana.title("Renta Card Los Patitos")

# Establecer el tamaño de la ventana
ventana.geometry("300x200")

# Agregar una etiqueta a la ventana
etiqueta = tkinter.Label(text="¡RENTA CAR!")
etiqueta.pack()
etiqueta.config(font=("Arial", 14, "bold"))
etiqueta_usuario = tkinter.Label(text="MENU PRINCIPAL")
etiqueta_usuario.pack()
etiqueta_usuario.config(font=("Arial", 14, "bold"))
boton_Ingresar = tkinter.Button(text="Ingresar")
boton_Ingresar.place(x=30, y=70)
boton_Ingresar.config(fg="blue", bg="light blue", font=("Arial", 12, "bold"))
boton_Editar = tkinter.Button(text="Editar")
boton_Editar.place(x=120, y=70)
boton_Editar.config(fg="blue", bg="light blue", font=("Arial", 12, "bold"))
boton_Mostrar = tkinter.Button(text="Mostrar")
boton_Mostrar.place(x=190, y=70)
boton_Mostrar.config(fg="blue", bg="light blue", font=("Arial", 12, "bold"))
boton_Eliminar = tkinter.Button(text="Eliminar")
boton_Eliminar.place(x=70, y=120)
boton_Eliminar.config(fg="blue", bg="light blue", font=("Arial", 12, "bold"))
boton_Salir = tkinter.Button(text="Salir")
boton_Salir.place(x=170, y=120)
boton_Salir.config(fg="red", bg="light blue", font=("Arial", 12, "bold"))




def funcion_ingresar():

    print("Ingresar de la clase mensaje en consola")

def funcion_Editar():

    print("Editar de la clase mensaje en consola")

def funcion_Mostrar():

    print("Mostrar de la clase mensaje en consola")

def funcion_Eliminar():

    print("Eliminar de la clase mensaje en consola")

def funcion_Salir():
    sys.exit()


boton_Ingresar.config(command=funcion_ingresar)
boton_Editar.config(command=funcion_Editar)
boton_Mostrar.config(command=funcion_Mostrar)
boton_Eliminar.config(command=funcion_Eliminar)
boton_Salir.config(command=funcion_Salir)

# Iniciar el bucle principal de la ventana
ventana.mainloop()
