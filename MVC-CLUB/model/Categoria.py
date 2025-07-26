class Categoria:
    def __init__(self,cod,denominacion):
        self.codigo = cod
        self.denominacion = denominacion

    def getCantidadJugadores(self,lista):
        return len(self.getListaJugadores(lista))

    def getListaJugadores(self,lista):
        listaJugadoresCategoria = []
        for i in lista:
            if i.categoria.codigo == self.codigo:
                listaJugadoresCategoria.append(i)
        return listaJugadoresCategoria
    
    def __str__(self):
        return (f"{self.denominacion} cod-{self.codigo}")

    def __repr__(self):
        return self.__str__()