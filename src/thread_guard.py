import threading

"""
Most of Python's Threading classes -- locks, condition variables, semaphores --
have context managers, but thread do not. This module implements simple
start/join context managers for single and multiple threads
"""

class thread_guard(object):
    """
    Some examples:

    ```
    import threading
    import thread_guard
    import time

    def hello():
        time.sleep(1)
        print "hello, world!"

    with thread_guard.thread_guard(threading.Thread(target=hello)):
        print "thread is running!"
    ```
    """
    def __init__(self, thread):
        self.thread_ = thread

    def __enter__(self):
        self.thread_.start()
        return self.thread_
    
    def __exit__(self, type, value, traceback):
        self.thread_.join()

class threads_guard(object):
    """
    Some examples:

    ```
    import threading
    import thread_guard
    import time

    def hello(name):
        time.sleep(1)
        print "hello, {}!".format(name)

    threads = [threading.Thread(target=hello, args=(name,)) for name in "ABC"] 
    with thread_guard.threads_guard(threads):
        print "threads are running!"
    ```
    """
    def __init__(self, threads):
        self.threads_ = threads

    def __enter__(self):
        map(lambda t: t.start(), self.threads_)
        return self.threads_
    
    def __exit__(self, type, value, traceback):
        map(lambda t: t.join(), self.threads_)
