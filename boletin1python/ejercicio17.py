#Crea una clase base llamada FiguraGeometrica con atributos ancho y altura, 
#y un método area que calcule el área de la figura. 

#Luego, crea clases derivadas como Rectangulo y Triangulo que 
#hereden de FiguraGeometrica y sobrescriban el método area
#para calcular el área específica de cada figura.

from FiguraGeometrica import *

figura1 = FiguraGeometrica(30,20)


rectangulo1 = Rectangulo(50,20)
print(rectangulo1.area())


triangulo1 = Triangulo(10,20)
print(triangulo1.area())
