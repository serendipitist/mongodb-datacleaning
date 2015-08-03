def logger(func):
    def inner(*args, **kwargs):
        print "Arguments were: %s,%s" % (args, kwargs)
        return func(*args, **kwargs)
    return inner
@logger
def foo1(x, y=1):
    return x * y
@logger
def foo2():
    return 2

foo1(5, 4)

# http://www.artima.com/weblogs/viewpost.jsp?thread=240808
# you will understand decorators
