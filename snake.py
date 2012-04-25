from canvas import *
from snake_lib import *

#### YOUR CODE GOES HERE:

def move(direction):
    hello_list = ['H', 'E', 'L', 'L', 'O', '!']

    x = 5
    y = 5
    for letter in hello_list:
        put_char((x,y), letter)
        x = x + 1
