class Madera:
    def __init__(self,largo,ancho,grosor,calidad,color,tipo,precio):
        self.largo=largo
        self.ancho=ancho
        self.grosor=grosor
        self.calidad=calidad
        self.color=color
        self.tipo=tipo
        self.precio=precio
    
    def set_largo(self,nuevo_largo):
        self.largo=nuevo_largo
    def set_ancho(self,nuevo_ancho):
        self.ancho=nuevo_ancho
    def set_grosor(self,nuevo_grosor):
        self.grosor=nuevo_grosor
    def set_precio(self,nuevo_precio):
        self.precio=nuevo_precio

    def get_largo():
        return self.largo
    def get_ancho():
        return self.ancho
    def get_grosor():
        return self.grosor
    def get_precio():
        return self.precio
    def get_calidad():
        return self.calidad
    def get_color():
        return self.color
    def get_tipo():
        return self.tipo