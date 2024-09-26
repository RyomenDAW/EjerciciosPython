

class estudiante:

#Crea una clase llamada Estudiante con atributos nombre, edad y curso. 
#Crea varios objetos de tipo Estudiante y almacénalos en una lista. 
#Luego, itera sobre la lista e imprime la información de cada estudiante.  
    
    def __init__(self, nombre="",edad="",curso=""):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso
        
    def devolveratributos(self):
        return self.nombre, str(self.edad), self.curso
