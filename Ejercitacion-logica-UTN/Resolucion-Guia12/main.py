import EjercicioArrays, EjercicioMatriz
def main():
    print("Resolucion de Activades de la Guia 12")
    
    while True:
        print("\n-----MENU DE OPCIONES-----")
        print("\nIngrese el 1 para la actividad 1")
        print("Ingrese el 2 para la actividad 2")
        print("Ingrese el 3 para la actividad 3")
        print("APARTIR DE AQUI LOS ENUNCIADOS SON MATRICES")
        print("Ingrese el 4 para la actividad 4")
        print("Ingrese el 5 para la actividad 5")
        print("Ingrese el 6 para la actividad 6")
        print("Ingrese el 7 para la actividad 7")
        print("Ingrese el 8 para la actividad 8")
        print("Ingrese el 9 para la actividad 9")
        print("Ingrese el 10 para la actividad 10")
        print("Ingrese el 0 para salir\n")
        
        numero = input("Ingrese el numero de la actividad que desee ejecutar: ")
        if numero == '1':
            print("\n---Actividad 1---")
            EjercicioArrays.lista_reptetida()
        elif numero == '2':
            print("\n---Actividad 2---")
            EjercicioArrays.ejercicio2()
        elif numero == '3':
            print("\n---Actividad 3---")
            EjercicioArrays.ejercicio3()
        elif numero == '4':
            print("\n---Actividad 4---")
            EjercicioMatriz.actividad4()
        elif numero == '5':
            print("\n---Actividad 5---")
            EjercicioMatriz.ejercicio5()
        elif numero == '6':
            print("\n---Actividad 6---")
            EjercicioMatriz.actividad6()
        elif numero == '7':
            print("\n---Actividad 7---")
            EjercicioMatriz.actividad7()
        elif numero == '8':
            print("\n---Actividad 8---")
            pass
        elif numero == '9':
            print("\n---Actividad 9---")
            pass
        elif numero == '10':
            print("\n---Actividad 10---")
            pass
        elif numero == '0':
            print("Fin del Programa")
            break
        else:
            print("Ingrese una opción válida")
    
            
if __name__ == '__main__':
    main()