class Empresa:
    def __init__(self,nombre,rubro,trabajadores):
        self.nombre=nombre
        self.rubro=rubro
        self.trabajadores=trabajadores
    
    def set_trabajadores(self,nuevo_trab):
        self.trabajadores=nuevo_trab
    
    def get_trabajadores():
        return self.trabajadores