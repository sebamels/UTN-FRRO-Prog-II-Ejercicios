from datetime import *

class Estadia():
    def __init__(self, nro_patente: str, hora_entrada: str, hora_salida = None, cant_horas = None, estado = None, pagado = None) -> None:
        self.__fecha = datetime.now().date()
        self.__nro_patente = nro_patente
        self.__hora_entrada = hora_entrada
        self.__hora_salida = None
        self.__cant_horas = None
        self.__estado = "Activo"
        self.__pagado = False

    @property
    def fecha(self):
        return self.__fecha

    @property
    def nro_patente(self):
        return self.__nro_patente

    @property
    def hora_entrada(self):
        return self.__hora_entrada

    @property
    def hora_salida(self):
        return self.__hora_salida

    @property
    def cant_hora(self):

        formato = "%H:%M"

        try:
            hora_entrada = datetime.strptime(self.hora_entrada, formato)
            hora_salida = datetime.strptime(self.hora_salida, formato)

            diferencia = hora_salida - hora_entrada
            horas_totales = diferencia.total_seconds() / 3600  # 3600 segundos en una hora
            return horas_totales
        except ValueError:
            return "Formato de hora incorrecto. Debe ser 'HH:MM'."

    @property
    def estado(self):
        return self.__estado

    @property
    def pagado(self):
        return self.__pagado


    def __str__(self) -> str:
        return (f"Patente => {self.nro_patente}\n"
                f" Fecha de entrada => {self.fecha}\n"
                f" Hora de entrada => {self.hora_entrada}\n")

    def registrar_salida(self, hora_salida):
        self.__hora_salida = hora_salida
        self.__estado = "Pagado"
        self.__pagado = True