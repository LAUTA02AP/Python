def dividir_numeros():
    try:
        num1 = float(input("Ingrese el primer número (dividendo): "))
        num2 = float(input("Ingrese el segundo número (divisor): "))
        
        resultado = num1 / num2
        print(f"El resultado de la división es: {resultado}")
    
    except ZeroDivisionError:
        print("Error: no se puede dividir por cero.")
    
    except ValueError:
        print("Error: debes ingresar números válidos.")

