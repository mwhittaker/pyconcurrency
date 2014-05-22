import threading
import async
import future
import time

def square(i):
    time.sleep(i / 2)
    return i**2

xs = range(10)
print sum([fut.get() for fut in [async.async(square, x) for x in xs]])
print sum([x**2 for x in xs])
