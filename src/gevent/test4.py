import time
import gevent
from gevent import select

start = time.time()
tic = lambda: 'at %1.1f seconds' % (time.time() - start)

#select() 函数通常是一个阻塞调用，它轮询各种文件描述符

def gr1():
    # Busy waits for a second, but we don't want to stick around...
    print('Started gr1 Polling: %s' % tic())
    select.select([], [], [], 2)                 
    # 可以理解成一个 IO 阻塞的操作，阻塞了2秒，这时 Greenlet 会自动切换到 gr2() 上下文执行 
    print('Ended gr1 Polling: %s' % tic())

def gr2():
    # Busy waits for a second, but we don't want to stick around...
    print('Started gr2 Polling: %s' % tic())
    select.select([], [], [], 2)
    print('Ended gr2 Polling: %s' % tic())

def gr3():
    print("Hey lets do some stuff while the greenlets poll, %s" % tic())
    gevent.sleep(1)
    # 让当前 Greenlet 休眠1秒，上面 gr1() gr2() 阻塞操作完成后，再切换到 gr1() gr2() 的上下文执行
    print('Ended gr3 Polling: %s' % tic())

gevent.joinall([
    gevent.spawn(gr1),
    gevent.spawn(gr2),
    gevent.spawn(gr3),
])
