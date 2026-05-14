"""📚 Ejercicio 2: Préstamo de libros en la biblioteca
Problema:  
Un alumno puede retirar libros de la biblioteca.
El sistema debe pedir el título de cada libro.
El ciclo continúa hasta que el alumno escriba "fin".
Al final se muestra la cantidad de libros retirados."""
 
cantidad_libros = 0
 
libros = input("Ingrese el título del libro que desea retirar( escriba fin para terminar): ")
 
while libros.lower() != "fin":
    cantidad_libros = cantidad_libros + 1
    libros = input("Ingrese el título del libro que desea retirar( escriba fin para terminar): ")
   
print("El total de libros prestados es: ", cantidad_libros)  
 