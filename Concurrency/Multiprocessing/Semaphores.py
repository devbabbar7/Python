import time
import random
import math
from multiprocessing import Process, Semaphore

def worker(sem, idx):
    print(f'{idx} waiting for response.')
    with sem:
        print(f"Worker {idx} entered critical section ({sem})")
        time.sleep(random.uniform(1,3))
        print(f"Worker {idx} leaving critical section ({sem})")
    print(f"Worker {idx} done.")

if __name__ == '__main__':
    sem = Semaphore(2)
    procs = [Process(target=worker, args=(sem, i)) for i in range(4)]
    for p in procs:
        p.start()
    for p in procs:
        p.join()