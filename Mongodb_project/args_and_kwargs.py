def one(*args):
    print args
    
one()
one(1, 2, 3)

def two(x, y, *args):
    print x, y , args
    
two('a', 'b', 'c')

def add(x, y):
    return x + y
lst = [1, 2]

print add(*lst)

# Things get only slightly more complicated when we introduce ** which does for dictionaries & key/value pairs exactly 
# what * does for iterables and positional parameters. Simple, right?
def foo(**kwargs):
    print kwargs
    
foo()

foo(x=1, y=2)
dct = {'x':1, 'y':2}
print add(**dct)  # keyword arguments

