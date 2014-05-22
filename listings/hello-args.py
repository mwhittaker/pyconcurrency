import threading

def hello(name="world"):
    print "hello, {}!".format(name)

threads = [threading.Thread(target=hello, args=(`i`,)) for i in range(10)]
map(lambda t: t.start(), threads)
map(lambda t: t.join(), threads)
