class VistaCategoria:
    def mostrarLista(self,lista):
        for club in lista:
            print(club)

    def mostarInfo(self,info):
        print(f"\nHay {info} jugadores en esta categoria")
    
    def listarJugadoresCategoria(self,lista):
        for i in lista:
            print(i.getMostrarInformacion())