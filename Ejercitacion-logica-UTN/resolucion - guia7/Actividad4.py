def circuito():
    print("                 ----💡----               ")
    print("Para encender el dispositivo, al menos dos interruptores deben estar cerrados (1).")
    print("-" * 80)
    print("Coloque 1 al interruptor que está CERRADO y 0 al que está ABIERTO.")
    print("-" * 80)

    # Defino variables
    primer_disp = int(input("Primer dispositivo: "))
    segundo_disp = int(input("Segundo dispositivo: "))
    tercer_disp = int(input("Tercer dispositivo: "))

    # Validación individual
    if primer_disp > 1 or primer_disp < 0:
        print("¡ERROR! INGRESE UNA OPCIÓN VÁLIDA EN EL PRIMER DISPOSITIVO (0 o 1).")
    elif segundo_disp > 1 or segundo_disp < 0:
        print("¡ERROR! INGRESE UNA OPCIÓN VÁLIDA EN EL SEGUNDO DISPOSITIVO (0 o 1).")
    elif tercer_disp > 1 or tercer_disp < 0:
        print("¡ERROR! INGRESE UNA OPCIÓN VÁLIDA EN EL TERCER DISPOSITIVO (0 o 1).")
    else:
        # Comparaciones lógicas según combinaciones posibles
        if primer_disp == 1 and segundo_disp == 1:
            print("El circuito está encendido -💡-")
        elif primer_disp == 1 and tercer_disp == 1:
            print("El circuito está encendido -💡-")
        elif segundo_disp == 1 and tercer_disp == 1:
            print("El circuito está encendido -💡-")
        else:
            print("--- El circuito no enciende ---")



