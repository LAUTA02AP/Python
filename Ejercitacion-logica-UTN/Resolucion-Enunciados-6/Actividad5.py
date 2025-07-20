
def descuentoAlmacen():
    valor = float(input('ingrese el valor del producto: '))
    if valor >=200:
        descuento = valor * 0.20
        total = valor - descuento
        print("Su compra fue mayor a $200 por ende tiene un descuento del %20")
        print(f"El precio final es de {total:.2f} ")
    else:
        print(f"El precio a pagar es de {valor} ")
