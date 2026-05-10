import time
import math
from multiprocessing import Process, Lock, Value

def worker(lock, counter):
    for i in range(100000):
        with lock:
            counter.value += 1

if __name__ == '__main__':
    lock = Lock()
    counter = Value('i', 0) # Shared, synchronized integer
    procs = [Process(target=worker, args=(lock, counter)) for i in range(10)]
    for p in procs:
        p.start()
    for p in procs:
        p.join()
    print(counter.value)

# Output
# 1000000