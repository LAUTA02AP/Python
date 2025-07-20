def calcularEdad():
    def pedirEdad():
        while True:
            try:
                edad = int(input('\ningrese su edad: '))
                if edad > 0: 
                    return edad
                else:
                    print("la edad esta en numeros negativos. Intenta de nuevo")
            except ValueError:
                print("Error: Debes ingresar un número entero válido.")
    
    edad = pedirEdad()            
    if edad >= 18:
        print('\nUsted es mayor de edad: ')
    else:
        print('\nUsted es menor de edad ')
