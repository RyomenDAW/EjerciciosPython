#Crea una clase llamada CuentaBancaria con atributos titular y saldo. 
#Agrega métodos para depositar y retirar dinero de la cuenta.  

class CuentaBancaria:
    
    
    def __init__ (self, titular="",saldo=0):
        self.titular = titular
        self.saldo = float(saldo)      
        
    def devolveratributos(self):
        return self.titular, str(self.saldo)
    
    
    def retirar(self, cantidad):
        if self.saldo >= cantidad:
            nuevo_saldo = self.saldo - cantidad 
            self.saldo = nuevo_saldo  
            print("Se han retirado " +str(cantidad)+ " euros")
        else:
            print("Dinero insuficiente, no se ha podido realizar")
        
    def depositar(self, cantidad):
        nuevo_saldo = self.saldo + cantidad  # Calcular el nuevo saldo sumando la cantidad
        self.saldo = nuevo_saldo  
        print("Se han ingresado "+ str(cantidad)+ " euros")