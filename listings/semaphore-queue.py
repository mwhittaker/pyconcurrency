import threading as th
import thread_guard as tg
import time

queue      = []
queue_sem  = th.Semaphore(0)

def pusher():
    for i in range(10):
        time.sleep(1)
        queue.append(i)
        queue_sem.release()

def popper():
    for i in range(10):
        queue_sem.acquire()
        print queue.pop()

threads = [th.Thread(target=pusher), th.Thread(target=popper)]
with tg.threads_guard(threads):
    pass
