import Punto1
import Punto2
import Punto3

def main():
    print("Resolución de las Actividades de la Guía 5")
    while True:
        print("\n1. Resolución del Punto 1")
        print("2. Resolución del Punto 2")
        print("3. Resolución del Punto 3")
        print("0. Salir")

        opcion = input("Ingrese el número de la opción para realizar la tarea: ")
        if opcion == '1':
            Punto1.calculoPrecioFinal()
        elif opcion == '2':
            Punto2.calculoDiscriminante()
        elif opcion == "3":
            Punto3.ventasInformatica()
        elif opcion == '0':
            print("Fin del Programa")
            break
        else:
            print("Ingrese una opción válida")

if __name__ == '__main__':
    main()
