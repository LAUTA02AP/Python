from model.Jugador import Jugador
from view.VistaJugador import VistaJugador



class ControllerJugadores:
    def __init__(self,controllerClub,controllerCategoria):
        self.vista=VistaJugador()
        self.listaJugadores =[]
        self.controllerClub = controllerClub
        self.controllerCategoria = controllerCategoria

    def cargarJugador(self):
        with open("20/jugadores.txt","r",encoding="utf-8") as f:
            renglones = f.readlines()
            for renglon in renglones:
                dni,apellido,nombre,codclub,codcategoria,goles,amon,axp = renglon.strip().split(",")
                objClub = self.controllerClub.buscarObj(codclub)
                objCate = self.controllerCategoria.buscarObj(codcategoria)
                self.listaJugadores.append(Jugador(dni,apellido,nombre,objClub,objCate,goles,amon,axp))

    def mostrarListaJugadores(self):
        self.vista.mostrarLista(self.listaJugadores)

    def registrarJugador(self):
        dni = self.vista.ingresarDatos("DNI")
        apellido = self.vista.ingresarDatos("apellido")
        nombre = self.vista.ingresarDatos("nombre")
        self.controllerClub.mostrarListaClub()
        codClub = self.vista.ingresarDatos("ingrese el codigo del club")
        self.controllerCategoria.mostrarListaCategoria()
        codCat = self.vista.ingresarDatos("ingrese el cod de la categoria")
        goles = self.vista.ingresarDatos("goles")
        amarillas = self.vista.ingresarDatos("amonestaciones")
        expulciones = self.vista.ingresarDatos("expulsiones")
        with open("20/jugadores.txt","a") as f:
            f.write(f"\n{dni},{apellido},{nombre},{codClub},{codCat},{goles},{amarillas},{expulciones}")

    def mostrarTodo(self):
        self.vista.listarDetallado(self.listaJugadores)

    def mostrarDesem(self):
        for i in self.listaJugadores:
            self.vista.mostrar(i.getPuntosDesem())
    
    def listaJugadoresXClubXCategoria(self,club,categoria):
        listaJugadoresClubCategoria = []
        for i in self.listaJugadores:
            if (i.club.codigo == club.codigo and i.categoria.codigo == categoria.codigo):
                listaJugadoresClubCategoria.append(i)
        self.vista.listarDetallado(listaJugadoresClubCategoria)
        