import threading

class future(object):
    def __init__(self):
        self.val_      = None
        self.val_lock_ = threading.Lock()
        self.val_event_ = threading.Event()

    def get(self):
        self.val_event_.wait()
        return self.val_

    def _set(self, val):
        with self.val_lock_:
            self.val_ = val
            self.val_event_.set()
