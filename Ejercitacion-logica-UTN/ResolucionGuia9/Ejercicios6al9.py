##EJERCICIO 6
def factorial():
    print("-----CALCULAR FACTORIALES-----")
    numero = int(input("ingrese un número entero positivo: "))

    factorial = 1

    print("los factoriales son:")
    for i in range(1, numero + 1):
        factorial *= i

    print(f"El factorial de {numero} Es = {factorial}")


#EJERCICIO 7
def ejercicio7():
    negativos = 0
    positivos = 0
    count = 0
    for i in range(6):
        numero = int(input("ingrese un numero mi rey: "))
        
        if numero < 0:
            negativos += numero
            
        if numero > 0:
            positivos += numero
            count += 1
    print(f"La sumatoria de los numeros negativos ingresados es = {negativos}")
    
    if positivos == 0:
        print("No hay valores positvos")
    else:
        promedio = (positivos/count)
        print(promedio)

#EJERCICIO 8
def calculoMonto():
    print("\nEste programa hace la suma de montos")
    print("Para dejar de cargar datos precione 0")
    print("no se permite la carga de negativos\n")
    
    montoTotal = 0
    while True:
        monto = float(input("Ingrese el Monto a sumar:"))
        if monto == 0:
            break
        elif monto > 0 :
            montoTotal += monto
        else:
            print("Usted ingreso un numero negativo, intente nuevamente")
    
    if montoTotal > 1000:
        montoFinal= montoTotal-(montoTotal*10)/100
        print(f"Monto original: {montoTotal}")
        print("Dado que el monto supera los 1000, se aplica un descuento del 10%.")
        print(f"Monto final con el descuento aplicado: {montoFinal}")
    else:
        print(f"Su monto total es de {montoTotal}")
        
#EJERCICIO 9

def CalculonumeroMayor():
    numeroMayor = 0
    print("Este prgrama te permite ingresar una x cantidad de numeros y descubrir cual es el mayor")
    while True:
        numeroUsuario = int(input("Ingrese un numero cualquiera o 0 para salir: "))
        if numeroUsuario >= 0:
            if numeroUsuario > numeroMayor:
                numeroMayor = numeroUsuario
        else:
            print("Ingrese un numero positivo")
        if numeroUsuario == 0:
            break
        
    
    print(f"El numero mayor ingresado fue el {numeroMayor}")   

