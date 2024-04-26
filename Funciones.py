
from AutoEconomico import Economico #SE IMPORTA LA CLASE ECONOMICO
from AutoEstandar import Estandar # SE IMPORTA LA CLASE ESTANDAR
from AutoPremium import Premium # SE IMPORTA LA CLASE PREMIUM
from Cliente import Cliente # SE IMPORTA LA CLASE CLIENTE

import os # SE IMPORTA biblioteca estándar que proporciona una interfaz para interactuar con el sistema operativo en el que se ejecuta el programa.

class Funciones(): # SE CREA LA CLASE FUNCIONES

    # TODAS LAS VAIABLES QUE SE VAN A NECESITAR PARA REALIZAR CALCULOS Y ALMACENAMIENTO DATOS.
    economico = int(25)
    estandar = int(50)
    premium = int(100)
    segEconomico = int(10)
    segEstandar = int(25)
    segPremium = int(50)
    fondo = int(100)
    iva = float(0.13)

    # CREA EL CONNTRUCTOR DE LA CLASE, CON LOS ATRIBUTOS
    def __init__(self ,economico, estandar, premium, seguroEconomico, seguroEstandar, seguroPremium, IVA, fondo):

        self.economico = economico
        self.estandar = estandar
        self.premium = premium
        self.seguroEconomico = seguroEconomico
        self.seguroEstandar = seguroEstandar
        self.seguroPremium = seguroPremium
        self.iva = IVA
        self.fondo = fondo

# SE CREA LA MATRIZ PARA ALMACENAR LOS AUTOS DEL RENTA CAR
VectorAutos = [] # Se inicializa el vector para guardar el registro de rentas de autos.
Matriz = [] # se inicializa la matriz para almacenar la disponibilidad de los autos.

###################################################################################################################################################
# SE CREA EL METODO QUE PERMITE INGRESAR LOS LOS DATOS DE CADA RENTA DE VEHICULOS
def Crear_RentaFactory():
    while True: # Bucle para que se cumplan las excepciones para ingrasar un nombre
        try: # try para que se ejecute el ingreso correctamente
            nombre = input("Ingrese el nombre del cliente: ") # Se solicita el ingreso del nombre
            if not nombre: # if para evitar que se ingrese espacio en blanco.
                raise ValueError("El nombre no puede estar vacío.") #  Mensaje exepción en caso de que se ingrese este dato en blanco.
            if not all(letra.isalpha() for letra in nombre): # if para evitar que se ingrese números
                raise ValueError("El nombre solo debe contener letras.") #  Mensaje exepción en caso de que se ingrese números.
                return nombre # Retorna el valor ingresado.
            break
        except ValueError as error: # captura el error y envia un mensaje al usuario, para ingresar un nombre valido.
            print(error)
            print("Por favor, ingrese un nombre válido (solo letras).")
    while True: # Bucle para que se cumplan las excepciones para ingrasar un apellido
        try: # try para que se ejecute el ingreso correctamente
            apellido = input("Ingrese el apellido del cliente: ") # Se solicita el ingreso el apellido
            if not apellido: # if para evitar que se ingrese espacio en blanco.
                raise ValueError("El apellido no puede estar vacío.") #  Mensaje exepción en caso de que se ingrese este dato en blanco.
            if not all(letra.isalpha() for letra in apellido): # if para evitar que se ingrese números.
                raise ValueError("El apellido solo debe contener letras.") #  Mensaje exepción en caso de que se ingrese números.
                return apellido # Retorna el valor ingresado.
            break
        except ValueError as error: # captura el error y envia un mensaje al usuario, para ingresar un nombre valido.
            print(error)
            print("Por favor, ingrese almenos un apellido válido (solo letras).")

    while True:# Bucle para que se cumplan las excepciones para ingrasar un apellido
        try: # try para que se ejecute el ingreso correctamente
            cedula = input("Ingrese el número de cédula del cliente ( 9 números): ") # Se solicita el ingreso la cédula
            if not cedula.isdigit(): # if para evitar que se ingrese letras.
                raise ValueError("La cédula solo debe contener números.") #  Mensaje exepción en caso de que se ingrese letras.
            if len(cedula) != 9: # if para que se ingrese  9 números.
                raise ValueError("La cédula debe tener 9 números.")  #  Mensaje exepción en caso de que no se ingresen 9 números.
                return cedula # Retorna el valor ingresado.
            break
        except ValueError as error:
            print(error)
            print("Por favor, ingrese el numero de Cédula válida (solo números).")

    while True: # Bucle para que se cumplan las excepciones para ingrasar un apellido
        try: # try para que se ejecute el ingreso correctamente
            credit_Card = input("Ingrese el número de tarjeta de credito del cliente (12 números): ") # Se solicita el ingreso el número de cuenta
            if not credit_Card.isdigit(): # if para evitar que se ingrese letras.
                raise ValueError("La tarjeta de credito solo debe contener números.") #  Mensaje exepción en caso de que se ingrese letras.
            if len(credit_Card) != 12: # if para que se ingrese 12 números.
                raise ValueError("La tarjeta de credito debe tener 12 números.")  #  Mensaje exepción en caso de que no se ingresen 12 números.
                return credit_Card # Retorna el valor ingresado.
            break
        except ValueError as error: # captura el error y envia un mensaje al usuario, para ingresar tarjeta de credito válida
            print(error)
            print("Por favor, ingrese el número de tarjeta de credito válida (solo números).")

    while True: # Bucle para que se cumplan las excepciones para ingrasar un apellido
        try: # try para que se ejecute el ingreso correctamente
            edad = input("Ingrese la edad del cliente: ") # Se solicita el ingreso la edad
            if not edad.isdigit(): # if para evitar que se ingrese letras.
                raise ValueError("La edad solo debe contener números.") #  Mensaje exepción en caso de que se ingrese letras.
            if len(edad) != 2: # if para que se ingrese  2 números.
                raise ValueError("La edad debe tener 2 números.") #  Mensaje exepción en caso de que no se ingresen 2 números.
                return edad # Retorna el valor ingresado.
            break
        except ValueError as error: # captura el error y envia un mensaje al usuario, para ingresar edad válida.
            print(error)
            print("Por favor, ingrese la edad del cliente (solo números).")

    while True: # Bucle para que se cumplan las excepciones para ingrasar un apellido
        try: # try para que se ejecute el ingreso correctamente
            telefono = input("Ingrese el número de teléfono del cliente (8 números): ") # Se solicita el ingreso el teléfono
            if not telefono.isdigit(): # if para evitar que se ingrese letras.
                raise ValueError("El número de teléfono solo debe contener números.") #  Mensaje exepción en caso de que se ingrese letras.
            if len(telefono) != 8: # if para que se ingrese 8 números.
                raise ValueError("El número de teléfono debe tener 8 números.") #  Mensaje exepción en caso de que no se ingresen 8 números.
                return telefono # Retorna el valor ingresado.
            break
        except ValueError as error: # captura el error y envia un mensaje al usuario, para ingresar un teléfono válida.
            print(error)
            print("Por favor, ingrese el número de teléfono del cliente (solo números).")


    while True: # Bucle para que se cumplan las excepciones para ingrasar un apellido
        try: # try para que se ejecute el ingreso correctamente
            color = input("Ingrese el color del automóvil: ") # Se solicita el ingreso el color
            if not color: # if para evitar que se ingrese espacios en blanco.
                raise ValueError("El color no puede estar vacío.") #  Mensaje exepción en caso de que se ingrese este dato en blanco.
            if not all(letra.isalpha() for letra in color): # if para evitar que se ingrese números.
                raise ValueError("El color solo debe contener letras.") # Mensaje exepción en caso de que se ingrese letras.
                return color # Retorna el valor ingresado.
            break
        except ValueError as error: # captura el error y envia un mensaje al usuario, para ingresar un color válido.
            print(error)
            print("Por favor, ingrese un color válido (solo letras).")

    while True: # Bucle para que se cumplan las excepciones para ingrasar un apellido
        try: # try para que se ejecute el ingreso correctamente
            placa = input("Ingrese la placa del automóvil (4 o más dígitos): ") # Se solicita el ingreso la placa del vehiculo
            if len(placa) < 4: # if para evitar que se ingrese un valor de menos de 4 dígitos.
                raise ValueError("El número de placa debe tener 4 o más números.") #  Mensaje exepción en caso de que se ingrese menos de 4 dígitos.
                return placa # Retorna el valor ingresado.
            break
        except ValueError as error: # captura el error y envia un mensaje al usuario, para ingresar una placa válida.
            print(error)
            print("Por favor, ingrese la placa del vehiculo.")

    while True: # Bucle para que se cumplan las excepciones para ingrasar un apellido
        try: # try para que se ejecute el ingreso correctamente
            marca = input("Ingrese la marca del automóvil: ") # Se solicita el ingreso la marca del vehiculo
            if not marca: # if para evitar que se ingrese espacios en blanco.
                raise ValueError("La marca no puede estar vacía.") #  Mensaje exepción en caso de que se ingrese este dato en blanco.
            if not all(letra.isalpha() for letra in marca): # if para evitar que se ingrese números.
                raise ValueError("La marca solo debe contener letras.") # Mensaje exepción en caso de que se ingrese letras.
                return marca # Retorna el valor ingresado.
            break
        except ValueError as error: # captura el error y envia un mensaje al usuario, para ingresar una placa válida.
            print(error)
            print("Por favor, ingrese una marca válido (solo letras).")

    categoriaOptenida=Obtener_Categoria() # Se obtiene el resultado de la función que obtiene la categoria del auto ingresado.
    retaMasSeguro = CategMasSeguro(categoriaOptenida) # Se obtiene el resultado de la función que calcula el monto más seguro de renta.
    montoPorIVA = MontoIva(retaMasSeguro) # Se obtiene el resultado de la función que calcula el IVA al monto más seguro de renta.
    mostoMasIVA = CostoTotalMasIva(retaMasSeguro) # Se obtiene el resultado de la función que suma el IVA más monto más seguro de renta.


    while True: # Bucle para que se cumplan las excepciones para ingrasar un apellido
        try: # try para que se ejecute el ingreso correctamente
            dias = input("Ingrese la cantidad de dias que desea rentar el vahiculo: ") # Se solicita el ingreso la cantidad de días de renta.
            if not dias:  #if para evitar que se ingrese espacios en blanco.
                raise ValueError("La cantidad de días no puede estar vacío.") #  Mensaje exepción en caso de que se ingrese este dato en blanco.
            if not dias.isdigit(): # if para evitar que se ingrese números.
                raise ValueError("La cantidad de días solo debe contener números.") # Mensaje exepción en caso de que se ingrese letras.
                return dias # Retorna el valor ingresado.
            break
        except ValueError as error: # captura el error y envia un mensaje al usuario, para ingresar los días de renta.
            print(error)
            print("Por favor, ingrese la cantidad de días de renta (solo números).")

    totalPorDias = Valor_Total_PorDias(int(dias), mostoMasIVA) # Se obtiene el resultado de la función del valor de renta por días de renta.
    ValorDeGrua= ServicioGrua(categoriaOptenida)
    totalMenosFondo = Deduccion_Por_fondo(totalPorDias, ValorDeGrua) # Se obtiene el resultado de la función resta del monto final a pagar menos el fondo.

    if categoriaOptenida == 1: # Categoria 1= economico, ingresa los datos del cliente y del auto al vector.
        clienteNuevo = Cliente(nombre, apellido, cedula, credit_Card, edad, telefono)
        rentaEconomica =Economico(color, placa, marca, retaMasSeguro,montoPorIVA, mostoMasIVA, totalPorDias, ValorDeGrua, totalMenosFondo)

        rentaEconomica.agregar_cliente(clienteNuevo)
        OcuparAuto()
        print("Datos ingresados correctamente")
        return VectorAutos.append(rentaEconomica)

    elif categoriaOptenida == 2: # Categoria 2= estandar, ingresa los datos del cliente y del auto al vector.
        rentaEstandar = Estandar(color, placa, marca, retaMasSeguro,montoPorIVA, mostoMasIVA, totalPorDias, ValorDeGrua, totalMenosFondo)
        clienteNuevo = Cliente(nombre, apellido, cedula, credit_Card, edad, telefono)
        rentaEstandar.agregar_cliente(clienteNuevo)
        OcuparAuto()
        print("Datos ingresados correctamente")
        return VectorAutos.append(rentaEstandar)

    elif categoriaOptenida == 3: # Categoria 3= premium, ingresa los datos del cliente y del auto al vector.
        rentaPremium = Premium(color, placa, marca, retaMasSeguro,montoPorIVA, mostoMasIVA, totalPorDias, ValorDeGrua, totalMenosFondo)
        clienteNuevo = Cliente(nombre, apellido, cedula, credit_Card, edad, telefono)
        rentaPremium.agregar_cliente(clienteNuevo)
        OcuparAuto()
        print("Datos ingresados correctamente")
        return VectorAutos.append(rentaPremium)

##################################################################################################################################################
# SE CREA LA FUNCIÓN PARA MODIFICAR LOS DATOS DE UN REGISTRO DE RENTA EN ESPECIFICO
def editarRenta():
    # sE SPLOCITA LA PALACA Y LA CEDUAL QUE PERTENECEN AL REGISTRO QUE SE DESEA MODIFICAR
    renta_Buscado = None

    while True:  # Bucle para que se cumplan las excepciones para ingrasar un apellido
        try:  # try para que se ejecute el ingreso correctamente
            cedulaBuscar = input("Ingrese la cedula del registro que desea editar (9 números): ")  # Se solicita el ingreso la cédula
            if not cedulaBuscar.isdigit():  # if para evitar que se ingrese letras.
                raise ValueError(
                    "La cédula solo debe contener números.")  # Mensaje exepción en caso de que se ingrese letras.
            if len(cedulaBuscar) != 9:  # if para que se ingrese  9 números.
                raise ValueError(
                    "La cédula debe tener 9 números.")  # Mensaje exepción en caso de que no se ingresen 9 números.
                return cedulaBuscar  # Retorna el valor ingresado.
            break
        except ValueError as error:
            print(error)
            print("Por favor, ingrese el numero de Cédula válida (solo números).")

    while True:  # Bucle para que se cumplan las excepciones para ingrasar un apellido
        try:  # try para que se ejecute el ingreso correctamente
            placaBuscar = input("Ingrese la placa del registro que desea editar (4 o más números): ")  # Se solicita el ingreso la placa del vehiculo
            if len(placaBuscar) < 4:  # if para evitar que se ingrese un valor de menos de 4 dígitos.
                raise ValueError(
                    "El número de placa debe tener 4 o más números.")  # Mensaje exepción en caso de que se ingrese menos de 4 dígitos.
                return placaBuscar  # Retorna el valor ingresado.
            break
        except ValueError as error:  # captura el error y envia un mensaje al usuario, para ingresar una placa válida.
            print(error)
            print("Por favor, ingrese la placa del vehiculo.")


    # SE RECORRE EL VECTOR DONDE SE ALMACENAN LOS REGISTROS DE LAS RENTAS
    for i in range(len(VectorAutos)):
        # CON ESTE IF SE BUSCA EN EL VECTOR EL REGISTRO QUE CONTENGA LA CEDULA Y LA PLACA ESPECIFICA
        if VectorAutos[i].cliente.cedula == cedulaBuscar and VectorAutos[i].placa == placaBuscar:
            # sE TOMA EL OBJETO ENCONTRADO Y SE MODIFICAN LOS DATOS QUE SE DESEA CAMBIAR
            renta_Buscado = VectorAutos[i]
            while True:  # Bucle para que se cumplan las excepciones para ingrasar un nombre
                try:  # try para que se ejecute el ingreso correctamente
                    nombre = input("Ingrese el nuevo nombre {}: ".format(i + 1))  # Se solicita el ingreso del nombre
                    if not nombre:  # if para evitar que se ingrese espacio en blanco.
                        raise ValueError(
                            "El nombre no puede estar vacío.")  # Mensaje exepción en caso de que se ingrese este dato en blanco.
                    if not all(letra.isalpha() for letra in nombre):  # if para evitar que se ingrese números
                        raise ValueError(
                            "El nombre solo debe contener letras.")  # Mensaje exepción en caso de que se ingrese números.
                        return nombre  # Retorna el valor ingresado.
                    break
                except ValueError as error:  # captura el error y envia un mensaje al usuario, para ingresar un nombre valido.
                    print(error)
                    print("Por favor, ingrese un nombre válido (solo letras).")

            while True:  # Bucle para que se cumplan las excepciones para ingrasar un apellido
                try:  # try para que se ejecute el ingreso correctamente
                    apellido = input("Ingrese el nuevo apellido del cliente {}: ".format(i + 1))  # Se solicita el ingreso el apellido
                    if not apellido:  # if para evitar que se ingrese espacio en blanco.
                        raise ValueError(
                            "El apellido no puede estar vacío.")  # Mensaje exepción en caso de que se ingrese este dato en blanco.
                    if not all(letra.isalpha() for letra in apellido):  # if para evitar que se ingrese números.
                        raise ValueError(
                            "El apellido solo debe contener letras.")  # Mensaje exepción en caso de que se ingrese números.
                        return apellido  # Retorna el valor ingresado.
                    break
                except ValueError as error:  # captura el error y envia un mensaje al usuario, para ingresar un nombre valido.
                    print(error)
                    print("Por favor, ingrese almenos un apellido válido (solo letras).")

            while True:  # Bucle para que se cumplan las excepciones para ingrasar un apellido
                try:  # try para que se ejecute el ingreso correctamente
                    cedula = input("Ingrese el  nuevo número de cédula del cliente (9 números) {}: ".format(i + 1))  # Se solicita el ingreso la cédula
                    if not cedula.isdigit():  # if para evitar que se ingrese letras.
                        raise ValueError(
                            "La cédula solo debe contener números.")  # Mensaje exepción en caso de que se ingrese letras.
                    if len(cedula) != 9:  # if para que se ingrese  9 números.
                        raise ValueError(
                            "La cédula debe tener 9 números.")  # Mensaje exepción en caso de que no se ingresen 9 números.
                        return cedula  # Retorna el valor ingresado.
                    break
                except ValueError as error:
                    print(error)
                    print("Por favor, ingrese el numero de Cédula válida (solo números).")

            while True:  # Bucle para que se cumplan las excepciones para ingrasar un apellido
                try:  # try para que se ejecute el ingreso correctamente
                    edad = input("Ingrese la nueva edad del cliente (2 números) {}: ".format(i + 1))  # Se solicita el ingreso la edad
                    if not edad.isdigit():  # if para evitar que se ingrese letras.
                        raise ValueError(
                            "La edad solo debe contener números.")  # Mensaje exepción en caso de que se ingrese letras.
                    if len(edad) != 2:  # if para que se ingrese  2 números.
                        raise ValueError(
                            "La edad debe tener 2 números.")  # Mensaje exepción en caso de que no se ingresen 2 números.
                        return edad  # Retorna el valor ingresado.
                    break
                except ValueError as error:  # captura el error y envia un mensaje al usuario, para ingresar edad válida.
                    print(error)
                    print("Por favor, ingrese la edad del cliente (solo números).")

            while True:  # Bucle para que se cumplan las excepciones para ingrasar un apellido
                try:  # try para que se ejecute el ingreso correctamente
                    telefono = input("Ingrese el nuevo numero de teléfono del cliente (8 números) {}: ".format(i + 1))  # Se solicita el ingreso el teléfono
                    if not telefono.isdigit():  # if para evitar que se ingrese letras.
                        raise ValueError(
                            "El número de teléfono solo debe contener números.")  # Mensaje exepción en caso de que se ingrese letras.
                    if len(telefono) != 8:  # if para que se ingrese 8 números.
                        raise ValueError(
                            "El número de teléfono debe tener 8 números.")  # Mensaje exepción en caso de que no se ingresen 8 números.
                        return telefono  # Retorna el valor ingresado.
                    break
                except ValueError as error:  # captura el error y envia un mensaje al usuario, para ingresar un teléfono válida.
                    print(error)
                    print("Por favor, ingrese el número de teléfono del cliente (solo números).")

            while True:  # Bucle para que se cumplan las excepciones para ingrasar un apellido
                try:  # try para que se ejecute el ingreso correctamente
                    credit_card = input("Ingrese el nuevo número de cuenta del cliente (12 números){}: ".format(i + 1))  # Se solicita el ingreso el número de cuenta
                    if not credit_card.isdigit():  # if para evitar que se ingrese letras.
                        raise ValueError(
                            "La tarjeta de credito solo debe contener números.")  # Mensaje exepción en caso de que se ingrese letras.
                    if len(credit_card) != 12:  # if para que se ingrese 12 números.
                        raise ValueError(
                            "La tarjeta de credito debe tener 12 números.")  # Mensaje exepción en caso de que no se ingresen 12 números.
                        return credit_card  # Retorna el valor ingresado.
                    break
                except ValueError as error:  # captura el error y envia un mensaje al usuario, para ingresar tarjeta de credito válida
                    print(error)
                    print("Por favor, ingrese el número de tarjeta de credito válida (solo números).")

            while True:  # Bucle para que se cumplan las excepciones para ingrasar un apellido
                try:  # try para que se ejecute el ingreso correctamente
                    color = input("Ingrese el nuevo color del automóvil {}: ".format(i + 1))  # Se solicita el ingreso el color
                    if not color:  # if para evitar que se ingrese espacios en blanco.
                        raise ValueError(
                            "El color no puede estar vacío.")  # Mensaje exepción en caso de que se ingrese este dato en blanco.
                    if not all(letra.isalpha() for letra in color):  # if para evitar que se ingrese números.
                        raise ValueError(
                            "El color solo debe contener letras.")  # Mensaje exepción en caso de que se ingrese letras.
                        return color  # Retorna el valor ingresado.
                    break
                except ValueError as error:  # captura el error y envia un mensaje al usuario, para ingresar un color válido.
                    print(error)
                    print("Por favor, ingrese un color válido (solo letras).")

            while True:  # Bucle para que se cumplan las excepciones para ingrasar un apellido
                try:  # try para que se ejecute el ingreso correctamente
                    placa = input("Ingrese la nuevo placa del automóvil (4 o más dígitos){}: ".format(i + 1)) # Se solicita el ingreso la placa del vehiculo
                    if len(placa) < 4:  # if para evitar que se ingrese un valor de menos de 4 dígitos.
                        raise ValueError(
                            "El número de placa debe tener 4 o más números.")  # Mensaje exepción en caso de que se ingrese menos de 4 dígitos.
                        return placa  # Retorna el valor ingresado.
                    break
                except ValueError as error:  # captura el error y envia un mensaje al usuario, para ingresar una placa válida.
                    print(error)
                    print("Por favor, ingrese la placa del vehiculo.")

            while True:  # Bucle para que se cumplan las excepciones para ingrasar un apellido
                try:  # try para que se ejecute el ingreso correctamente
                    marca = input("Ingrese la nuevo marca del automóvil {}: ".format(i + 1)) # Se solicita el ingreso la marca del vehiculo
                    if not marca:  # if para evitar que se ingrese espacios en blanco.
                        raise ValueError(
                            "La marca no puede estar vacía.")  # Mensaje exepción en caso de que se ingrese este dato en blanco.
                    if not all(letra.isalpha() for letra in marca):  # if para evitar que se ingrese números.
                        raise ValueError(
                            "La marca solo debe contener letras.")  # Mensaje exepción en caso de que se ingrese letras.
                        return marca  # Retorna el valor ingresado.
                    break
                except ValueError as error:  # captura el error y envia un mensaje al usuario, para ingresar una placa válida.
                    print(error)
                    print("Por favor, ingrese una marca válido (solo letras).")



            # SE AGREGAN LOS NUEVOS DATOS
            VectorAutos[i].cliente.nombre = nombre
            VectorAutos[i].cliente.apellido = apellido
            VectorAutos[i].cliente.edad = edad
            VectorAutos[i].cliente.telefono = telefono
            VectorAutos[i].cliente.credit_card = credit_card
            VectorAutos[i].cliente.cedula = cedula
            VectorAutos[i].color = color
            VectorAutos[i].placa = placa
            VectorAutos[i].marca = marca

            break
    # sI SE ENCUENTRA EL REGISTRO SE MANDA EL PRIMER MENSAJE, SINO SE PRESENTA EL SEGUNDO MENSAJE
    if renta_Buscado:
        print(f"Edición exitosa: ")
    else:
        print("Auto no encontrado")

##################################################################################################################################################
# FUNCIÓN PARA ELIMINAR EL REGISTRO DE AULGUNA RENTA
def EliminarRenta():
    rentaBuscado = None
    # SE PIDE EL NUMERO DE CEDULA QUE CORRESPONDE AL CLIENTE DEL REGISTRO A ELIMINAR

    while True:  # Bucle para que se cumplan las excepciones para ingrasar un apellido
        try:  # try para que se ejecute el ingreso correctamente
            cedulabuscar = input("Ingrese la cedula del segistro que desea eliminar (9 números): ")  # Se solicita el ingreso la cédula
            if not cedulabuscar.isdigit():  # if para evitar que se ingrese letras.
                raise ValueError(
                    "La cédula solo debe contener números.")  # Mensaje exepción en caso de que se ingrese letras.
            if len(cedulabuscar) != 9:  # if para que se ingrese  9 números.
                raise ValueError(
                    "La cédula debe tener 9 números.")  # Mensaje exepción en caso de que no se ingresen 9 números.
                return cedulabuscar  # Retorna el valor ingresado.
            break
        except ValueError as error:
            print(error)
            print("Por favor, ingrese el numero de Cédula válida (solo números).")

    # CON ESTE FOR SE RECORRE EL VECTOR
    for i in range(len(VectorAutos)):
        # SI LA POSICION DEL VECTOR COINSIDE CON LA CEDULA A BUSCAR SE ELIMINA
        if VectorAutos[i].cliente.cedula == cedulabuscar:
            rentaBuscado = VectorAutos[i]
            del VectorAutos[i]

            break # detiene el bucle de for

    if rentaBuscado: # en caso de ser encontrado el registro se muestra el primer mensaje, de lo contrario el segundo.
        print(f"Renta se encontro  y se elimino :")
    else:
        print("Renta no encontrado")

###################################################################################################################################################
# SE GENERA LA MATRIZ CON LOS AUTOS DISPONIBLES
def CrearDisponibilidadAutos():
    print("Generación de la matriz de almancen de autos")
    filas = 4
    columnas = 5
    for i in range(filas):
        Matriz.append([])
        for j in range(columnas):
            Matriz[i].append("Auto Disponible")
    # SE IMPRIMEN TODAS LA FILAS DE LA MATRIZ
    for filas in Matriz:
        print(filas)
##################################################################################################################################################
# con esta función se cambia el estado disponible de los autos a no disponible, cada vez que son rentados.
def OcuparAuto():
    datoDeComprobacion=0
    filas = 4
    columnas = 5

    for i in range(filas):
        for j in range(columnas):
            if Matriz[i][j] == 'Auto Disponible' and datoDeComprobacion == 0 :
                Matriz[i][j] = "Auto no disponible"
                datoDeComprobacion=1
                break

    for filas in Matriz:
        print(filas)



##################################################################################################################################################
# SE CREA LA FUNCIÓN PARA MOSTRAR TODOS LOS REGISTROS DE RENTAS CREADOS
def To_string():

    if len(VectorAutos) == 0:
        print(" No existen risgitros de renta")
    else:
         # SE MUESTRAN TODOS LOS REGISTROS QUE HAYAN EN EL VECTOR CON SUS DATOS CORRESPONDIENTES
        for auto in VectorAutos: # se recorre el vector de autos y se muestran los datos de los registros.
            print("-----------DATOS DEL CLIENTE----------------")
            print("Nombre del cliente:", auto.cliente.nombre)
            print("Apellidos del cliente:", auto.cliente.apellido)
            print("Edad:", auto.cliente.edad)
            print("Teléfono:", auto.cliente.telefono)
            print("Numero de cuenta:", auto.cliente.credit_card)
            print("Cédula:", auto.cliente.cedula)
            print("<<<<<<<Datos Del Auto>>>>>>>")
            print("Color:", auto.color)
            print("Placa:", auto.placa)
            print("Marca:", auto.marca)

            print(">>>>>>>>>>>>>>>DATOS DE LA RENTA<<<<<<<<<<<<<<<")
            print("Monto de renta mas seguro: ", auto.rentaMasSeguro)
            print("Monto del impuesto de IVA: ", auto.montoPorIVA)
            print("Monto total de la renta más el IVA: ", auto.montoMasIVA)
            print("Monto total de todos los dias de alquiler: ", auto.totalPorDias)
            print("Monto por servicio de grua: ", auto.valorDeGrua)
            print("Monto total a pagar menos fondo por daños: ", auto.totalMonosFondo)


###################################################################################################################################################
"""
CON ESTA FUNCIÓN EL USUARIO ELIGE LA CATEGORIA DE AUTO QUE DESEA ALQUILAR, LA EXCEPCION EEVITA QUE SE ESCOJA UNA OPCIÓN 
FURA DEL RANGO DE 1 A 3.
"""
def Obtener_Categoria():
    while True:
        try:
            categoria = int(input("Ingrese la categoría del vehículo (1. Si Economico, 2. Si estandar o 3. Premium): "))
            if 1 <= categoria <= 3:
                    return categoria
            else:
                    print("Error: El número debe estar entre 1 y 3.")
        except ValueError:
                print("Error: Debe ingresar un número válido.")


##################################################################################################################################################
"""
CON ESTA FUCIÓN SE CABTURA LA CATEGORIA DE AUTO POR PARAMETRO Y SEGUN SU CATEGORIA SE REALIZA EL CALCULO DEL MONTO MÁS EL SEGURO
"""
def CategMasSeguro (categoria):

            if 1 <= categoria <= 3:
                if categoria == 1:
                    rentaMasSeguro = Funciones.economico + Funciones.segEconomico
                elif categoria == 2:
                    rentaMasSeguro = Funciones.estandar + Funciones.segEstandar
                elif categoria == 3:
                    rentaMasSeguro = Funciones.premium + Funciones.segPremium

                return rentaMasSeguro
################################################################################################################################################
"""
CON ESTA FUNCIÓN SE CALCULA EL MONTO DE IVA QUE CORRESPONDE AL MONTO DE CATEGORIA MAS EL SEGURO
"""
def MontoIva (totalrentemasseguro):

    totalMontoIva = totalrentemasseguro * Funciones.iva
    # RETORNA EL MONTO DE IVA
    return totalMontoIva
#################################################################################################################################################
"""
con esta funcion se suman el monto por seguro y categoria del auto más el impuesto de IVA
"""
def CostoTotalMasIva (totalrentemasseguro):

    resultadoTotalMasIVA= totalrentemasseguro + MontoIva(totalrentemasseguro)
    return resultadoTotalMasIVA

###################################################################################################################################################
"""
CON ESTA FUNCIÓN SE OBTIENE LOS DIAS QUE EL CLIENTE VA ALQUILAR EL AUTO Y SE MULTIPLICA POR EL MONTO TOTAL DE SEGURO,
CATEGORIA Y EL IMPUESTO DE IVA, RETORNA EL RESULTADO
"""
def Valor_Total_PorDias (Dias, TotalMasIva):
    totalPorDias = Dias * TotalMasIva

    return totalPorDias

##################################################################################################################################################
#Se implementa l patron de diseño adapter
def ServicioGrua(categoria): # Se toma la categoriadel auto por parametro

    if categoria == 2: # si la categoria es 2= Estandar, llama el metodo servicio de grúa de categoria estandar
        montoGrua=Estandar.ServicioGrua(categoria) # Se toma el valor que retorna el metodo de Estandar
    elif categoria == 3: # si la categoria es 3= Estandar, llama el metodo servicio de grúa de categoria Premium
        montoGrua= Premium.ServicioGrua(categoria) # Se toma el valor que retorna el metodo de Premium

    else: # En caso de que el parámetro de categoria tenga el valor 1=Economico
        montoGrua=0

    return montoGrua #Retorna el valor del la función estandar o Premium.
###################################################################################################################################################
"""
CON ESTA FUNCIÓN SE CALCULA OBTIENE POR PARAMETRO EL MONTO TOTAL DEL ALQUILER Y SE DEDUSE EL MONTO DE FONDO POR
RIESGOS QUE ES DE 100 DOLARES Y SE RETORNA EL RESULTADO.
"""
def Deduccion_Por_fondo (totalPorDias, montoGrua):
    totalMenosFondo= (totalPorDias + montoGrua) - Funciones.fondo

    return totalMenosFondo
##################################################################################################################################################
"""
CON ESTA FUNCIÓN SE SACA EL PROMEDIO DE VENTA OBTENIDO DE TODOS LOS REGISTROS INGRESADOS
"""
def PromedioVenta():
    totalClientes =float(0)

    # SE RECORRE EL VECTOR
    for i in range(len(VectorAutos)): # Se recorre el vector
        #
        totalClientes = totalClientes + VectorAutos[i].TotalMenosFondo # Se suman los totales de cada una de las rentas y se pasan a la variable.

    numeroRentas = len(VectorAutos) # Se cuenta la cantidad de rentas del vector
    promedioRentasporJornada = totalClientes / numeroRentas # Se toma la cantidad de los montos de renta y se divide entre la cantidad de rentas.

    print("Promedio de rentas:", promedioRentasporJornada)# Se imprime el resultado del promedio de ventas.


###################################################################################################################################################
"""
En esta función se crea un archivo txt y se guradan todas las rentas realizadas.
"""
def GuardarArchivo():
    with open("miArchivo.txt", "w") as archivo: # se abre el archivo txt.
        for i in range(len(VectorAutos)): # Se recorre la longitud del vector y se van escribiendo en el archivo txt.

            archivo.write(f"Nombre: {VectorAutos[i].cliente.nombre}\n")
            archivo.write(f"Apellido: {VectorAutos[i].cliente.apellido}\n")
            archivo.write(f"Edad: {VectorAutos[i].cliente.edad}\n")
            archivo.write(f"Telefono: {VectorAutos[i].cliente.telefono}\n")
            archivo.write(f"Credit_card: {VectorAutos[i].cliente.credit_card}\n")
            archivo.write(f"Cedula: {VectorAutos[i].cliente.cedula}\n")
            archivo.write(f"color: {VectorAutos[i].color}\n")
            archivo.write(f"placa: {VectorAutos[i].placa}\n")
            archivo.write(f"marca: {VectorAutos[i].marca}\n")
            archivo.write(f"RentaMasSeguro: {VectorAutos[i].rentaMasSeguro}\n")
            archivo.write(f"TotalMontoIva: {VectorAutos[i].montoPorIVA}\n")
            archivo.write(f"ResultadoTotalMasIVA: {VectorAutos[i].montoMasIVA}\n")
            archivo.write(f"totalPorDias: {VectorAutos[i].totalPorDias}\n")
            archivo.write(f"TotalMenosFondo: {VectorAutos[i].totalMonosFondo}\n")
            archivo.write("\n")

    print("Datos guardados exitosamente!") # Se imprime un mensaje de confirmación de ingreso de datos al archivo txt.
    archivo.close() # Se cierra el archivo.
#################################################################################################################################################
"""
 En esta función se edita el archivo txt craedo anteriormente.
"""
def EditarArchivo():
    with open("miArchivo.txt", "r+") as archivo: # Se abre el archivo txt
        contenido = archivo.read() # Se lee el contenido del archivo.
        print(f"Contenido actual:\n{contenido}") # Se muestra el contenido del archivo.
    archivo.close()

    with open("miArchivo.txt", "r+") as archivo: # Se abre el archivo txt
        contenido = archivo.read() # Se lee el contenido del archivo.
        archivo.seek(0, 2)  # Mover al final del archivo
        for i in range(len(VectorAutos)): # se recorre el vector y se escriben los datos del vector en le archivo.
            # SI LA POSICION DEL VECTOR COINSIDE CON LA CEDULA A BUSCAR SE ELIMINA
            archivo.write(f"Nombre: {VectorAutos[i].cliente.nombre}\n")
            archivo.write(f"Apellido: {VectorAutos[i].cliente.apellido}\n")
            archivo.write(f"Edad: {VectorAutos[i].cliente.edad}\n")
            archivo.write(f"Telefono: {VectorAutos[i].cliente.telefono}\n")
            archivo.write(f"Credit_card: {VectorAutos[i].cliente.credit_card}\n")
            archivo.write(f"Cedula: {VectorAutos[i].cliente.cedula}\n")
            archivo.write(f"color: {VectorAutos[i].color}\n")
            archivo.write(f"placa: {VectorAutos[i].placa}\n")
            archivo.write(f"marca: {VectorAutos[i].marca}\n")
            archivo.write(f"RentaMasSeguro: {VectorAutos[i].rentaMasSeguro}\n")
            archivo.write(f"TotalMontoIva: {VectorAutos[i].montoPorIVA}\n")
            archivo.write(f"ResultadoTotalMasIVA: {VectorAutos[i].montoMasIVA}\n")
            archivo.write(f"totalPorDias: {VectorAutos[i].totalPorDias}\n")
            archivo.write(f"TotalMenosFondo: {VectorAutos[i].totalMonosFondo}\n")
            archivo.write("\n")

        print("Archivo modificado y guarado con exito")
        archivo.close() # Se cierra el archivo.
###################################################################################################################################################
"""
Con esta función se elimina el archivo txt por completo.
"""
def EliminarArchivo ():

    with open("miArchivo.txt", 'w') as archivo:
        archivo.write("")
        print("Datos del archivo eliminados correctamente.")

    archivo.close()

##################################################################################################################################################
"""
Con esta función se crea un diccionario donde se guardan las descripciones de cada una de las categorias de renta de autos.
"""

def BuscarDiccionario():
     # Se crea el diccionario.
    diccionario = {"Auto Economico":"Es un vehiculo pequeño, con poco espacio, de menor valor de renta",
                   "Auto Estandar": "Vehiculo mediano, un poco más comodo, de costo medio, no tan lujoso",
                   "Auto Premium":"Auto muy lujo, con espacio para varios pasajeros (familiar), tracción 4X4"}
    # Se solicita la clave al usuario
    clave= input("Ingrese la clase de vehiculo a consultar (Auto Economico , Auto Estandar o Auto Premium):  ")
     # Se imprimen los datos a los que hace referencia la clave en el diccionario.
    print(diccionario[clave])
##################################################################################################################################################

"""
Con esta función se crea una tupla, donde se almacenan los precios de renta de cada una de las categorias de renta.
"""
def MostrarTupla():
     # Se crea la  tupla con sus datos.
    tuplaPrecios= ("152.55","197.75","282.5")
    # Se accede a la posicion especifica de la tupla y se le pasa el valo a cada una de las categorias.
    autoEconomico = tuplaPrecios[0]
    autoEstandar = tuplaPrecios[1]
    autoPremium = tuplaPrecios[2]
    # Se imprime los valores correspondientes obtenidos de la tupla.
    print(f"Precios de renta por día")
    print(f"Auto Economico: ${autoEconomico}")
    print(f"Auto Estandar: ${autoEstandar}")
    print(f"Auto Premiun: ${autoPremium}")

##################################################################################################################################################
"""
Esta función permite al sistema eliminar todo lo que alla en consola, para asi liberar memoria.
"""
def Clear_console():
    """limpiar consola """
    if os.name == 'nt':  # para windows
        os.system('cls')
    else:               # para linux y mac
        os.system('clear')