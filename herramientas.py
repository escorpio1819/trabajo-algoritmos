class Herramientas:
    def __init__(self,tipo,precio,marca,cantidad,existencia):
        self.tipo=tipo
        self.precio=precio
        self.marca=marca
        self.cantidad=cantidad
        self.existencia=existencia
    
    def set_tipo(self,nuevo_tipo):
        self.tipo=nuevo_tipo
    def set_precio(self,nuevo_precio):
        self.precio=nuevo_precio
    def set_marca(self,nueva_marca):
        self.marca=nueva_marca
    def set_cantidad(self,nueva_cantidad):
        self.cantidad=nueva_cantidad
    
    def get_tipo():
        return self.tipo
    def get_precio():
        return self.precio
    def get_marca():
        return self.marca
    def get_cantidad():
        return self.cantidad
    def get_exixtencia():
        return self.existencia