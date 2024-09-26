##Crea una clase base llamada FiguraGeometrica con atributos ancho y altura, 
#y un método area que calcule el área de la figura. 

#Luego, crea clases derivadas como Rectangulo y Triangulo que 
#hereden de FiguraGeometrica y sobrescriban el método area
#para calcular el área específica de cada figura.

class FiguraGeometrica:
    
        def __init__(self, ancho="",altura=""):
            self.ancho = ancho
            self.altura = altura
            
        def area (self):
            area = self.ancho * self.altura
            return area
        
class Rectangulo(FiguraGeometrica):
        def area (self):
            area = self.ancho * self.altura
            return area
        
class Triangulo(FiguraGeometrica):
        def area (self):
            area = self.ancho * (self.altura / 2)
            return area