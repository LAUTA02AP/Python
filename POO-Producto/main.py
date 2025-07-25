from Producto import Producto
productos = []
def cargar_productos():
    with open("productos.txt","r") as f:
        for linea in f:
            datos = linea.strip().split(',')
            nombre = datos[0]
            precio = float(datos[1])
            cantidad = int(datos[2])
            ventas = int(datos[3])
            producto = Producto(nombre,precio,cantidad,ventas)
            productos.append(producto)

def consultarPrecio():
    i = 1
    for producto in productos:
        if producto.cantidad > 0:
            print(f"el producto {i} " ,producto.nombre + "-vale -$" + str(producto.precio))
            i += 1


def realizar_venta(seleccion_producto, venta):
    for producto in productos:
        if producto.nombre == seleccion_producto:
            producto.vender(venta)
def agregar_producto():
    nombre = input('ingrese el nombre del producto: ')
    precio = input('ingrese el precio: ')
    cantidad = input('ingrese la cantidad de stock: ')
    ventas = input("ingrese la cantidad vendidas")
    with open("productos.txt", "a") as f: 
        f.write(f"\n{nombre},{precio},{cantidad},{ventas}")

def main():
    cargar_productos()

    while True:
        print("\n MENU DE OPCIONES: ")
        print("\nElija una opcion")
        print("1.para consultar precios")
        print("2.para agregar producto")
        print("3.para registrar venta")
        print("0.para salir")
        opcion= int(input("ingrese una opcion: "))

        if opcion == 1:
            consultarPrecio()

        elif opcion == 2:
            agregar_producto()

        elif opcion == 3:
            consultarPrecio()
            seleccion_producto = input('selecciona el producto que desee vender: ')
            venta = int(input('ingrese la cantidad a vender: '))
            realizar_venta(seleccion_producto,venta)

        elif opcion == 0:
            break
        else:
            print("ingrese una opcion valida: \n")



if __name__ == '__main__':
    main()





