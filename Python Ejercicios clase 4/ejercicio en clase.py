"""Ejercicio N°1
 
Verificación de edad para ver una película
 
Supongamos que estás desarrollando un programa para un cine y deseas
asegurarte de que los espectadores sean lo suficientemente mayores para
ver una película clasificada como PG-13.
 
Debes solicitar la edad del espectador y permitir el acceso solo si
tienen al menos 13 años."""
 
print("===Clasificación PG-13===")    
edad = int(input("Ingrese la edad: "))
 
if edad >= 13 and edad <=100:
    print("Podés ver la peli.")

elif edad >= 1 and edad <= 12:
    print("No podés ver la peli.")
    
else:
    print("Edad inválida.")