from model.Club import Club
from view.VistaClub import VistaClub
class ControllerClub:
    def __init__(self):
        self.vista=VistaClub()
        self.listaClub =[]

    def cargarClub(self):
        with open("20/clubes.txt") as f:
            renglones = f.readlines()
            for renglon in renglones:
                datos = renglon.strip().split(",")
                self.listaClub.append(Club(*datos))

    def mostrarListaClub(self):
        self.vista.mostrarLista(self.listaClub)

    def buscarObj(self,cod):
        for obj in self.listaClub:
            if obj.codigo == cod:
                return obj

    def listarJugadoresClub(self,objeto,lista):
        listaJug = objeto.getListaJugadores(lista)
        self.vista.mostrarLista(listaJug)
