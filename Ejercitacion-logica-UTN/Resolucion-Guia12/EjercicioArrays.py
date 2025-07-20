#EJERCICIO 1 
def lista_reptetida():
    lista= [4, 2, 5, 2, 1, 3, 4, 5, 1,9,8,7,7,6,10, 2, 3, 5, 4, 1, 2, 3, 5, 4, 1, 3]

    lista_sin_repetidos = []

    #muestro lista 
    for i in range (len(lista)):
        if lista[i] not in lista_sin_repetidos:
            lista_sin_repetidos.append(lista[i])

    print (f"lista= {lista}")
    print(f"lista sin repetidos = {lista_sin_repetidos}")

#EJERCICIO 2
def ejercicio2():
    lista= [4, 2, 5, 2, 1, 3, 4, 5, 1, 9, 8, 7, 7, 6, 10, 2, 3, 5, 4, 1, 2, 3, 5, 4, 1, 3]

    numero_mayor = 0
    numero_menor = lista[0]
    suma = 0
    for i in range(len(lista)):
        suma = suma + lista[i]
        if lista[i] > numero_mayor:
            numero_mayor = lista[i]
        
        if numero_menor > lista[i]:
            numero_menor = lista[i]
    promedio = suma / len(lista)    
        
    print("\nDada la siguiente lista:\n")
    print(lista)
    print()
    print(f"-Se sabe que el numero mayor es = {numero_mayor}")
    print(f"-El numero menor = {numero_menor}")
    print(f"-El promedio = {promedio:.3f}\n")


def ejercicio3():
    #carga de lista 
    def cargaLista(lista):
        print("Ingresá números enteros uno por uno. Para terminar, solo presioná Enter sin escribir nada.")
        while True:
            entrada = input("Número: ")
            if entrada == "":
                break
            try:
                numero = int(entrada)
                lista.append(numero)
            except ValueError:
                print("Por favor, ingresá un número entero válido.")
    # Primero intercalamos hasta donde se pueda
    def entrelazar(lista1, lista2, lista3):
        limite = min(len(lista1), len(lista2))

        for i in range(limite):
            lista3.append(lista1[i])
            lista3.append(lista2[i])

        if len(lista1) > len(lista2):
            for i in range(limite, len(lista1)):
                lista3.append(lista1[i])
        else:
            for i in range(limite, len(lista2)):
                lista3.append(lista2[i])

        print("1. Sea el arreglo A:", lista1)
        print("2. Sea el arreglo B:", lista2)
        print("3. Se genera el arreglo intercalado:", lista3,"\n")
        
    arregloA = [3, 2, 0]
    arregloB = [7, 1, 8, 4, 5, 6]
    arregloC = []
    listaUsuarioA = []
    listaUsuarioB = []
    listaUsuarioC = []

    print("-"*60)
    print("\nEste programa se encarga de intercalar los arreglos de dos listas numericas")
    print("Como en el siguiente ejemplo")
    entrelazar(arregloA,arregloB,arregloC)

    rta = ""

    while rta != "si" and rta != "no":
        rta = input("¿Quiere hacerlo con otras 2 listas? (Si/No): ").strip().lower()

        if rta == "no":
            print("Fin del programa")
        elif rta == "si":
            print("\nCARGA LA LISTA A")
            cargaLista(listaUsuarioA)
            print("\nCARGA LA LISTA B")
            cargaLista(listaUsuarioB)
            entrelazar(listaUsuarioA,listaUsuarioB,listaUsuarioC)
        else:
            print("Ingrese un valor válido (Si/No)")

