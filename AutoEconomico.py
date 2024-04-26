
from Auto import Auto # Se importa la clase auto
class Economico(Auto): # Se crea la clase economico con herencia de la clase auto.

    # Se crea el contructor de la clase, con sus atributos.
    def __init__(self, Color, Placa, Marca, RetaMasSeguro,MontoPorIVA, MostoMasIVA, TotalPorDias, ValorDeGrua, TotalMenosFondo):
        super().__init__(Color, Placa, Marca, RetaMasSeguro,MontoPorIVA, MostoMasIVA, TotalPorDias, ValorDeGrua, TotalMenosFondo)

