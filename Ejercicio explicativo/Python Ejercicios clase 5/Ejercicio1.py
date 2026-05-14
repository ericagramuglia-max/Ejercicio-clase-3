"""total = 0

precio = float(input("Ingrese el precio de la golosina que sea comprar (0 para terminar): "))

while precio > 0:            #"""precio !=0:  tambien resta numeros o se puede ingresar num negativos"""
    total = total + precio
    precio = float(input("Ingrese el precio de la golosina que sea comprar (0 para terminar): "))

print ("El total a pagar es: ", total) 
"""


"""🛒 Ejercicio 1: Compras en el kiosco
Problema:  
Un cliente quiere comprar golosinas.
El programa debe pedir el precio de cada producto.
Se van sumando los precios hasta que el cliente ingrese 0 (no compra más).
Al final se muestra el total a pagar."""
 
total = 0
 
while True:
    precio = float(input("Ingrese el precio de la golosina que desea comprar('0 para terminar'): "))
    if precio == 0:
        break
    total = total + precio
   
print(f"El precio total es: ${total}")  
 