# Snake!

You've played [Snake][1] before, right?  Let's learn how to make Snake
for ourselves!

[1]: http://en.wikipedia.org/wiki/Snake_(video_game)

# Setup

1. Make sure you've followed the instructions on how to install
Python.
2. Go to [https://github.com/ruggeri/snake3][2] to download the zip
file containing the project materials.  Extract the zip.
3. In Terminal.app, run the `configure` script to install the Tornado
web server:

    ~/projects/snake3$ ./configure
    Creating /Users/edwardruggeri/projects/snake3/lib/site.py
    Searching for tornado
    Reading http://pypi.python.org/simple/tornado/
    Reading http://www.tornadoweb.org/
    Best match: tornado 2.2.1
    ...

4. Go ahead and launch the snake program with the `run` script:

    ~/projects/snake3$ ./run
    Server started.

5. Open `snake.html` in Chrome; you should see just a single
"H" in the middle of the screen.  This is your snake!

6. Finally, open `snake.py` in your editor; this is where we'll write
your Python code!  Here's what it looks like now:

    from canvas import *
    from snake_lib import *
    
    #### YOUR CODE GOES HERE:
    
    snake = Snake((WIDTH / 2, HEIGHT / 2))
    def move(direction):
        draw(snake)

[2]: https://github.com/ruggeri/snake3
