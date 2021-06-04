import gevent
'''
（1）spawn(function, *args, **kwargs) # → Greenlet
创建一个新的Greenlet对象，安排它运行函数funtion(*args, **kwargs)。

（2）joinall(greenlets, timeout=None, raise_error=False, count=None)等待greenlets结束。
参数：greenlets -- 一系列greenlets去等待。
timeout -- 如果给出，最大的等待秒数
返回： 在timeout结束前一系列已经结束的greenlets。
'''

def foo():
    print('Running in foo')
    gevent.sleep(0)
    print('Explicit context switch to foo again')

def bar():
    print('Explicit context to bar')
    gevent.sleep(0)
    print('Implicit context switch back to bar')

# gevent.joinall([
#     gevent.spawn(foo),
#     gevent.spawn(bar),
# ])

gevent.spawn(foo)
gevent.spawn(bar)
gevent.get_hub().join()
