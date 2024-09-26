#Crea una clase llamada Persona con atributos nombre y edad. 
# Luego, crea un objeto de tipo Persona e imprime sus atributos.

from persona import *

persona1 = Persona("Juan","24")
persona2 = Persona("Eva","19")

print(persona1.devolveratributos())
print(persona2.devolveratributos())