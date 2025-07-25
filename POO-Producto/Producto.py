class Producto:
    def __init__(self,nombre,precio,cantidad,vendidos):
        self.nombre=nombre
        self.precio=precio
        self.cantidad = cantidad
        self.__vendidos=vendidos

    def get_vendidos(self):
        return self.__vendidos




    def __str__(self):
        return f"{self.nombre}"

    def vender(self,venta):
        if self.cantidad >= venta:
            self.cantidad -= venta
            self.__vendidos += venta
            print(f'quedan {self.cantidad} unidades')
        else:
            print('no hay suficientes productos')




