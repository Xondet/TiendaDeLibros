class Trajsaccion:
    TIPO= {
        1:'VENTA',
        2:'ABASTECIMIENTO'
    }

    def __init__(self, tipo, fecha, cantidad):
        self.__tipo=self.TIPO['1'] if tipo==1 else self.TIPO['2']
        self.__cantidad=cantidad
        self.__fecha=fecha
    def getTipo(self):
        return self.__tipo
    def setTipo(self, tipo):
        self.__tipo=self.TIPO['1'] if tipo==1 else self.TIPO['2']
    def getCantidad(self):
        return self.__cantidad
    def setCantidad(self, cantidad):
        self.__cantidad=cantidad
    def getFecha(self):
        return self.__fecha
    def setFecha(self, fecha):
        self.__fecha=fecha

    