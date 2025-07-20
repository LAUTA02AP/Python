def plantaVTV():
   nombre = input("Ingrese el nombre del cliente: ")
   auto = input("Ingrese el modelo del auto: ")
   patente = input("Ingrese el número de patente: ")
   dni = int(input("Ingrese el DNI del cliente: "))

   while True:
      vencimiento = input("¿El cliente tiene VTV vencida? (Si/No): ").strip().lower()
      if (vencimiento == "si" or vencimiento =="no"):
         break
      else:
         print("Ingrese un valor valido")
   while True:
      comprobante = input("¿El cliente tiene comprobante? (Si/No): ").strip().lower()
      if (comprobante == "si" or comprobante =="no"):
         break
      else:
         print("Ingrese un valor valido")

   orden = int(input("Ingrese el número de orden: "))

   # Tarifa fija
   monto = 1560
   descuento1 = 0  
   descuento2 = 0  

   if vencimiento == "no":
      descuento2 = monto * 0.07

   if comprobante == "si":
      print("---- El cliente tiene comprobante ----")
      horas = int(input("Ingrese la cantidad de horas que esperó el cliente: "))
      if 1 <= horas <= 4:
         descuento1 = monto * 0.02
      elif 4 < horas <= 6:
         descuento1 = monto * 0.05
      elif horas > 6:
         descuento1 = monto * 0.10
      else:
         descuento1 = 0

   montoF = monto - descuento1 - descuento2

   # Mostrar resultados
   print("\n-------------------------------")
   print(f"Orden --- Nº{orden} ---")
   print(f"Cliente: {nombre}")
   print(f"DNI: {dni}")
   print(f"Vehículo: {auto}, Patente: {patente}")
   print("-" * 30)
   print(f"Tarifa fija = $1560")
   if comprobante == "si":
      print(f"Descuento por espera: ${descuento1:.2f}")
   else:
      print("No tiene comprobante.")

   if vencimiento == "no":
      print(f"Descuento por VTV vigente: ${descuento2:.2f}")
   else:
      print("No tiene VTV vigente.")
   print("-" * 30)
   print(f"TOTAL A PAGAR: ${montoF:.2f}\n")



