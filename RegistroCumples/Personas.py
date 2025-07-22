class Personas:
    def __init__(self,nombre,apellido,fecha_cumple,telefono,mail,estado):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_cumple = fecha_cumple
        self.telefono = telefono
        self.mail = mail
        self.estado = estado

    def __str__(self):
        return f"{self.nombre}"

    def saludar(self):
        print(f"HOY ES EL CUMPLE DE {self.nombre} {self.apellido}")
        print(f"----------ENVIALE SUS FELICIDADES----------")
        print(f"su telefono = {self.telefono}, y correo = {self.mail}")

    def consultar_todos(self):
        print(f"{self.fecha_cumple},{self.nombre}-{self.apellido}")

    def isHabilitada(self):
        return self.estado == "1"

