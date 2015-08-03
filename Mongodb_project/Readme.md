requires understanding several functional programming concepts as well as feeling 
comfortable with some unique features of Python’s function definition and function 
calling syntax. 
*Using* decorators is easy (see Section 10)! But writing them can be complicated.

I can't make decorators easy - but maybe by walking through 

A decorator is just a callable that takes a function as an argument and returns a replacement function. 
We’ll start simply and work our way up to useful decorators.


"""
It’s a matter of opinion as to whether doing it this makes our code cleaner: isolating the bounds checking in its
 own function and applying it to all the functions we care to by wrapping them with a decorator. 
 The alternative would be a function call on each input argument and on the resulting output before returning inside each math
  function and it is undeniable that using the decorator is at least less repetitious in terms of the amount of code needed 
to apply bounds checking to a function. In fact - if its our own functions we’re decorating 
we could make the decorator application a little more obvious.
"""

*args and **kwargs
We’ve written a useful decorator but it’s hard coded to work only on a
 particular kind of function - one which takes two arguments. 
 Our inner function checker accepts two arguments and passes the arguments
  on to the function captured in the closure. What if we wanted a decorator
  that did something for any possible function? Let’s write a decorator that increments a counter for every function call of every decorated function without changing any of it’s decorated functions. This means it would have to accept the calling signature of any of the functions that it decorates and also call the functions
 it decorates passing on whatever arguments were passed to it.