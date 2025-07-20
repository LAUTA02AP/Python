
#EJERCICIO 1
def piramide():
    filas = int(input("Ingrese la cantidad de filas: "))
    for i in range(1, filas + 1):
        num = 2 * i - 1 
        for j in range(i):
            print(num - 2 * j, end=" ")
        print()  



        
#EJERCICIO 2
def contra():
    contra = input("registre su password: ").strip()
    
    intento= 0
    while intento < 3:
        verificar = input("ingrese su passwaord: ").strip()
        if verificar == contra:
            print("\n####Contraseña válida####\n")
            break
        else:
            print("\nPassword incorrecta intente nuevamente")
            intento +=1
            print(f"Le quedan {3-intento} intentos")
    else:
        print("\nSe le acabaron los intentos.Usted no puede ingresar\n")

#EJERCICIO 3
def primo():
    numero = int(input("Ingresa un número: "))

    if numero <= 1:
        print("No es primo")
    else:
        es_primo = True

        for i in range(2, numero):
            if numero % i == 0:
                es_primo = False
                break

        if es_primo:
            print("Es primo")
        else:
            print("No es primo")

#EJERCICIO 4
def sumatoria():
    print("se sumaron todos los numeros del 1 al 100 y")

    # coloco las variables para acumular
    suma = 0
    contador = 0

    # uso del buble para relizar la suma
    while contador <= 100:
        suma += contador
        contador += 1

    print(f"la suma es: {suma}")

#EJERCICIO 5
def divisores_positivos():
    numero = int(input("ingrese un número: "))
    contador = 1

    print(f"los divisores de {numero} son:")
    while contador <= numero:
        if numero % contador == 0:
            print(contador)
        contador += 1
