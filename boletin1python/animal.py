class Animal:
    
#Crea una clase base llamada Animal con un método hablar que imprima un mensaje genérico.
#Luego, crea dos clases derivadas, Perro y Gato, que hereden de Animal y 
#sobrescriban el método hablar para imprimir mensajes diferentes. 

    def __init__(self, nombre=""):
        self.nombre = nombre
    
    def hablar(self):
        return ("Un mensaje sin mucha importancia")
        
        
class Gato(Animal):
        def hablar(self):
            return("Maullido")
            
class Perro(Animal):
        def hablar(self):
            return("Ladrido")