class VistaJugador:
    def mostrarLista(self,lista):
        for club in lista:
            print(club)

    def listarDetallado(self,lista):
        for i in lista:
            print(i.getMostrarInformacion())

    def mostrar(self,dato):
        print(dato)

    def ingresarDatos(self,dato):
        return input(f"infrese el {dato} del jugador: ")