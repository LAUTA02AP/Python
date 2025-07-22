import datetime as d
from Personas import Personas
import tkinter as tk
from tkinter import messagebox, font
import winsound 

gente =[]
hoy = d.datetime.now()

def cargar_cumples():
    with open("cumples.txt", "r") as f:
        for linea in f:
            dato = linea.strip().split(",")
            nombre = dato[0]
            apellido = dato[1]
            fecha_cumple = dato[2]
            telefono = dato[3]
            mail = dato[4]
            estado = dato[5]
            persona = Personas(nombre,apellido,fecha_cumple,telefono,mail,estado)
            gente.append(persona)


def alerta_cumple(persona, edad):
    winsound.PlaySound("sound/tada.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
   
    root = tk.Tk()
    root.title("🎉 ¡Cumpleaños Hoy! 🎂")
    root.geometry("350x150")
    root.configure(bg="#3E1F92") 
    root.eval('tk::PlaceWindow . center')

    fuente_titulo = font.Font(family="Helvetica", size=16, weight="bold")
    fuente_mensaje = font.Font(family="Helvetica", size=12)

    titulo = tk.Label(root, text="¡Atención!", bg="#3E1F92", fg="#F9DC5C", font=fuente_titulo)
    titulo.pack(pady=(10, 5))
    #mensaje
    mensaje = f"{persona.nombre} {persona.apellido} cumple {edad} años hoy.\nNo olvides felicitarlo/a."
    etiqueta = tk.Label(root, text=mensaje, bg="#3E1F92", fg="#FFFFFF", font=fuente_mensaje, justify="center")
    etiqueta.pack(pady=5, padx=10)

    # Botón para cerrar la ventana
    boton_cerrar = tk.Button(root, text="Cerrar", command=root.destroy, bg="#F9DC5C", fg="#3E1F92", font=fuente_mensaje)
    boton_cerrar.pack(pady=(10, 10))
    
    root.mainloop()

def cumplehoy():
    hoy = d.datetime.now()
    hoy_cumple = False
    for persona in gente:
        if Personas.isHabilitada(persona):
            cumple_persona = d.datetime.strptime(persona.fecha_cumple, "%d/%m/%Y")
            if (hoy.month, hoy.day) == (cumple_persona.month, cumple_persona.day):
                edad = hoy.year - cumple_persona.year
                Personas.saludar(persona)
                print(f"Recordar que {persona.nombre} cumple {edad} años hoy!")
                alerta_cumple(persona, edad)
                hoy_cumple = True
    if not hoy_cumple:
        print("HOY NO HAY CUMPLES\n")



def consultar_cumple(nombre,apellido):
    for persona in gente:
        if Personas.isHabilitada(persona):
            if persona.nombre == nombre and persona.apellido == apellido:
                cumple_persona = (d.datetime.strptime(persona.fecha_cumple, "%d/%m/%Y"))
                print(f"hoy es {hoy.day}/{hoy.month}")
                print(f"esta persona los cumple el {cumple_persona.day}/{cumple_persona.month}\n")

def consultar_cumples_mes():
    hoy = d.datetime.now()
    cumples_mes = []

    for persona in gente:
        if Personas.isHabilitada(persona):
            fecha = d.datetime.strptime(persona.fecha_cumple, "%d/%m/%Y")
            if fecha.month == hoy.month:
                persona.dia_del_cumple = fecha.day
                cumples_mes.append(persona)

    for i in range(len(cumples_mes) - 1):
        for j in range(i + 1, len(cumples_mes)):
            if cumples_mes[i].dia_del_cumple > cumples_mes[j].dia_del_cumple:
                cumples_mes[i], cumples_mes[j] = cumples_mes[j], cumples_mes[i]

    print("CUMPLEAÑOS DE ESTE MES (ordenados por día):\n")
    for persona in cumples_mes:
        print(f"{persona.nombre} {persona.apellido} — Día {persona.dia_del_cumple}")
    

def remover_persona(nombre,apellido):
    for persona in gente:
        if Personas.isHabilitada(persona):
            if persona.nombre == nombre and persona.apellido == apellido:
                persona.estado = "0"
                print("la persona se deshabilito correctamente")
            if persona.estado == "0":
                print("la persona ya esta deshabilitada")

def agregar_persona():
    nombre = input('ingrese el nombre de la persona:')
    apellido = input('ingrese el apellido de la persona:')
    fecha = input('ingrese la fecha de su cumple:')
    telefono = input("ingrese el telefono:")
    mail = input("ingrese su correo:")
    estado = "1"
    with open("cumples.txt","a") as f:
        f.write(f"\n{nombre},{apellido},{fecha},{telefono},{mail},{estado}")

def mostrar_todos_los_cumples():
    hoy = d.datetime.now()
    cumples_proximos = []

    for persona in gente:
        if Personas.isHabilitada(persona):
            fecha_nac = d.datetime.strptime(persona.fecha_cumple, "%d/%m/%Y")
            cumple = fecha_nac.replace(year=hoy.year)

            if cumple < hoy:
                cumple = cumple.replace(year=hoy.year + 1)

            dias_restantes = (cumple - hoy).days

            persona.dias_para_cumple = dias_restantes
            cumples_proximos.append(persona)

    for i in range(len(cumples_proximos) - 1):
        for j in range(i + 1, len(cumples_proximos)):
            if cumples_proximos[i].dias_para_cumple > cumples_proximos[j].dias_para_cumple:
                cumples_proximos[i], cumples_proximos[j] = cumples_proximos[j], cumples_proximos[i]

    print("\n------------------------REGISTRO DE TODOS LOS CUMPLEAÑOS:-------------------------")
    print("-Se mostraran los cumpleaños en orden de proximidad")
    print("-Se moestraran los dias faltantes de los mismos\n")
    
    for persona in cumples_proximos:
        Personas.consultar_todos(persona)
        print(f"-Faltan {persona.dias_para_cumple} días para su cumpleaños")
        
    
def main():
    cargar_cumples()
    while True:
        print("1 para ver si hoy hay cumpleaños")
        print("2 para mostrar todos los cumpleaños registrados")
        print("3 para consultar el cumpleaños de una persona en especifico")
        print("4 ver los cumpleaños de este mes")
        print("5 desabilitar persona")
        print("6 agregar persona")
        print("0 para salir")
        
        opcion = int(input("\nIngrese el número: "))
        if opcion == 1:
            cumplehoy()
        elif opcion == 2:
            mostrar_todos_los_cumples()
        elif opcion == 3:
            nombre = input("ingrese el nombre de la persona: ")
            apellido = input("ingrese el apellido: ")
            consultar_cumple(nombre,apellido)
        elif opcion == 4:
            consultar_cumples_mes()
        elif opcion == 5:
            print("para poder deshabilitar un apersona debe colocar su nombre y apellido")
            nombre = input("ingrese el nombre: ")
            apellido = input("ingrese el apellido: ")
            remover_persona(nombre,apellido)
        elif opcion == 6:
            agregar_persona()
        elif opcion == 7:
            break
        else:
            print("ingrese una opcion valida")

if __name__ == "__main__":
    main()



# mensaje automatico al numero telefonico,ordenar cumpleanios(por fecha)
#modificar formato de archivo (lo coloque asi debido a un  eroor en la lectura)
