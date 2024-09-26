class Rectangulo:
    
    
#Crea una clase llamada Rectangulo con atributos ancho y altura. 
#Agrega un método para calcular el área del rectángulo 
#y otro para calcular su perímetro. 

    def __init__(self, ancho="", altura=""):
        self.ancho = ancho
        self.altura = altura
    
    def area(self):
        area = self.ancho * self.altura
        return area
        
    #P = 2 l + 2 w
    def perimetro(self):
        perimetro = (self.ancho * 2) + (self.altura * 2)
        return perimetro


        