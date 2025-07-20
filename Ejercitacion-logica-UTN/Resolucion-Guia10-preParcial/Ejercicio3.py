def choferes():
    nombre = input('Ingrese el nombre y apellido del conductor: ')
    tipo = int(input('Ingrese "1" para categoría 1-2, "2" para categoría 3-4 y "3" para categoría 5: '))
    servicio = int(input('Ingrese los años que el chofer trabaja para la empresa: '))
    faltas = int(input('Ingrese cuántas faltas tuvo este mes: '))

    match tipo:
        case 1:
            sueldo = 7000
            antiguedad = sueldo * 0.02 * servicio
            if faltas == 0:
                premio = 2000
            else:
                premio = 0
            total = sueldo + antiguedad + premio
            print(f'El chofer {nombre} trabajó 8 hs diarias, conduce colectivo de dos pisos, y tuvo {faltas} faltas.')
            print(f'Sueldo básico: ${sueldo}')
            print(f'Antigüedad: ${antiguedad}')
            if premio > 0:
                print(f'Premio por asistencia perfecta: ${premio}')
            print(f'Total a pagar: ${total}')
            
        case 2:
            sueldo = 5000
            antiguedad = sueldo * 0.02 * servicio
            if faltas == 0:
                premio = 2000
            else:
                premio = 0
            total = sueldo + antiguedad + premio
            print(f'El chofer {nombre} trabajó 12 hs diarias, conduce colectivo de un piso, y tuvo {faltas} faltas.')
            print(f'Sueldo básico: ${sueldo}')
            print(f'Antigüedad: ${antiguedad}')
            if premio > 0:
                print(f'Premio por asistencia perfecta: ${premio}')
            print(f'Total a pagar: ${total}')
            
        case 3:
            sueldo = 3000
            antiguedad = sueldo * 0.02 * servicio
            if faltas == 0:
                premio = 2000
            else:
                premio = 0
            total = sueldo + antiguedad + premio
            print(f'El chofer {nombre} trabajó menos de 8 hs diarias, conduce colectivo de un piso, y tuvo {faltas} faltas.')
            print(f'Sueldo básico: ${sueldo}')
            print(f'Antigüedad: ${antiguedad}')
            if premio > 0:
                print(f'Premio por asistencia perfecta: ${premio}')
            print(f'Total a pagar: ${total}')
            
        case _:
            print('Error: categoría no válida. Ingrese 1, 2 o 3.')
