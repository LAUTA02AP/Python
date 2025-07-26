class VistaGeneral:
    def eleccionMenu(self):
        print("\nMENU DE OPCIONES: \n1-listado de todos los jugadores"
              "\n2-registro jugador"
              "\n3-listado club"
              "\n4-evaluacion de desempenio"
              "\n5-consultar categoria y club"
              "\n6-mostrar cantidad por categoria"
              "\n7-mostrar detalles por categoria "
              "\n0-para salir")
        op = int(input("ingrese la opcion deseada: "))
        return op

    def mensajeError(self):
        print("no ingreso un valor correcto")

    def pedirDato(self,dato):
        return input(f"ingrese el {dato} : ")