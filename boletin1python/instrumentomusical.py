#Crea una clase base llamada InstrumentoMusical con un método tocar que imprima un mensaje genérico. Luego,
# crea clases derivadas como Piano y Guitarra que hereden de InstrumentoMusical y sobrescriban el método tocar 
# para imprimir mensajes diferentes.

class InstrumentoMusical:
    
    def __init__(self, tipo=""):
        self.tipo = tipo

    def tocar(self):
        print("No se que tocar, que soy?")
        
        
class Piano(InstrumentoMusical):
        
        def __init__(self, color=""):
            self.color = color
            
        def tocar(self):
            print("Octava tras octava")


class Guitarra(InstrumentoMusical):
        
        def __init__(self, vatios=""):
            self.vatios = vatios
            
        def tocar(self):
            print("In the End pero a guitarra electrica")