
from Auto import Auto # Se importa la clase auto
class Estandar(Auto): # Se crea la clase estandar con herencia de la clase auto.

    # Se crea el contructor de la clase, con sus atributos.
    def __init__(self, Color, Placa, Marca, RetaMasSeguro,MontoPorIVA, MostoMasIVA, TotalPorDias, ValorDeGrua, TotalMenosFondo):
        super().__init__(Color, Placa, Marca, RetaMasSeguro,MontoPorIVA, MostoMasIVA, TotalPorDias, ValorDeGrua, TotalMenosFondo)


    def ServicioGrua(self):
        valorServicio= int(100)
        return valorServicio