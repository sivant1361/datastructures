import time
def test1():
    s=time.time()
    l = []
    for i in range(10000):
        l = l + [i]
    e=time.time()
    print("%d"%(e-s))

def test2():
    s=time.time()
    l = []
    for i in range(10000):
        l.append(i)
    e=time.time()
    print("%d"%(e-s))

def test3():
    s=time.time()
    l = [i for i in range(10000)]
    e=time.time()
    print("%d"%(e-s))

def test4():
    s=time.time()
    l = list(range(10000))
    e=time.time()
    print("%d"%(e-s))

test1()
test2()
test3()
test4()