import threading
import async
import future
import time

def double_wait(i):
    time.sleep(1)
    return i * 2

fut = async.async(double_wait, 21)
print fut.get()
