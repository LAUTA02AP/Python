def isbn_correcto():
    codigo = input('ingrese un codigo ISBN:')
    sum = 0
    for i in range(len(codigo)):
        sum += int(codigo[i]) * (i+1)
    if sum % 11 == 0:
        print('"el codigo es valido"')
    else:
        print('"el codigo no es valido"')
        
#ejercicio 7 

def fabricaBotella():
    botellas_mercado = int(input("Ingrese la cantidad de botellas que hay disponibles en el mercado: "))
    botellas_necesarias = int(input("Ingrese la cantidad de botellas usadas para fabricar 1 nueva: "))
    
    total_nuevas = 0

    while botellas_mercado >= botellas_necesarias:
        nuevas = botellas_mercado // botellas_necesarias
        sobras = botellas_mercado % botellas_necesarias
        total_nuevas += nuevas
        botellas_mercado = nuevas + sobras 

    print("Total de botellas fabricadas:", total_nuevas)
    
