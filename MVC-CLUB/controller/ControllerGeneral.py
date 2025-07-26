from view.VistaGeneral import VistaGeneral
from controller.ControllerClub import ControllerClub
from controller.ControllerCategoria import ControllerCategoria
from controller.ControllerJugadores import ControllerJugadores
class ControllerGeneral:
    def __init__(self):
        self.vista = VistaGeneral()
        self.controllerclub = ControllerClub()
        self.controllercategoria = ControllerCategoria()
        self.controllerjugador = ControllerJugadores(self.controllerclub,self.controllercategoria)

    def cargaDeArchivo(self):
        self.controllerclub.cargarClub()
        self.controllercategoria.cargarCategoria()
        self.controllerjugador.cargarJugador()



    def iniciar(self):
        self.cargaDeArchivo()
        op=self.vista.eleccionMenu()
        while(op!=0):
            if (op==1):
                #lisar
                self.controllerjugador.mostrarTodo()
            elif op==2:
                #registro
                self.controllerjugador.registrarJugador()
            
            elif op==3:
                #listado por club
                self.controllerclub.mostrarListaClub()
                cod = self.vista.pedirDato("Codigo de club")
                objeto = self.controllerclub.buscarObj(cod)
                self.controllerclub.listarJugadoresClub(objeto,self.controllerjugador.listaJugadores)
    
            elif op==4:
                #desempenio
                self.controllerjugador.mostrarDesem()
    
            elif op==5:
                #listado por categoria
                self.controllerclub.mostrarListaClub()
                cod = self.vista.pedirDato("Codigo de club")
                objeto = self.controllerclub.buscarObj(cod)

                self.controllercategoria.mostrarListaCategoria()
                codigoCat = self.vista.pedirDato("Codigo de categoria")
                objetoCat = self.controllercategoria.buscarObj(codigoCat)
                
                self.controllerjugador.listaJugadoresXClubXCategoria(objeto,objetoCat)
            
            elif op ==6:
                #total categoria
                self.controllercategoria.mostrarListaCategoria()
                cod = self.vista.pedirDato("Codigo de categoria: ")
                objeto = self.controllercategoria.buscarObj(cod)
                self.controllercategoria.CantidadJugadoresXCategoria(objeto,self.controllerjugador.listaJugadores)
                
            elif op == 7:
                self.controllercategoria.mostrarListaCategoria()
                cod = self.vista.pedirDato("Codigo de categoria: ")
                objeto = self.controllercategoria.buscarObj(cod)
                self.controllercategoria.detalleJugadoresXCategoria(objeto,self.controllerjugador.listaJugadores)
                
                #detalle por categoriap
            elif op ==0:
                break
            else:
                self.vista.mensajeError()
            op = self.vista.eleccionMenu()