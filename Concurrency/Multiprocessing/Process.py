import time
import math
from multiprocessing import Process

def watchdog(interval = 5):
    while True:
        print(f"[{time.strftime('%X')}] heartbeat")
        time.sleep(interval)

if __name__ == '__main__':
    # Process() creates a new process independent of the main class execution
    # daemon = True, if parent process is terminated, child process also gets terminated.
    p = Process(target=watchdog, args=(5,), daemon=True) # Child process
    p.start()
    result = [math.factorial(i) for i in range(10000)] # Parent process
    print('Main work done, exiting.')

'''
Output:
[16:58:51] heartbeat
[16:58:56] heartbeat
Main work done, exiting.
'''