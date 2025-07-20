def calculoPrecioFinal():
    INFLACION = 0.04
    precio_actual = float(input("Ingrese el valor del producto: $"))
    while precio_actual < 0:
        print("Error: El precio no puede ser negativo.")
        precio_actual = float(input("Ingrese el valor del producto: $"))

    anio_actual = int(input("Ingrese el año actual: "))
    anio_futuro = int(input("Ingrese el año futuro: "))

    precio_final = precio_actual * (1 + INFLACION) ** (anio_futuro - anio_actual)
    print(f"El precio final del producto para el año {anio_futuro} será de ${precio_final:.2f}.")


if __name__ == '__main__':
    calculoPrecioFinal()
