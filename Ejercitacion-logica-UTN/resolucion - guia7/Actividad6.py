def calculoRenta():
    print("se le calculara el valor total de su renta con los tramos impositivos")
    print("--"*40)
    renta = float(input("ingrese su renta: $"))

    cuenta1 = renta + (renta*5)/100
    cuenta2 = renta + (renta*15)/100
    cuenta3 = renta + (renta*20)/100
    cuenta4 = renta + (renta*30)/100
    cuenta5 = renta + (renta*45)/100
    print(cuenta1)
    if renta < 100000:
        print("Su tipo enpositivo es del %5 ")
        print(f"el valor total de la renta es de: ${cuenta1}")
    if renta >= 100000 and renta <200000:
        print("Su tipo enpositivo es del %15 ")
        print(f"el valor total de la renta es de: ${cuenta2}")
    if 200000<= renta <350000:
        print("Su tipo enpositivo es del %20 ")
        print(f"el valor total de la renta es de: ${cuenta3}")
    if 350000<= renta <600.000:
        print("Su tipo enpositivo es del %30 ")
        print(f"el valor total de la renta es de: ${cuenta4}")
    if renta >=600000:
        print("Su tipo enpositivo es del %45 ")
        print(f"el valor total de la renta es de: ${cuenta5}")


