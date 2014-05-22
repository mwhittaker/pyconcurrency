import threading

def hello():
    print "hello, world!"

t = threading.Thread(target=hello)
t.start()
t.join()
