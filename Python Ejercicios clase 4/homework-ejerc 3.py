"""Ejercicio N°3
 
Calculadora de descuento
 
Ahora debes generar un programa que calcule el descuento de un producto, se le solicita
al usuario ingresar el precio original de un producto. Luego, calcula y muestra el precio final
después del descuento.
 
Tener en cuenta lo siguiente:
Si se ingresa un precio de producto mayor o igual a $12.999 entonces se realizará el descuento del 30%,
Sino, se realizará el descuento del 20% sobre el total del producto."""

precio_original = float(input("Ingrese un precio: "))

if precio_original >= 12000:
    descuento = precio_original * 0.30
    print (f"descuento obtenido según descuento del 30% es: {descuento}")
    print (f"el precio final es: {precio_original - descuento}")
else:    
    descuento = precio_original * 0.20
    print (f"descuento obtenido según descuento del 30% es: {descuento}")
    print (f"el precio final es: {precio_original - descuento}")

    #print(f" Descuento obtenido: {descuento}\n precio final con el descuento aplicado: {precio_original-descuento}")