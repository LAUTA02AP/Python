def contaminante():
    #Primero saco el costo unitario de la pileta
    print('ingrese el costo de los materiales para realizar 1 pileta:')
    costo_vidrio= float(input ('ingrese el costo de la fibra de videio utilizada: $'))
    costo_quimico =  float(input('ingrese el costo de los quimicos utilizados: $'))
    mano_obra = float (input('ingrese el valor de la mano de obra: $'))
    costo_unitario = costo_quimico + costo_vidrio + mano_obra
    print("-"*40)

    #Calculo la ganancia diaria 
    precio_venta = int(input('ingrese el valor de la pileta: $'))
    ganancia_por_unidad = precio_venta - costo_unitario
    piletas_vendidas = int(input("cuantas piletas se venden por dia?: "))
    ganancia_diaria = ganancia_por_unidad * piletas_vendidas
    print(f"Su ganancia diaria es de {ganancia_diaria} ")
    print("-"*40)
    #Aplico las reglas del IMECA
    print("CONTROL DE PUNTOS IMECA")
    puntos_total = 0
    for i in range(1,5+1):
        puntos = int(input(f"ingrese los puntos IMECA obtenidos en el dia {i}: "))
        puntos_total += puntos

    promedioIMECA= puntos_total / 5
    multa = ganancia_diaria / 2
    perdida = (ganancia_diaria * 7) + multa
    if promedioIMECA <= 170:
        print("\nSu IMECA es normal, sus niveles de contaminacion son bajos")
        print("Su ganancia permanecera igual")
    if promedioIMECA > 170:
        print("🚨🚨🚨----------------------⚠️--⚠️--⚠️------------------------🚨🚨🚨")
        print("\nSu IMECA ES ALTO, TIENE CONTAMINACION GRAVE")
        print(f"DEBE SUSPENDER SU PRODUCCION POR 7 DIAS, PERDERA ${ganancia_diaria * 7}") #calcule * 5 por que 
        print(f"TAMBIEN DEBERA A BONAR UNA MULTA DE ${multa}")
        print(f"USTED TIENE UNA PERDIDA FINAL DE {perdida} POR CONTAMINACION GRAVE")
