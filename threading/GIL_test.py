import threading
from queue import Queue
import copy
import time

def job(l,q):
    res = sum(l)
    q.put(res)

def multithreading(l):
    q = Queue()
    threds = []

    for i in range(4):
        t = threading.Thread(target=job,args=(l,q))
        t.start()
        threds.append(t)
    [t.join() for t in threds]
    total = 0
    for _ in range(4):
        total += q.get()
    print(total)

def normal(l):
    total = sum(l)
    print(total)
    
if __name__ == '__main__':
    l = list(range(1000000))
    s_t = time.time()
    normal(l*4)
    print('normal:',time.time()-s_t)
    s_t = time.time()
    multithreading(l)
    print('multithreading: ',time.time()-s_t)

"""
output:
1999998000000
normal: 0.08509016036987305
1999998000000
multithreading:  0.03632998466491699
"""
