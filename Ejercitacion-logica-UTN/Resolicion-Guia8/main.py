import Ejercicio1al5,Ejercicio6y7
def main():
    print("Resolucion de Activades de la Guia 8")
    
    while True:
        print("\n-----MENU DE OPCIONES-----")
        print("\nIngrese el 1 para la actividad 1")
        print("Ingrese el 2 para la actividad 2")
        print("Ingrese el 3 para la actividad 3")
        print("Ingrese el 4 para la actividad 4")
        print("Ingrese el 5 para la actividad 5")
        print("Ingrese el 6 para la actividad 6")
        print("Ingrese el 7 para la actividad 7")
        print("Ingrese el 0 para salir\n")
        
        numero = input("Ingrese el numero de la actividad que desee ejecutar: ")
        if numero == '1':
            print("\n---Actividad 1---")
            Ejercicio1al5.promedio()
        elif numero == '2':
            print("\n---Actividad 2---")
            Ejercicio1al5.impares_menores_cien()
        elif numero == '3':
            print("\n---Actividad 3---")
            Ejercicio1al5.pares()
        elif numero == '4':
            print("\n---Actividad 4---")
            Ejercicio1al5.triangulo()
        elif numero == '5':
            print("\n---Actividad 5---")
            Ejercicio1al5.eco()
        elif numero == '6':
            print("\n---Actividad 6---")
            Ejercicio6y7.isbn_correcto()
        elif numero == '7':
            print("\n---Actividad 7---")
            Ejercicio6y7.fabricaBotella()

        elif numero == '0':
            print("Fin del Programa")
            break
        else:
            print("Ingrese una opción válida")
    
            
if __name__ == '__main__':
    main()