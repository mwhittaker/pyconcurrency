import threading as th
import thread_guard as tg
import time

queue = []

def pusher():
    for i in range(10):
        time.sleep(1)
        queue.append(i)

def popper():
    for i in range(10):
        print queue.pop()

threads = [th.Thread(target=pusher), th.Thread(target=popper)]
with tg.threads_guard(threads):
    pass
