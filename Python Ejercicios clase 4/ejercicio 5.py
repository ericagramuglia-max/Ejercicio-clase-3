edad = int(input("Ingrese su edad:  (del 1 al 100) "))

if edad >= 40 and edad <=100:
    print("Usted es mayor de edad y tiene un descuento.")
elif edad >=18 and edad <= 39:
    print("Usted es mayor de edad.")
elif edad >= 1 and edad <= 17:
    print("Usted es menor.")
else:
    print("Edad inválida.")
