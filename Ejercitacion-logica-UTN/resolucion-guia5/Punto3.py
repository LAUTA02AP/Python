    
def ventasInformatica(): 
    #ingreso las constantes
    INGRESO_PC = 12
    INGRESO_DE_IMPRESORA = 7
    IVA = 21
    #pido el precio
    pc = float(input("ingrese el costo de la PC: $"))
    impresora = float(input("ingrese el valor de la impresora: $"))
    #calculo el valor total
    precio_pc = pc + (pc * INGRESO_PC/100)
    precio_impresora = impresora + (impresora * INGRESO_DE_IMPRESORA/100)
    precio_pc_impuestos = precio_pc+(precio_pc * IVA/100)
    precio_impresora_impuestos = precio_impresora+(precio_impresora * IVA/100)
    precio_total = precio_pc_impuestos + precio_impresora_impuestos

    #imprimo el resultado
    print("-----------------------------------------")
    print(f'El total a pagar es de $ {precio_total} ')


if __name__ == '__main__':      
    ventasInformatica()
    