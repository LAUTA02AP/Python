import Ejercicios1al5,Ejercicios6al9
def main():
    print("Resolucion de Activades de la Guia 9")
    
    while True:
        print("\n-----MENU DE OPCIONES-----")
        print("\nIngrese el 1 para la actividad 1")
        print("Ingrese el 2 para la actividad 2")
        print("Ingrese el 3 para la actividad 3")
        print("Ingrese el 4 para la actividad 4")
        print("Ingrese el 5 para la actividad 5")
        print("Ingrese el 6 para la actividad 6")
        print("Ingrese el 7 para la actividad 7")
        print("Ingrese el 8 para la actividad 8")
        print("Ingrese el 9 para la actividad 9")
        print("Ingrese el 0 para salir\n")
        
        numero = input("Ingrese el numero de la actividad que desee ejecutar: ")
        if numero == '1':
            print("\n---Actividad 1---")
            Ejercicios1al5.piramide()
        elif numero == '2':
            print("\n---Actividad 2---")
            Ejercicios1al5.contra()
        elif numero == '3':
            print("\n---Actividad 3---")
            Ejercicios1al5.primo()
        elif numero == '4':
            print("\n---Actividad 4---")
            Ejercicios1al5.sumatoria()
        elif numero == '5':
            print("\n---Actividad 5---")
            Ejercicios1al5.divisores_positivos()
        elif numero == '6':
            print("\n---Actividad 6---")
            Ejercicios6al9.factorial()
        elif numero == '7':
            print("\n---Actividad 7---")
            Ejercicios6al9.ejercicio7()
        elif numero == '8':
            print("\n---Actividad 8---")
            Ejercicios6al9.calculoMonto()
        elif numero == '9':
            print("\n---Actividad 9---")
            Ejercicios6al9.CalculonumeroMayor()
        

        elif numero == '0':
            print("Fin del Programa")
            break
        else:
            print("Ingrese una opción válida")
    
            
if __name__ == '__main__':
    main()