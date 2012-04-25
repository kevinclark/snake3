# Snake!

You've played [Snake][1] before, right?  Let's learn how to make Snake
for ourselves!

[1]: http://en.wikipedia.org/wiki/Snake_(video_game)

# Setup

First, make sure you've followed the instructions on how to install
Python.  Second, go to [https://github.com/ruggeri/snake3][2] to
download the zip file containing the project materials.  Extract the
zip.
[2]: https://github.com/ruggeri/snake3

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

The file we'll work the most with is `snake.py`.  Take a look at the
bit after `def move(direction):`.  This part prints "HELLO!".  Let's
look at this line:

    hello_list = ['H', 'E', 'L', 'L', 'O', '!']

To the right of the `=` is a *list* of items.  We can make lots of
different lists in Python:

    [0, 1, 2, 3]
    ['John', 'Paul', 'Geroge', 'Ringo']

Lists start with a `[` and end with a `]`.  Then we list each item,
separated by commas.

The `hello_list` part to the left of the `=` is a *variable* name.  By
assigning a *value* to a variable, we can use that name later on.  So

    beatles = ['John', 'Paul', 'Geroge', 'Ringo']

lets us use the name `beatles` to mean `['John', ...]` later on.

Now you try!  Open up IDLE or the Python interpreter and make a list
of your friends.  Assign the list to the variable `friends`.

## Printing and for loops

Let's say hello to your friends.  Here's how we could say hello to a
single friend:

    >>> print("Hey Joe!")
    Hey Joe!

`print` is called a *function*.  Functions do work for us; the part in
parentheses is what a function works on.  `print` takes `"Hey Joe!"`
and prints it out.

Go ahead and print some messages in IDLE or the python interpreter!

Okay, let's see how to say hello to each of my cats.

    >>> cats = ["Earl", "Breakfast", "Gizmo", "Kiki"]
    >>> for cat in cats:
    ...     print("Hello " + cat + "!")
    ...
    Hello Earl!
    Hello Breakfast!
    Hello Gizmo!
    Hello Kiki!

What all is this?  The first line defines the variable `cats` and sets
it equal to my list of cats.  Next comes `for cat in cats:`; this
tells Python to loop through each element in `cats`, each time
assigning the value to a new variable `cat`.  The last part,
`print("Hello " + cat + "!")` is called the *body*.  We run the
commands in the body for each cat in the list.  Notice that `cat` is
different every time; it's set to each of my cats in the order of the
list.

Okay!  Now you try!  Use a for loop in IDLE to greet some of your
friends!

## Back to hello_list

Let's take another look at the code in `snake.py`.

    def move(direction):
        hello_list = ['H', 'E', 'L', 'L', 'O', '!']
        
        x = 5
        y = 5
        for letter in hello_list:
            put_char((x,y), letter)
            x = x + 1

The key here is the function `put_char`.  This prints a letter, or
*character* at a specific location.  The location is a point in the
*grid*.  Here's an example of a grid:

     0 1 2 3 4 5
    0
    1
    2          Q
    3
    4    P
    5      R

This is a five-by-five grid; I've marked three points: `P`, `Q`, and
`Q`.  `P` is two columns over and four rows down; we say that it is at
position `(4, 2)`.  `Q` is 5 columns over and 2 rows down; we say its
position is `(5, 2)`.  What position is `R` at.

We can tell our program where to draw letters by giving `put_char` a
position and a letter; let's look closely at

     put_char((x,y), letter)

The first bit, `(x,y)` is the position; `x` and `y` are variables
which will represent how many columns to go over and how many rows to
go down.  `letter` is also a variable; it's the letter to print.

Try swapping `(y,x)` for `(x,y)`; what do you think will happen?

The last part of our for loop's body is `x = x + 1`.  Why don't you
try adding the line `y = y + 1`; what do you think will happen?

Go ahead and change the list so your own name is printed!

## Drawing the border

Let's draw a border for our Snake game along each of the edges.  Here,
I'll draw one side:

    def move(direction):
        for y in range(HEIGHT):
            put_char((0, y), "W")

I'm putting a "W" for "Wall".  Here's a new couple new things.
`HEIGHT` is a variable with the number of rows; there's another
variable you can use named `WIDTH` for the number of columns.

What is this `range` guy?  He's another function, and you can see
`range` is being given the `HEIGHT`.  `range(HEIGHT)` returns a list
of numbers up to `HEIGHT`:

    >>> HEIGHT
    30
    >>> range(HEIGHT)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]

When we write `for y in range(HEIGHT):`, we're saying that we should
run the body 30 times, for `y = 0`, `y = 1`, `y = 2`, for each of the
heights.

Can you add loops to print the other three borders?
