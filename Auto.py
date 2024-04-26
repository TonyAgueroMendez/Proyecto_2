


class Auto(): # Se crea la clase auto

    # Se inicializa el contructor de la clase, con sus atributos correspondientes.
    def __init__(self, Color, Placa, Marca, RetaMasSeguro,MontoPorIVA, MostoMasIVA, TotalPorDias, ValorDeGrua, TotalMenosFondo):
        self. color= Color
        self. placa= Placa
        self. marca= Marca
        self. rentaMasSeguro= RetaMasSeguro
        self. montoPorIVA= MontoPorIVA
        self. montoMasIVA= MostoMasIVA
        self. totalPorDias= TotalPorDias
        self. valorDeGrua= ValorDeGrua
        self. totalMonosFondo= TotalMenosFondo
        self. cliente = None
    # Se hace la agregación de la clase cliente a autos.
    def agregar_cliente(self, cliente):
        self.cliente = cliente





