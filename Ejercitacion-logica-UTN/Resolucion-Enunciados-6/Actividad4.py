
def escribirNum():
    try:
        N = int(input('Ingrese un número del 1 al 10: '))
        if 1 <= N <= 10:
            match str(N):
                case "1":
                    print("uno")
                case "2":
                    print("dos")
                case "3":
                    print("tres")
                case "4":
                    print("cuatro")
                case "5":
                    print("cinco")
                case "6":
                    print("seis")
                case "7":
                    print("siete")
                case "8":
                    print("ocho")
                case "9":
                    print("nueve")
                case "10":
                    print("diez")
        else:
            print("Error: solo se aceptan números del 1 al 10.")
    except ValueError:
        print("Error: debe ingresar un número válido.")