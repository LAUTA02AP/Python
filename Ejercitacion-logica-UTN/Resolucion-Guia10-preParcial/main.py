import Ejercicio1,Ejercicio2,Ejercicio3,Ejercicio4,Ejercicio5
def main():
    print("Resolucion de Activades de la Guia 10")
    
    while True:
        print("\n-----MENU DE OPCIONES-----")
        print("\nIngrese el 1 para la actividad 1")
        print("Ingrese el 2 para la actividad 2")
        print("Ingrese el 3 para la actividad 3")
        print("Ingrese el 4 para la actividad 4")
        print("Ingrese el 5 para la actividad 5")
        print("Ingrese el 0 para salir\n")
        
        numero = input("Ingrese el numero de la actividad que desee ejecutar: ")
        if numero == '1':
            print("\n---Actividad 1---")
            Ejercicio1.cajero()
        elif numero == '2':
            print("\n---Actividad 2---")
            Ejercicio2.pulsaciones_correctas()
        elif numero == '3':
            print("\n---Actividad 3---")
            Ejercicio3.choferes()
        elif numero == '4':
            print("\n---Actividad 4---")
            Ejercicio4.contaminante()
        elif numero == '5':
            print("\n---Actividad 5---")
            Ejercicio5.plantaVTV()
        elif numero == '0':
            print("Fin del Programa")
            break
        else:
            print("Ingrese una opción válida")
    
            
if __name__ == '__main__':
    main()