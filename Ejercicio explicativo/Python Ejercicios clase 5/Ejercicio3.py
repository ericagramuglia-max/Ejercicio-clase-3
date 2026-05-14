"""🎮 Ejercicio 3: Vida de un personaje en un videojuego
Problema:  
Un personaje empieza con 100 puntos de vida.
El programa debe pedir cuánto daño recibe en cada ataque.
Restar ese daño a la vida.
El ciclo continúa mientras la vida sea mayor que 0.
Al terminar, mostrar "Game Over"."""
 
 
life = 100
 
 
 
while life > 0:
    damage = int(input("Daño recibido(vida inicial: 100): "))
    life = life - damage
    print(f"Vida restante: {life}")
 
   
print("Game Over")  