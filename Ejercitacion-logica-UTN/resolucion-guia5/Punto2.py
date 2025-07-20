def calculoDiscriminante():
    a = float(input("Ingrese el valor de A: "))
    b = float(input("Ingrese el valor de B: "))
    c = float(input("Ingrese el valor de C: "))

    discriminante = b**2 - 4*a*c

    print(f'El resultado del discriminante es: {discriminante}')

    if discriminante >= 0:
        print("Las raíces son reales")
    else:
        print("Las raíces no son reales")

if __name__ == '__main__':
    calculoDiscriminante()