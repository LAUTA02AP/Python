
def empresaSalas():
    edad = int(input("Ingrese su edad: "))
    print("-" * 20)

    if edad >= 0 and edad < 4:
        print("Su entrada es gratuita")
    elif 4 <= edad < 18:
        print("Usted debe abonar $500 para poder ingresar")
    elif edad >= 18:
        print("Usted debe abonar $800 para poder ingresar")
    elif edad <0:
        print("Ingresó un número negativo")

    print("-" * 20)
