import threading as th
import thread_guard as tg
import time

event = th.Event()

def waiter(name):
    event.wait()
    print name

def setter():
    print "sleeping"
    time.sleep(5)
    print "setting"
    event.set()

waiters = [th.Thread(target=waiter, args=(name,)) for name in "ABCDEF"]
setter  = th.Thread(target=setter)
with tg.threads_guard(waiters + [setter]):
    pass
