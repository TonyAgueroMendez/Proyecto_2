
import tkinter # Importa el módulo tkinter de la biblioteca estándar de Python.
import sys # Permite acceder a información y funciones específicas del sistema
import time # Proporciona varias funciones para trabajar con tareas relacionadas con el tiempo.

ventana= tkinter.Tk() # Crear la ventana principal de tu interfaz gráfica en Python.


ventana.title("Renta Card Los Patitos") # Configurar el título de la ventana


ventana.geometry("400x350") # Establecer el tamaño de la ventana


etiqueta = tkinter.Label(text="¡RENTA CAR!") # Agregar una etiqueta a la ventana
etiqueta.pack()
etiqueta.config(font=("Arial", 14, "bold"))
lb_Archivo = tkinter.Label(text="MANEJO DE ARCHIVOS") # Agregar una etiqueta a la ventana
lb_Archivo.pack()
lb_Archivo.config(font=("Arial", 14, "bold"))
lb_Archivo.place(x=100, y=170)
etiqueta_usuario = tkinter.Label(text="MENU PRINCIPAL") # Agregar una etiqueta a la ventana
etiqueta_usuario.pack()
etiqueta_usuario.config(font=("Arial", 14, "bold"))
boton_Ingresar = tkinter.Button(text="Ingresar") # Agrega un botón ingresar a la ventana
boton_Ingresar.place(x=90, y=70)
boton_Ingresar.config(fg="blue", bg="light blue", font=("Arial", 12, "bold"))
boton_Editar = tkinter.Button(text="Editar") # Agrega un botón Editar a la ventana
boton_Editar.place(x=230, y=120)
boton_Editar.config(fg="blue", bg="light blue", font=("Arial", 12, "bold"))
boton_Mostrar = tkinter.Button(text="Mostrar") # Agrega un mostrar ingresar a la ventana
boton_Mostrar.place(x=230, y=70)
boton_Mostrar.config(fg="blue", bg="light blue", font=("Arial", 12, "bold"))
boton_Eliminar = tkinter.Button(text="Eliminar") # Agrega un botón eliminar a la ventana
boton_Eliminar.place(x=90, y=120)
boton_Eliminar.config(fg="blue", bg="light blue", font=("Arial", 12, "bold"))
boton_GuardarArchivo= tkinter.Button(text="Guardar Archivo") # Agrega un botón guardar archivo a la ventana
boton_GuardarArchivo.place(x=220, y=200)
boton_GuardarArchivo.config(fg="blue", bg="light blue", font=("Arial", 12, "bold"))
boton_ModificarArchivo= tkinter.Button(text="Modificar Archivo") # Agrega un botón modificar archivo a la ventana
boton_ModificarArchivo.place(x=50, y=200)
boton_ModificarArchivo.config(fg="blue", bg="light blue", font=("Arial", 12, "bold"))
boton_EliminarArchivo= tkinter.Button(text="Eliminar Archivo") # Agrega un botón eliminar archivo a la ventana
boton_EliminarArchivo.place(x=230, y=240)
boton_EliminarArchivo.config(fg="blue", bg="light blue", font=("Arial", 12, "bold"))
botonDiccionario= tkinter.Button(text="Diccionario de autos") # Agrega un botón para ver la descripción de autos
botonDiccionario.place(x=40, y=240)
botonDiccionario.config(fg="blue", bg="light blue", font=("Arial", 12, "bold"))
botontupla= tkinter.Button(text="Precios de renta") # Agrega un botón para ver los precios de renta de autos
botontupla.place(x=30, y=290)
botontupla.config(fg="blue", bg="light blue", font=("Arial", 12, "bold"))
boton_Salir = tkinter.Button(text="Salir") # Agrega un botón para salir del programa
boton_Salir.place(x=180, y=290)
boton_Salir.config(fg="red", bg="black", font=("Arial", 12, "bold"))

import Funciones # importa la clase funciones
Funciones.CrearDisponibilidadAutos()

# Esta funcion llama la función ingresar de la clase funciones, ingresa todos los registros de renta con sus datos correspondientes
def Funcion_ingresar():
    Funciones.Clear_console()
    ventana.withdraw()
    Funciones.Crear_RentaFactory()
    time.sleep(8)
    Funciones.Clear_console()
    ventana.deiconify()

# Esta función llama la función editar de la clase funciones, edita los datos de algún registro ya ingresado.
def Funcion_Editar():
    Funciones.Clear_console()
    ventana.withdraw()
    Funciones.editarRenta()
    time.sleep(3)
    Funciones.Clear_console()
    ventana.deiconify()

# Esta función llama la función mostrar de la clase funciones, y muestra todos los datos de los registros guardados.
def Funcion_Mostrar():
    Funciones.Clear_console()
    ventana.withdraw()
    Funciones.To_string()
    time.sleep(10)
    Funciones.Clear_console()
    ventana.deiconify()

# Esta función llama la función eliminar de la clase funciones, para eliminar un registro.
def Funcion_Eliminar():
    Funciones.Clear_console()
    ventana.withdraw()
    Funciones.EliminarRenta()
    time.sleep(5)
    Funciones.Clear_console()
    ventana.deiconify()

# Esta función llama la función guardar archivos de la clase funciones, para guardar los datos en el archivo txt.
def Funcion_GuardarArchivo():
    Funciones.Clear_console()
    ventana.withdraw()
    Funciones.GuardarArchivo()
    ventana.deiconify()

# Esta función llama la función modificar archivos de la clase funciones, para modificar los datos en el archivo txt.
def Funcion_ModificarArchivo():
    Funciones.Clear_console()
    ventana.withdraw()
    Funciones.EditarArchivo()
    time.sleep(5)
    ventana.deiconify()

# Esta función llama la función eliminar archivos de la clase funciones, para eliminar el archivo txt.
def Funcion_EliminarArchivo():
    Funciones.Clear_console()
    ventana.withdraw()
    Funciones.EliminarArchivo()
    time.sleep(5)
    ventana.deiconify()

# Esta función llama la función  buscar diccionario, donde se guarda las características de los tipos de autos.
def FuncionDiccionario():
    Funciones.Clear_console()
    ventana.withdraw()
    Funciones.BuscarDiccionario()
    time.sleep(5)
    ventana.deiconify()

# Esta función llama la función tupla, para mostrar los precios de renta de los autos.
def FuncionTupla():
    Funciones.Clear_console()
    ventana.withdraw()
    Funciones.MostrarTupla()
    time.sleep(5)
    ventana.deiconify()


# Esta función llama la función salir, para salir del sistema.

def Funcion_Salir():
    sys.exit()

# En estas lineas se le configura cada una de las funciones que van a realizar los botones de la intefaz gráfica.
boton_Ingresar.config(command=Funcion_ingresar)
boton_Editar.config(command=Funcion_Editar)
boton_Mostrar.config(command=Funcion_Mostrar)
boton_Eliminar.config(command=Funcion_Eliminar)
boton_Salir.config(command=Funcion_Salir)
boton_GuardarArchivo.config(command=Funcion_GuardarArchivo)
boton_ModificarArchivo.config(command=Funcion_ModificarArchivo)
boton_EliminarArchivo.config(command=Funcion_EliminarArchivo)
botonDiccionario.config(command=FuncionDiccionario)
botontupla.config(command=FuncionTupla)



ventana.mainloop() # Iniciar el bucle principal de la ventana
