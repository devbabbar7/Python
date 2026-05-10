import time
import math
from multiprocessing import Pool

if __name__ == '__main__':
    start = time.perf_counter()
    results1 = [math.factorial(i) for i in range(10000)]
    end = time.perf_counter() - start
    print(end) # 8.46457449999798
    start = time.perf_counter()
    pool = Pool()
    results2 = pool.map(math.factorial, range(10000))
    end = time.perf_counter() - start
    print(end) # 2.1515081000034115
    print(all(x == y for x, y in zip(results1, results2))) # True
