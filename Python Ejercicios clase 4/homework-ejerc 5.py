"""Ejercicio N°5
 
El mayor de tres números
 
Crea un programa que solicite al usuario ingresar tres números y determine
cuál es el mayor de los tres, luego informa al usuario con un mensaje cual es el número mayor."""

num1=int(input ("Ingrese el primer número "))
num2=int(input ("Ingrese el segundo número "))
num3=int(input ("Ingrese el tercero número 1"))

if num1 > num2 and num1 > num3:
    print (f"{num1} es el mayor.")
elif num2 > num1 and num2 > num3:
    print (f"{num2} es el mayor.")
else:
    print (f"{num3} es el mayor.")