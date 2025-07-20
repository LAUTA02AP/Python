def consultarParidad():
    valorA = int(input('ingrese un numero: '))
    resultado = valorA %2
    if resultado == 0:
        print('su numero es par')
    else:
        print('su numero es impar')
