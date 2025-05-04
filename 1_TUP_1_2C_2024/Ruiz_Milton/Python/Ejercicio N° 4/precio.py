
class Precio():
    __precio_hora = 5000
    def __init__(self) -> None:
        pass
    
    @classmethod
    def calcular_importe(cls, cant_horas: int) -> float:
        precio_final = cant_horas * cls.__precio_hora
        return precio_final
