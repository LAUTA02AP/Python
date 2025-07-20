import Actividad1,Actividad2,Actividad3,Actividad4,Actividad5,Actividad6

def main():
    print("Resolucion de Activades de la Guia 7")
    
    while True:
        print("\n-----MENU DE OPCIONES-----")
        print("\nIngrese el 1 para la actividad 1")
        print("Ingrese el 2 para la actividad 2")
        print("Ingrese el 3 para la actividad 3")
        print("Ingrese el 4 para la actividad 4")
        print("Ingrese el 5 para la actividad 5")
        print("Ingrese el 6 para la actividad 6")
        print("Ingrese el 0 para salir\n")
        numero = int(input("Ingrese el numero de la actividad que desee ejecutar: "))
        if numero == 1:
            print("\n---Actividad 1---")
            Actividad1.empresaSalas()
        elif numero == 2:
            print("\n---Actividad 2---")
            Actividad2.descuentoAlmacen()
        elif numero == 3:
            print("\n---Actividad 3---")
            Actividad3.descuentoFruteria()
        elif numero == 4:
            print("\n---Actividad 4---")
            Actividad4.circuito()
        elif numero == 5:
            Actividad5.intercepcion()
        elif numero == 6:
            Actividad6.calculoRenta()
        elif numero == 0:
            break
        else:
            print("Ingrese un numero valido")
    
            
if __name__ == '__main__':
    main()