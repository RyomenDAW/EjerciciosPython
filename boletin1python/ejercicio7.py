#Calcula el máximo común divisor (MCD) de dos números. 


print("Dime el primer numero")
num1 = input()
print("Dime el segundo numero")
num2 = input()

divisor = 0
if num1 >= num2:
    divisor = num1
else:
    divisor = num2

maxcomundivisor = 0
for divisor in range (int(divisor), 1, -1):
    if int(num1) % divisor == 0 and int(num2) % divisor == 0:
        if divisor > maxcomundivisor:
            maxcomundivisor = divisor
            print("Maximo Comun Divisor es " +str(divisor))
