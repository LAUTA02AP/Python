
def descuentoAlmacen():
    print("Usted tiene una rebaja acorde a la cantidad de compra de un mismo producto:")
    print("\t- Más de 20 unidades: 20% de rebaja")
    print("\t- Más de 10 unidades hasta 20: 10% de rebaja")
    print("\t- 10 o menos unidades: sin rebaja")
    print("-" * 40)

    # Defino variables
    producto = input("Ingrese el nombre del producto que desea comprar: ")
    costo = float(input("Ingrese el valor unitario del producto: $"))
    cantidad = int(input("Ingrese la cantidad que desea llevar: "))

    valor = cantidad * costo

    print("-" * 40)

    if cantidad > 20:
        total = valor * 0.80
        print(f"Usted tiene un descuento del 20% en su compra de {producto}.")
        print(f"Debe pagar un total de: ${total}")

    elif cantidad > 10:
        total = valor * 0.90
        print(f"Usted tiene un descuento del 10% en su compra de {producto}.")
        print(f"Debe pagar un total de: ${total}")

    else:
        print(f"No se aplica descuento.")
        print(f"Debe pagar un total de: ${valor}")
