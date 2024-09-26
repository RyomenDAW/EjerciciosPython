#Crea una clase llamada CuentaBancaria con atributos titular y saldo. 
#Agrega métodos para depositar y retirar dinero de la cuenta.  

from cuentabancaria import * 

cuenta1 = CuentaBancaria("Kazan","1000")

print(cuenta1.devolveratributos())
print(cuenta1.depositar(1000))
print(cuenta1.devolveratributos())
print(cuenta1.retirar(500))
print(cuenta1.devolveratributos())
