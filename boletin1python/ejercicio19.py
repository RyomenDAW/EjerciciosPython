#Crea una clase base llamada InstrumentoMusical con un método tocar que imprima un mensaje genérico. Luego,
# crea clases derivadas como Piano y Guitarra que hereden de InstrumentoMusical y sobrescriban el método tocar 
# para imprimir mensajes diferentes.


from instrumentomusical import *

instrumento1 = InstrumentoMusical("Viento")

piano1 = Piano("Negro")
guitarra1 = Guitarra("400")


print(piano1.tocar())
print(guitarra1.tocar())