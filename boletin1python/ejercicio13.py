#clase estudiante

from estudiante import *


estudiante1 = estudiante("David","20","2DAW")
estudiante2 = estudiante("Juan","25","2DAM")
estudiante3 = estudiante("Kazan","18","2ASIR")
estudiante4 = estudiante("Maria","22","2SMR")

lista = [estudiante1, estudiante2, estudiante3, estudiante4]
for i in lista:
    print(i.devolveratributos())

