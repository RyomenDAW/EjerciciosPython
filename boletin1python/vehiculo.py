#Crea una clase base llamada Vehiculo con atributos marca y modelo,
# y un método informacion que imprima la información del vehículo. 
# Luego, crea clases derivadas como Coche y Bicicleta que hereden 
# de Vehiculo y añadan atributos y métodos específicos de cada tipo de vehículo.


class Vehiculo:
    
    
    def __init__(self, marca="", modelo=""):
        self.marca = marca
        self.modelo = modelo
        
    def informacion(self):
        return(self.marca, self.modelo)
    
class Coche(Vehiculo):
    def __init(self, kilometraje="", espacios=""):
        self.kilometraje = kilometraje
        self.espacio = kilometraje
        
    def acelerar(self):
        print("Broom Broom Broom")
        
class Bicicleta(Vehiculo):
    def __init__(self, tipobici="", numeromarchas=""):
        self.tipobici = tipobici
        self.numarchas = numeromarchas    
        
    def pedalear(self):
        print("Pedaleo Pedaleo Pedaleo")
    