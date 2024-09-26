#Crea una lista de números (4) y calcula su promedio. 
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
num3 = float(input("Introduce el tercer número: "))
num4 = float(input("Introduce el cuarto número: "))

lista = [num1, num2, num3, num4]
promedio = sum(lista) / len(lista)

print("La media de los números es:", promedio)
