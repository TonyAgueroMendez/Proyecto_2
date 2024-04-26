
class Cliente (): # Se crea la clase cliente.
    # iNICIALIZA UNA ENTANCIA VACIA PARA EL METODO DE SINGLETON
    _instance = None
    # Se crea el contructor de la clase con sus atributos.
    def __init__(self, Nombre, Apellido, Cedula, credit_Card, Edad, Telefono):
        self. nombre = Nombre
        self. apellido= Apellido
        self. cedula= Cedula
        self. credit_card= credit_Card
        self. edad= Edad
        self. telefono= Telefono

        # DEFINICIÓN DE LA FUNCIÓN DE SINGLETON EN LA CLASE PERSONA PARA NO PERMITIR CREAR MÁS DE UNA ISNTANCIA DE ESTA CLASE.
        def __new__(cls, *args, **kwargs):
            if not isinstance(cls._instance, cls):
                cls._instance = object.__new__(cls)
            return cls._instance

