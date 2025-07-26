from model.Categoria import Categoria
from view.VistaCategoria import VistaCategoria



class ControllerCategoria:
    def __init__(self):
        self.vista=VistaCategoria()
        self.listaCategorias =[]

    def cargarCategoria(self):
        with open("20/categorias.txt") as f:
            renglones = f.readlines()
            for renglon in renglones:
                datos = renglon.strip().split(",")
                self.listaCategorias.append(Categoria(*datos))

    def mostrarListaCategoria(self):
        self.vista.mostrarLista(self.listaCategorias)

    def buscarObj(self, cod):
        for obj in self.listaCategorias:
            if obj.codigo == cod:
                return obj

    def CantidadJugadoresXCategoria(self,categoria,lista):
        self.vista.mostarInfo(categoria.getCantidadJugadores(lista))
    
    def detalleJugadoresXCategoria(self,categoria,lista):
        self.vista.listarJugadoresCategoria(categoria.getListaJugadores(lista))
        