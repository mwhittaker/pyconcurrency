import threading
import time
from thread_guard import thread_guard

def hello(name="world"):
    time.sleep(1)
    print "hello, {}!".format(name)

with thread_guard(threading.Thread(target=hello)):
    print "hi"
 
print "bye"
