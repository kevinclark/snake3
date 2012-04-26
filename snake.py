from canvas import *
from random import *
from snake_lib import *

#### YOUR CODE GOES HERE:

def move(direction):
    for i in range(100):
        x = randint(0, WIDTH)
        y = randint(0, HEIGHT)
        put_char((x,y), "X")
