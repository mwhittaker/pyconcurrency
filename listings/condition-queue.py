import threading as th
import thread_guard as tg
import time

queue      = []
queue_lock = th.Lock()
queue_cv   = th.Condition(queue_lock)

def pusher():
    for i in range(10):
        time.sleep(1)
        with queue_cv:
            queue.append(i)
            queue_cv.notify()

def popper():
    for i in range(10):
        with queue_cv:
            while (len(queue) == 0):
                queue_cv.wait()
            print queue.pop()

threads = [th.Thread(target=pusher), th.Thread(target=popper)]
with tg.threads_guard(threads):
    pass
