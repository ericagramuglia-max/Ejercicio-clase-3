"""Determinar si una persona puede acceder a un descuento para estudiantes
bajo las dos condiciones de La persona debe tener menos de 25 años y debe ser estudiante"""


edad = int(input("Ingrese la edad:  "))
estudiante = input ("¿Es estudiante?, Ingrese si/no:   ")

if edad < 25 and estudiante == "si" :
    print ("Usted tiene un descuento para estudiantes")

elif edad <25 or estudiante == "si": 
    print ("Usted tiene un beneficio parcial")

else:
    print("Usted no accede al descuento")

