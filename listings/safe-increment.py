import threading as th
import thread_guard as tg

COUNT      = 0
COUNT_LOCK = th.Lock()

def incr():
    global COUNT
    with COUNT_LOCK:
        COUNT += 1

def increment():
    for i in range(10 * 1000):
        incr()

threads = [th.Thread(target=increment) for i in range(10)]
with tg.threads_guard(threads):
    pass

print COUNT
