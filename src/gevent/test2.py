from greenlet import greenlet
def test1(x, y):
    print (id(greenlet.getcurrent()), id(greenlet.getcurrent().parent))
    z = gr2.switch(x+y)
    print(z)

def test2(u):
    print (id(greenlet.getcurrent()), id(greenlet.getcurrent().parent))
    print(u)
    gr1.switch(42)

gr1 = greenlet(test1)
gr2 = greenlet(test2)
print (id(greenlet.getcurrent()), id(gr1), id(gr2))
gr1.switch("hello", " world")