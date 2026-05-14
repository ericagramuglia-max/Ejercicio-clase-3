"""Ejercicio N°2
 
Calificación de un estudiante
 
Imagina que eres un profesor y deseas calcular las calificaciones finales de
tus estudiantes en función de sus puntajes en un examen.  La calificación final se
asignará de la siguiente manera:
 
Si el puntaje…
 
Es mayor o igual a 90, la calificación es "A".
Está entre 80 y 89, la calificación es "B".
Está entre 70 y 79, la calificación es "C".
Está entre 60 y 69, la calificación es "D".
Es menor que 60, la calificación es "F"."""

Nota = int(input("Ingresa una nota del  al 100"))

if Nota >=90 and Nota <=100:
    print("La calificación es A")

elif Nota >=80 and Nota <=89:
    print ("La calificación es B")

elif Nota >=70 and Nota <=79:
    print ("La calificación es C")

elif Nota >=60 and Nota <=69:
    print ("La calificación es D")

elif Nota <60:  
    print ("La calificación es F")

else:
    print("Número inválido")
