def descuentoFruteria():
    print("descuentos por kilo")
    print("apartir de los 2kg")
    print("-"*40)
    print("de 2.1 a 5 kg hay %10 de descuento")
    print("de 5.1 a 10 kg hay %15 de descuento")
    print("de 10.1 kg en adelante hay %20 de descuento")
    print("-"*40)
    print("entonces ¿que desea llevar?")
    print("-"*40)

    #pido los datos
    fruta = input("ingrese la verdura o fruta que desee llevar: ")
    cantidad = float(input("ingrese la cantidad desee comprar: "))
    precio = float(input("ingrese el valor por kg: $"))

    #realizo el calculo
    resultado1 = cantidad * precio
    resultado2 = resultado1 - (resultado1*5)/100
    resultado3 = resultado1 - (resultado1*10)/100
    resultado4 = resultado1 - (resultado1*20)/100
    #resultados con descuentos
    if cantidad <=2:
        print(f" usted debe pagar ${resultado1}")
    if cantidad > 2 and cantidad<=5:
        print(f" usted debe pagar ${resultado2}")
        print(f"el valor sin el descuento es ${resultado1}")
    if cantidad > 5 and cantidad <=10:
        print(f" usted debe pagar ${resultado3}")
        print(f"el valor sin el descuento es ${resultado1}")
    if cantidad >10:
        print(f" con el descuento usted debe pagar ${resultado4}")
        print(f"el valor sin el descuento es ${resultado1}")

    print("-" * 40)
    print("--MUCHAS GRACIAS POR SU COMPRA---")
    print("-"*40)