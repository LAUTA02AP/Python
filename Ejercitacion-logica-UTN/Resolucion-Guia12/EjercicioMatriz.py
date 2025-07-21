def actividad4():
    matriz = [
        ["meses","Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"],
        ["Dulces",870,200,300,300,500,230,170,800,800,645,230,870],
        ["Bebidas", 800,150,150,200,300,220,250, 400,180,500,190,630],
        ["Conservas", 60, 90,110,140,260,210, 190,370, 160,430,170,600] 
        ]
    
    def buscarMes(fila,costo):
        for i in range(1,len(matriz[0])):
            if matriz[fila][i] == costo:
                print(matriz[0][i], "con costo de = ",matriz[fila][i])
        
    def buscarDpto(): #se puede simplicar con la funcion anterior 
            for i in range (1,4):
                if matriz[i][8] == dptoMenorAgo:
                    print(matriz[i][0],"con costo =",matriz[i][8])
                    print()

        
    #mayor costo de dulces  
    costoMayorDulce = 0
    for i in range(1,len(matriz[0])):
        if matriz[1][i] > costoMayorDulce:
            costoMayorDulce =  matriz[1][i]
    
    #promedio anual de costos de produccion de bebidas 
    costoBebidaTotal = 0
    for i in range(1,len(matriz[0])):
        costoBebidaTotal += matriz[2][i]
    
    promedioBebida = round(costoBebidaTotal / 12,2)
            
    #Mes con menor costo registrado en bebidas
    costomenorBebidas = matriz[2][1]
    
    for i in range(1,len(matriz[0])):
        if matriz[2][i] < costomenorBebidas:
            costomenorBebidas = matriz[2][i]
    
    #Departamento que tuvo el menor costo de producción en Agosto
    dptoMenorAgo = matriz[1][8]
    for i in range(1,4):
        if matriz[i][8] < dptoMenorAgo:
            dptoMenorAgo = matriz[i][8]
                  
    print('MATRIZ USADA COMO EJEMPLO')
    for i in range(len(matriz)):
        print(matriz[i])
    
    print("-----------------------RESPUESTAS-------------------------")
    print("\nA) En el mes o meses en el que se registro el mayor costo de produccion fueron ")
    buscarMes(1,costoMayorDulce) #costo mayor dulces
    
    print(f"\nB) El Promedio anual de los costos de producción de bebidas es = {promedioBebida}")
    
    print("\nC) En el mes o meses que se registró el menor costo de producción de bebidas ")
    buscarMes(2,costomenorBebidas) # costo menor bebidas

    print("\nC)El departamento que tuvo el menor costo de producción en Agosto fue:")
    buscarDpto()
    

def ejercicio5():
    
    ventas = [
        ["V/M", "M1", "M2", "M3", "M4", "M5", "M6", "M7", "M8", "M9", "M10", "M11", "M12", "M13", "M14", "M15"],
        ["V1",  3,    1,    0,    2,    0,    1,    2,    1,    0,    1,     2,     1,     1,     2,     1],
        ["V2",  0,    2,    1,    0,    1,    2,    1,    0,    2,    1,     1,     0,     0,     1,     2],
        ["V3",  1,    0,    2,    1,    1,    0,    2,    1,    0,    0,     1,     2,     1,     1,     1],
        ["V4",  2,    1,    1,    2,    2,    1,    0,    2,    1,    1,     1,     1,     2,     0,     0],
        ["V5",  0,    0,    1,    1,    0,    0,    1,    1,    2,    1,     0,     0,     1,     2,     1],
        ["V6",  1,    2,    2,    1,    1,    2,    2,    0,    1,    2,     2,     1,     0,     1,     0],
        ["V7",  2,    1,    0,    1,    1,    1,    0,    2,    1,    0,     1,     2,     1,     1,     1],
        ["V8",  0,    1,    2,    2,    2,    0,    1,    1,    0,    1,     0,     2,     1,     0,     2],
        ["V9",  1,    0,    1,    0,    1,    2,    2,    1,    1,    0,     2,     1,     1,     2,     0],
        ["V10", 2,    1,    1,    1,    2,    1,    0,    0,    2,    2,     1,     1,     2,     1,     1]
        ]
            
    totalVendidos = []
    for fila in ventas:
            for valor in fila:
                print(f"{str(valor):>4}", end=" ")  # >4 alinea a la derecha en 4 espacios
            print()
    
    print("\n-----------       VENTAS DEL VENDEDOR     ----------")    
    for i in range(1,11):
        suma = 0
        for j in range(1,16):
            suma = suma + ventas[i][j]
            
        totalVendidos.append(suma)
        
        print(f"El vendedor V{i} tubo un total de ventas en el mes = {suma}")
        
    print("\n-----------       MODELOS VENDIDOS       ----------")
    for i in range(1,16):
        suma = 0
        for j in range(1,11):
            suma = suma + ventas[j][i]
        
        print(f"El modelo M{i} fue vendido {suma} veces en el mes")
    
    print("\n-----------       PREMIO AL MEJOR VENDEDOR      ----------")
    print("Los vendedores ganadores de este mes fueron: ")
    mayor = 0
    for i in range(len(totalVendidos)):
        if mayor < totalVendidos[i]:
            mayor = totalVendidos[i]
            
    for i in range(len(totalVendidos)):
        if mayor == totalVendidos[i]:
            print(f" V{i+1} con un total de {mayor} ventas")
    
def actividad6():
    resultados = [
    ["Distrito", "Candidato A", "Candidato B", "Candidato C", "Candidato D"],
    ["12.1", 194, 48, 206, 45],
    ["13.2", 180, 20, 320, 16],
    ["14.3", 221, 90, 140, 20],
    ["15.4", 432, 50, 821, 14],
    ["16.5", 820, 61, 946, 18]
    ]

    def imprimir_tabla(tabla):
        for fila in tabla:
            print("{:<10} {:<12} {:<12} {:<12} {:<12}".format(*fila))
            
    votos_totales = 0
    for i in range(1,6):
        for j in range(1,5):
            votos_totales += resultados[i][j]
    
    
        # Lista para acumular votos por candidato: A, B, C, D
    votos_candidatos = [0, 0, 0, 0]

    # Sumamos los votos
    for i in range(1, 6):  # filas (distritos)
        for j in range(1, 5):  # columnas (candidatos)
            votos = resultados[i][j]
            votos_candidatos[j - 1] += votos  # j-1 porque candidatos van de 0 a 3 en la lista

    
    nombres = resultados[0][1:]  # ["Candidato A", "Candidato B", "Candidato C", "Candidato D"]

    # Mostrar resultados
    print("\nLos resultados de las últimas elecciones al gobierno en el pueblo X han sido las siguientes")
    imprimir_tabla(resultados)
    print("-----------------RESULTADO DE LAS ELECCIONES--------------\n")

    porcentajes = []
    for i in range(4):
        porcentaje = round((votos_candidatos[i] / votos_totales) * 100, 2)
        porcentajes.append(porcentaje)
        
    for i in range(4):
        print(f"{nombres[i]} obtuvo el %{porcentajes[i]} = {votos_candidatos[i]} votos")

    print(f"\nTotal de votos: {votos_totales}")

    # Buscar ganador > 50%
    ganador = ""
    mayor_porcentaje = 0
    for i in range(4):
        if porcentajes[i] > 50:
            ganador = nombres[i]
            mayor_porcentaje = porcentajes[i]
            break

    if ganador != "":
        print(f"🎉 El ganador es {ganador} con el ({mayor_porcentaje}%) de los votos 🎉\n")
    else:
        max1_idx = 0
        for i in range(1, 4):
            if votos_candidatos[i] > votos_candidatos[max1_idx]:
                max1_idx = i

        max2_idx = 0 if max1_idx != 0 else 1
        for i in range(4):
            if i != max1_idx and votos_candidatos[i] > votos_candidatos[max2_idx]:
                max2_idx = i

        print("No hay ganador con más del 50%, pasan a segunda vuelta los dos candidatos con más votos:")
        print(f"- {nombres[max1_idx]} con {votos_candidatos[max1_idx]} votos ({porcentajes[max1_idx]}%)")
        print(f"- {nombres[max2_idx]} con {votos_candidatos[max2_idx]} votos ({porcentajes[max2_idx]}%)")

def actividad7():
    
    def cargar_matriz():
        dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
        meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", 
                 "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]

        matriz = []

        # Primera fila: encabezado
        encabezado = ["Mes?días"] + dias
        matriz.append(encabezado)

        # Carga de datos por cada mes
        for mes in meses:
            fila = [mes]  # primera celda: nombre del mes
            print(f"\nIngresá los datos para {mes}:")
            for dia in dias:
                while True:
                    try:
                        valor = int(input(f"  {dia.capitalize()}: "))
                        fila.append(valor)
                        break
                    except ValueError:
                        print("Ingresá solo números enteros.")
            matriz.append(fila)

        return matriz

    def mostrar_matriz(matriz):
        print("\nMatriz final:")
        for fila in matriz:
            for valor in fila:
                print(f"{str(valor):<12}", end="")  # esto es para que se vea mejor a la hora de mostrar
            print()

    def calcular_total_ventas(matriz):
        total = 0
        for i in range(1, len(matriz)):  
            for j in range(1, len(matriz[0])): 
                total += matriz[i][j]
        return total

    def calcular_ventas_por_mes(matriz):
        ventas_mes = []
        for i in range(1, len(matriz)):
            total_mes = 0
            for j in range(1, len(matriz[0])):
                total_mes += matriz[i][j]
            ventas_mes.append((matriz[i][0], total_mes))
        return ventas_mes

    #
    matriz = cargar_matriz()
    mostrar_matriz(matriz)

    total = calcular_total_ventas(matriz)
    print(f"\nTotal de ventas del año: {total}")

    print("\nVentas por mes:")
    ventas_mes = calcular_ventas_por_mes(matriz)
    for mes, total in ventas_mes:
        print(f"  {mes}: {total}")


