from canvas import *

UP = (0, -1)
RIGHT = (1, 0)
DOWN = (0, 1)
LEFT = (-1, 0)

KEY_TO_DIR = {
    38: UP,
    39: RIGHT,
    40: DOWN,
    37: LEFT
    }

class Snake:
    def __init__(self, position, direction = UP):
        self.head = position
        self.tail = []
        self.grow = False
        self.dir = direction

    def draw(self, canvas):
        for t in self.tail:
            canvas.put_char(t, "T")
        canvas.put_char(self.head, "H")

    def move(self):
        self.tail.insert(0, self.head)
        if not self.grow:
            self.tail.pop()

        (x, y) = self.head
        (x_off, y_off) = self.dir
        self.head = (x + x_off, y + y_off)

    def turn(self, direction):
        self.dir = direction

CANVAS = Canvas()
def put_char(pos, char):
    CANVAS.put_char(pos, char)
def draw(obj):
    obj.draw(CANVAS)

KEY_BUFFER_MAX_SIZE = 4
KEY_BUFFER = []
def m(keys, move_func):
    direction = None

    for key in keys:
        if len(KEY_BUFFER) == KEY_BUFFER_MAX_SIZE:
            break
        elif key in KEY_TO_DIR:
            KEY_BUFFER.append(key)

    if KEY_BUFFER:
        direction = KEY_TO_DIR[KEY_BUFFER.pop(0)]

    CANVAS.clear()
    move_func(direction)
    return CANVAS.render()
