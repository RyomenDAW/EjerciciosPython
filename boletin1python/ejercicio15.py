#Crea una clase llamada Coche con atributos marca y modelo. 
# Crea un método que imprima la información del coche en un formato legible. 

from coche import *



coche1 = coche("Citroen","V500")
coche2 = coche("Mercedes","C")
coche3 = coche("Fiat","Tipo")

print(coche1.devolveratributos())
print(coche2.devolveratributos())
print(coche3.devolveratributos())