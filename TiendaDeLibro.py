from Libro import Libro 

class TiendaLibros:

    def __init__(self):
        self.__caja=0
        self.__catalogo=[]
    
    def getCatalogo(self):
        return self.__catalogo
    
    def getCaja(self):
        return self.__caja
    
    def setCaja(self):
            Caja=self.__caja
    def BuscarLibroPorTitulo(self, titulo):
        libroBuscado=None

        for libro in self.__catalogo:
            if libro.getTitulo()==titulo:
                libroBuscado=libro
                break
        return libroBuscado
    def BuscarLibroPorISBN(self, isbn):
    
        isbn==None
        for libro in self.__catalogo:
            if libro.getISBN()==isbn:
                isbn=libro
                break
        return isbn
    def registrarLibro(self, titulo, isbn, cantidadActual, precioCompra, precioVenta, rutaImagen):
        
        buscar=self.BuscarLibroPorISBN(isbn)
        nuevo=None
        if buscar==None:
            nuevo=Libro(titulo, isbn, cantidadActual, precioCompra, precioVenta, rutaImagen)
            self.__catalogo.append(nuevo)
        return nuevo
    def eliminarLibro(self, isbn):
        buscar=self.BuscarLibroPorISBN(isbn)
        eliminado=False
        if buscar:
            if buscar.getCantidadActual()==0:
                self.__catalogo.remove(buscar)
                eliminado=True
        return eliminado
    def darlibroMasEconomico(self):
        libroMasEconomico=[0]
        for libro in self.__catalogo:
            if libroMasEconomico.getPrecioVenta()>libro.getPrecioVenta():
                libroMasEconomico=libro
        return libroMasEconomico
    #forma profe
    #def darLibroMasEconomico(self):
    #    menosCostoso=None
    #    if (len(self.__catalogo)>0):
    #        menosCostoso=self.__catalogo[0]
    #        for libro in self.__catalogo:
    #            if (libro.getPrecioVenta()<menosCostoso.getPrecioVenta()):
    #                menosCostoso=libro
    #    return menosCostoso
    def darlibroMasCaro(self):
        libroMasCaro=[0]
        for libro in self.__catalogo:
            if libroMasCaro.getPrecioVenta()<libro.getPrecioVenta():
                libroMasCaro=libro
        return libroMasCaro
    def Vender(self, fecha, cantidad, isbn, titulo=None):
        vendido=False
        buscado=self.BuscarLibroPorISBN(isbn)
        
        
        if titulo is not None and buscado is None:
            buscado=self.BuscarLibroPorTitulo(titulo)

        if buscado:
            vendido=buscado.vender(cantidad, fecha)
            self.setCaja(self.getCaja+(cantidad*buscado.getPrecioVenta()))
        return vendido
    def Abastecer(self, fecha, cantidad, isbn, titulo=None):
        