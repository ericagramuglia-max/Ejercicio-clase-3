"""Situación: Ingresar una nota del 0 al 10 y mostrar si el estudiante está:"""

nota = int(input("Ingrese una nota del 0 al 10: "))
if nota >= 0 and nota <=5: 
    print ("DESAPROBADO") #condicion verdadera
elif nota >= 6 and nota <=8:
    print ("APROBADO")
else:
    print ("SOBRESALIENTE") #condicion falsa segunda condición


