def intercepcion():
    print("Calcular el punto de intersección de 2 conjuntos de 3 valores")
    print("--" * 40)
    print("Para el grupo A")
    A1 = int(input("Ingrese el primer valor numérico: "))
    A2 = int(input("Ingrese el segundo valor numérico: "))
    A3 = int(input("Ingrese el tercer valor numérico: "))
    print("Para el grupo B")
    B1 = int(input("Ingrese el primer valor numérico: "))
    B2 = int(input("Ingrese el segundo valor numérico: "))
    B3 = int(input("Ingrese el tercer valor numérico: "))

    print("La intersección se da en:")

    coincidencia = False

    if A1 == B1 or A1 == B2 or A1 == B3:
        print(A1)
        coincidencia = True
    if A2 == B1 or A2 == B2 or A2 == B3:
        if A2 != A1: 
            print(A2)
            coincidencia = True
    if A3 == B1 or A3 == B2 or A3 == B3:
        if A3 != A1 and A3 != A2:
            print(A3)
            coincidencia = True

    if not coincidencia:
        print("-" * 40)
        print("Sus conjuntos no tienen intersección")
