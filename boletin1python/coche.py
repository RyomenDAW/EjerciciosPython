class coche:
    
    
    def __init__ (self, marca="",modelo=""):
        self.marca = marca
        self.modelo = modelo
        
    def devolveratributos(self):
        return (self.marca, self.modelo)
