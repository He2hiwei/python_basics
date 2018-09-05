import threading
from queue import Queue
import copy
import time

def job(l,q):
    res = sum(l)
    q.put(res)
