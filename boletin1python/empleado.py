#Crea una clase base llamada Empleado con atributos nombre y salario, y un 
# método calcular_salario_anual que calcule el salario anual del empleado.
# Luego, crea clases derivadas como Gerente y Programador que hereden de Empleado y
# añadan atributos y métodos específicos de cada tipo de empleado.

class Empleado:
    def __init__ (self, nombre="", salario=0):
        self.nombre = nombre
        self.salario = salario
        
    def calcular_salario_anual (self):
        salarioanual = self.salario * 12
        return salarioanual
    
class Gerente(Empleado):
    def __init__ (self, puestogerente=""):
        self.puestogerente = puestogerente
        
    def reunion(self):
        llamadareunion = "A las 10:00 en Meet compis"
        return llamadareunion   

class Programador(Empleado):
    def __init__ (self, lenguaje=""):
        self.lenguaje = lenguaje
        
    def proyecto(self):
        startup = "He iniciado un proyecto nuevo"
        return startup