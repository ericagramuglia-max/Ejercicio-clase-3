"""Situación: Ingresar tres números y mostrar cuál es el mayor de los tres."""

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

if num1 > num2 and num1 > num3 :
    input("El número 1 es mayor")

elif num2 > num1 and num2 > num3:
    input("El número 2 es mayor")
    
else:
    input("El número 3 es mayor")