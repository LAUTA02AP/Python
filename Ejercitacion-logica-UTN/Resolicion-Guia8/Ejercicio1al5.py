#EJERCICIO 1
def promedio():
    cant = int(input("ingrese la cantidad de numeros que desee promediar: "))
    acu=0
    for i in range(cant):
        numero= int(input("ingrese numero: "))
        acu = acu + numero
    promedio = acu/cant
    print(f"su promedio es de {promedio}")


#EJERCICIO 2
def impares_menores_cien():
    for i in range(1,100,2):
        print(i)
#otra forma en la que pude hacerlo 
def impares_residuo():
    for i in range(1,100):
        if (i % 2) != 0:
            print (i)

#EJERCICIO 3

def pares():
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        
        if num2 > num1 :
            print(f"Los numeros pares entre {num1} y el {num2} son: ")
            for i in range(num1, num2+1): # le sumo 1 para que se tenga en cuenta el numero ingresado
                if i % 2 == 0:
                    print(i)
        elif num2 < num1:
            print(f"Los numeros pares entre {num2} y el {num1} son: ")
            for i in range(num2,num1+1):
                if i % 2 == 0:
                    print(i)
        else:
            print("Los numeros son iguales")

# EJERCICIO 4

def triangulo():
    altura= int(input("Ingrese la altura del triángulo: "))
    acum= 0 
    for i in range(altura + 1):
        print("*"*i)
        acum = acum + i 

# EJERCICIO 5

def eco():
    print("ESTE PROGRAMA MUESTRA EL ECO DE UNA PALABRA")
    print("SI DESEA FINALIZAR ESCRIBRA SALIR")
    while True:
        palabra = input("introduzca una palabra: ")
        print(palabra)
        
        if palabra.lower() == "salir":
            break
