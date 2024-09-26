#Crea una clase base llamada Animal con un método hablar que imprima un mensaje genérico.
#Luego, crea dos clases derivadas, Perro y Gato, que hereden de Animal y 
#sobrescriban el método hablar para imprimir mensajes diferentes. 

from animal import *

animal1= Animal("Juan")
gato1= Gato("Gato1")
perro1 = Perro("Perro1")


print(animal1.hablar())
print(gato1.hablar())
print(perro1.hablar())