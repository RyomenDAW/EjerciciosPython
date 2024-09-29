#Crea una clase base llamada Vehiculo con atributos marca y modelo,
# y un método informacion que imprima la información del vehículo. 
# Luego, crea clases derivadas como Coche y Bicicleta que hereden 
# de Vehiculo y añadan atributos y métodos específicos de cada tipo de vehículo.

from vehiculo import *

vehiculo1 = Vehiculo("Toyota","300")

coche1 = Coche("500","5")
bicicleta1 = Bicicleta("Montaña","9")


print(coche1.acelerar())
print(bicicleta1.pedalear())