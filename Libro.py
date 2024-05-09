from Transacciones import Transaccion
class Libro:

    def __init__self(self, titulo, isbn, cantidadActual, precioCompra, precioVenta, rutaImagen):
        self.__titulo=titulo
        self.__isbn=isbn
        self.__cantidadActual=cantidadActual
        self.__precioCompra=precioCompra
        self.__precioVneta=precioVenta
        self.__rutaImagen=rutaImagen
        self.__transacciones=[]
    def getTitulo(self):
        return self.__titulo
    
    def setTitulo(self, nTitulo):
        self.__titulo=nTitulo

    def getIsbn(self):
        return self.__isbn
    
    def setIsbn(self, nIsbn):
        self.__isbn=nIsbn
    
    def getPreciodeCompra(self):
        return self.__precioCompra
    
    def setPreciodeCompra(self, nPrecioCompra):
        self.__precioCompra=nPrecioCompra

    def getPreciodeVenta(self):
        return self.__precioVenta
    
    def setPreciodeVenta(self, nPrecioVenta):
        self.__precioVenta=nPrecioVenta
    
    def getCantidadActual(self):
        return self.__cantidadActual
    
    def setCantidadActual(self, nCantidadActual):
        self.__cantidadActual=nCantidadActual

    def vender(self, cantidad, fecha):

        vendido=False
        if cantidad <=self.getCantidadActual:
            self.setCantidadActual(self.getCantidadActual()-cantidad)
            nueva=Transaccion(1, cantidad, fecha)
            self.__transacciones.append(nueva)
            vendido=True
    def abastecer(self, cantidad, fecha):
         
        self.setCantidadActual(self.getCantidadActual()+cantidad)
        nueva=Transaccion(2, cantidad, fecha)
        self.__transacciones.append(nueva)