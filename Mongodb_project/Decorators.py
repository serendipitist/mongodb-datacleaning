# A decorator is just a callable that takes a Function
# as an argument and returns a replacement Function
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return "coord:" + str(self.__dict__)
    
def add(a, b):
        return Coordinate(a.x + b.x, a.y + b.y)
def sub(a, b):
        return Coordinate(a.x - b.x, a.y - b.y)
    
one = Coordinate(100, 200)

two = Coordinate(300, 200)

three = Coordinate(-100, -100)


print add(one, two)    
print add(two, three)
