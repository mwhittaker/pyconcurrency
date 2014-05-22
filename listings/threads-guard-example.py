import threading
import time
from thread_guard import threads_guard

def hello(name="world"):
    time.sleep(1)
    print "hello, {}!".format(name)

threads = [threading.Thread(target=hello, args=(`i`,)) for i in range(5)]
with threads_guard(threads):
    print "hi"
 
print "bye"
