class Jugador:
    def __init__(self,dni,apellido,nombre,club,categoria,goles,anotaciones,expulsiones):
        self.dni = dni
        self.apellido = apellido
        self.nombre = nombre
        self.club = club
        self.categoria = categoria
        self.goles = goles
        self.anotaciones = anotaciones
        self.expulsiones = expulsiones

    def getPuntosDesem(self):
        desempenio = int(self.goles)*10 - int(self.anotaciones)*2 -int(self.expulsiones)*5
        return f"El jugador {self.apellido} tiene un desempenio de {desempenio}"

    def getMostrarInformacion(self):
        return f"DNI={self.dni} |-Nombre: {self.apellido} {self.nombre} |- Club : {self.club.__str__()} |- Categoria: {self.categoria.__str__()} |-goles {self.goles}|- Amolestaciones {self.anotaciones} |- Expulsiones {self.expulsiones}\n"

    def __str__(self):
     return f"{self.apellido}, {self.nombre}"

    def __repr__(self):
        return self.__str__()
