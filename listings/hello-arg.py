import threading

def hello(name="world"):
    print "hello, {}!".format(name)

t = threading.Thread(target=hello)
t.start()
t.join()

t = threading.Thread(target=hello, args=("michael",))
t.start()
t.join()
