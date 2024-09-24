#Hacer el ejemplo con un programa de calculadora basica

print("Indique el primer numero")
num1 = input()
print("Indique el segundo numero")
num2 = input()

def sumar (num1, num2):
    suma = int(num1) + int(num2)
    return suma

def resta (num1, num2):
    resta = int(num1) - int(num2)
    return resta

def multiplicar (num1, num2):
    multiplicar = int(num1) * int(num2)
    return multiplicar

def division (num1, num2):
    division = int(num1) / int(num2)
    return division

print("")
print("Primero haremos la suma")
res1 = sumar(num1, num2)
print("El resultado de la suma es " +str(res1))
print("")

print("Luego haremos la resta")
res2 = resta(num1, num2)
print("El resultado de la resta es " +str(res2))
print("")

print("Despues haremos la multiplicacion")
res3 = multiplicar(num1, num2)
print("El resultado de la multiplicacion es " +str(res3))
print("")

print("Finalmente haremos la division")
res4 = division(num1, num2)
print("El resultado de la multiplicacion es " +str(res4))
print("")