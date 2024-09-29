#Crea una clase base llamada Empleado con atributos nombre y salario, y un 
# método calcular_salario_anual que calcule el salario anual del empleado.
# Luego, crea clases derivadas como Gerente y Programador que hereden de Empleado y
# añadan atributos y métodos específicos de cada tipo de empleado.

from empleado import *

empleado1 = Empleado("Juan",2000)

print (empleado1.calcular_salario_anual())

gerente1= Gerente("CEO")

print (gerente1.reunion())

programador1 = Programador("Python")

print (programador1.proyecto())