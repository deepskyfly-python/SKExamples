import gevent
from gevent.lock import Semaphore

sem = Semaphore(1)

def f1():
    for i in range(5):
        sem.acquire()
        print('f1 is ' + str(i))
        sem.release()
        gevent.sleep(1)

def f2():
    for i in range(5):
        sem.acquire()
        print('f2 is ' + str(i))
        sem.release()
        gevent.sleep(0.3)

t1 = gevent.spawn(f1)
t2 = gevent.spawn(f2)
gevent.joinall([t1, t2])
