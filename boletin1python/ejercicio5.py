#Calcula el factorial de un número.

print("Dime un numero")
num = input()
factorial = 1
for num in range (int(num), 1, -1):
    factorial = int(num) * int(factorial)
    
print("El factorial es "+str(factorial))