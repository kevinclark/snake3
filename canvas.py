HEIGHT = 30
WIDTH = 80

def render_grid(grid):
    lines = []

    for y in range(HEIGHT):
        line = ""
        for x in range(WIDTH):
            if (x,y) in grid:
                line = line + grid[(x,y)]
            else:
                line = line + " "
        lines.append(line)
    return '\n'.join(lines)

class Canvas:
    def __init__(self):
        self.grid = {}

    def put_char(self, pos, char):
        self.grid[pos] = char

    def clear(self):
        self.grid = {}

    def render(self):
        return render_grid(self.grid)
