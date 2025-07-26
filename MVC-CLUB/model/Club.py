class Club:
    def __init__(self,cod,denominacion):
        self.codigo = cod
        self.denominacion = denominacion


    def getListaJugadores(self,lista):
        listaJugadoresClub = []
        for i in lista:
            if i.club.codigo == self.codigo:
                listaJugadoresClub.append(i)
        return listaJugadoresClub
    
    
    def __str__(self):
        return f"{self.denominacion} ID= {self.codigo}"

    def __repr__(self):
        return self.__str__()
