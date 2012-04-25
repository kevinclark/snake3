# Snake!

You've played [Snake][1] before, right?  Let's learn how to make Snake
for ourselves!

[1]: http://en.wikipedia.org/wiki/Snake_(video_game)

# Setup

First, make sure you've followed the instructions on how to install
Python.  Second, go to [https://github.com/ruggeri/snake3][2] to
download the zip file containing the project materials.  Extract the
zip.

Next, in Terminal.app, run the `configure` script to install the
Tornado web server:

    ~/projects/snake3$ ./configure
    Creating /Users/edwardruggeri/projects/snake3/lib/site.py
    Searching for tornado
    Reading http://pypi.python.org/simple/tornado/
    Reading http://www.tornadoweb.org/
    Best match: tornado 2.2.1
    ...

Now go ahead and launch the snake program with the `run` script:

    ~/projects/snake3$ ./run
    Server started.

Open `snake.html` in Chrome; you should see just the message "HELLO!" in the
middle of the screen.  This is your snake!

Finally, open `snake.py` in your editor; this is where we'll write
your Python code!  Here's what it looks like now:

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

# First steps



[2]: https://github.com/ruggeri/snake3
