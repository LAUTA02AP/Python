# La actividad requiere entregar un máximo de 60 billetes.
# Sin embargo, dado el rango de montos permitidos (entre $1000 y $50000)
# y las denominaciones disponibles, la cantidad máxima de billetes
# necesaria para cubrir cualquier monto dentro del rango nunca excede los 60.
# Por lo tanto, esta restricción ya queda implícita en el rango definido.
#igual mente puse un contador de billetes 


def cajero():
    while True:
        print("Solo puede retirar montos entre $1000 y $50000")
        cantidad = int(input("Ingrese el monto que quiere retirar: $"))
        
        if cantidad < 1000 or cantidad > 50000:
            print("El monto que ingreso no esta dentro del rango permisible. Intente de nuevo\n")
        else:
            break

    contadorBilletes = 0

    billetes_1000 = cantidad // 1000
    cantidad = cantidad % 1000
    if billetes_1000 > 0:
        contadorBilletes += billetes_1000
        print(f'Billetes de 1000 = {billetes_1000}')

    billetes_500 = cantidad // 500
    cantidad = cantidad % 500
    if billetes_500 > 0:
        contadorBilletes += billetes_500
        print(f'Billetes de 500 = {billetes_500}')

    billetes_200 = cantidad // 200
    cantidad = cantidad % 200
    if billetes_200 > 0:
        contadorBilletes += billetes_200
        print(f'Billetes de 200 = {billetes_200}')

    billetes_100 = cantidad // 100
    cantidad = cantidad % 100
    if billetes_100 > 0:
        contadorBilletes += billetes_100
        print(f'Billetes de 100 = {billetes_100}')

    billetes_50 = cantidad // 50
    cantidad = cantidad % 50
    if billetes_50 > 0:
        contadorBilletes += billetes_50
        print(f'Billetes de 50 = {billetes_50}')

    billetes_20 = cantidad // 20
    cantidad = cantidad % 20
    if billetes_20 > 0:
        contadorBilletes += billetes_20
        print(f'Billetes de 20 = {billetes_20}')

    billetes_10 = cantidad // 10
    cantidad = cantidad % 10
    if billetes_10 > 0:
        contadorBilletes += billetes_10
        print(f'Billetes de 10 = {billetes_10}')
    print(f"En total se le entregaron {contadorBilletes} billetes")

