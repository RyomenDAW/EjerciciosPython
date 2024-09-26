#Crea una clase llamada Persona con atributos nombre y edad. 
class Persona:
    
    
    def __init__(self, nombre="",edad=""):
        self.nombre = nombre
        self.edad = edad
        
    def saludar(self):
        print("Hola, soy un metodo de ejemplo")
    
    def devolveratributos(self):
        return self.nombre, str(self.edad)  # Paso a string
    
