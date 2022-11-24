# Objetivos
Crear un juego pong básico: 2 raquetas, una bola, puntuaciones.

## Aspectos importantes
- Se trata de crear el juego con objetos e ir utilizando la documentación para aprender pygame.
- El problema de las puntuaciones, como comunicar un objeto con otros
- La necesidad de un controlador (el juego, ya sea clase o secuencial) -> Tratamos de la clase
- Ordenación del código, importacion de ficheros (entities.py)
- Una vez hecho con dibujos de pg.draw, usar imágenes
- Crear animaciones, con la raqueta
- Crear animaciones 2, con la bola

## Cajon de sastre
Una vez tenemos la bola rebotando por dentro de los límites, y la raqueta que se sale de la pantalla tenemos que resolver dos cosas:
    - como informar a la raqueta y la bola de los límites de la pantalla
        - solución constantes del juego
        - solución informar a la instancia en el __init__ 
A este nivel me decanto por las constantes del juego

Cuando creamos las dos raquetas tenemos que usar teclas distintas. ¿Como solucionarlo? -> crear atributos teclas arriba y abajo, puede ser una, o ver otras.