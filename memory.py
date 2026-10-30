"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *
from turtle import *

from freegames import path

car = path('car.gif')
tiles = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] * 2
state = {'mark': None, 'taps': 0, 'win': False}
hide = [True] * 16


def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 100) // 50 + ((y + 100) // 50) * 4)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 4) * 50 - 100, (count // 4) * 50 - 100


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    if x < -100 or x > 100 or y < -100 or  y > 100:
        return

    spot = index(x, y)

    if spot < 0 or spot >= len(tiles):
        return

    state['taps'] += 1
    print(f"Cantidad de clics ocurridos: {state['taps']}")

    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:    
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

        # Ejercicio3 detectar si todas las fichas fueron reveladas
        if all(not h for h in hide):
            state ['win'] = True
        


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(16):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 10, y + 5)
        color('black')
        write(tiles[mark], font=('Arial', 24, 'normal'))

# Ejercicio 3: Mostrar mensaje de victoria en pantalla si ya ganaron
    if state.get('win', False):
        up()
        goto(0, 0)
        color('blue')
        write("¡GANASTE!", align="center", font=('Arial', 30, 'bold'))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
draw()
onscreenclick(tap)
done()
