def pulsaciones_correctas():
    edad = int(input('ingrese su edad: '))
    sexo = int(input('ingrese 1 para hombre o 2 para mujer: '))

    if 2 != sexo != 1:
        print('ingrese un numero valido')
    else:
        pulsaciones = int(input('íngrese la pulsacion obtenida en 10 seg: '))

    hombre = (210 - edad) / 10
    mujer = (220 - edad) / 10

    match sexo:
        case 1:
            if pulsaciones == hombre:
                print('sus pulsaciones son normales')
            elif pulsaciones < hombre:
                print('sus pulsaciones son bajas')
            else:  # pulsaciones > hombre
                print('sus pulsaciones son altas')
        case 2:
            if pulsaciones == mujer:
                print('sus pulsaciones son normales')
            elif pulsaciones < mujer:
                print('sus pulsaciones son bajas')
            else:  # pulsaciones > mujer
                print('sus pulsaciones son altas')

