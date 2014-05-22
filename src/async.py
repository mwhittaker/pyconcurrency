import threading
import future

def async(f, *args, **kwargs):
    fut = future.future()

    def closure():
        fut._set(f(*args, **kwargs))
    
    t = threading.Thread(target=closure)
    t.start()

    return fut
