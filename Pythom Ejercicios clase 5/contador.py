"""#incrementador 

contador = 0

while contador <=10:
    print (contador)
    contador = contador + 1
    # print (contador) (muestra en pantalla 11 porque primera llega a 10 y luego suma 1 mas y llega a 11)
print ("fin de conrtador")

#decrementador
while contador >=0:
    print (contador)
    contador = contador - 1
print ("fin de contador")

contador = 1

while True:
    print("contador es: ", contador)
    contador = contador + 1
    if contador > 5:
        break


# sólo while
password = input("Ingrese una contraseña: ")

while password != "1234":
    print("contraseña incorrecta. Intenta nuevamente")
    password = input("Ingrese una contraseña: ")

print ("acceso correcto")

"""

while True:
    password = input("Ingrese una contraseña: ")
    if password == "1234":
       break 
    print("contraseña incorrecta. Intenta nuevamente.")
print ("acceso correcto")

