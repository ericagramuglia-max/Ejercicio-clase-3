"""Ejercicio N°4
 
Validar dias de la semana
 
Crea un programa que pida al usuario ingresar un número del 1 al 7 y muestre el día de
la semana correspondiente. Si ingresa un número fuera de ese rango, mostrar el siguiente
mensaje de error: "Número de día incorrecto"."""

numero = input("Ingrese un númuro del 1 al 7: ").lower()  # ingresa un string con mayúsculas y minusculas y lo pasa todo a minúsculas
                                             #.oper() pasa todo el string a mayúscula
                                             # .capitalice() primera mayúscula y el resto en minúscula       
if numero == 1 or "domingo":
    print("DOMINGO")

elif numero == 2 or "lunes": 
    print("LUNES")

elif numero == 3 or "martes":
    print("MARTES")

elif numero == 4 or "miércoles":
    print("MIÉRCOLES")

elif numero == 5 or "jueves":
    print("JUEVES")

elif numero == 6 or "viernes":
    print("VIERNES")

elif numero == 7 or "sábado":
    print("SÁBADO")

else: print("Número de día incorrecto")
