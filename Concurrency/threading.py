import threading
import time

done = False

def worker(initialize):
    counter = initialize
    while True:
        time.sleep(1)
        counter += 1
        print(counter)

# daemon = True means function(child process) execution will stop when main file(Parent Process) finishes execution.
threading.Thread(target=worker, daemon=True, args=(0,)).start()
# Daemon=True basically means this thread shouldn't keep the program alive.
# If any one thread has daemon set to False, then all other threads will continue to execute normally until the daemon=False stops executing.
threading.Thread(target=worker, daemon=True, args=(1000,)).start()

# Same thing as above.
t1 = threading.Thread(target=worker, daemon=True, args=(0,))
t2 = threading.Thread(target=worker, daemon=True, args=(1000,))
t1.start()
t2.start()
# Join waits for thread execution to complete before proceeding.
t1.join()
t2.join()
input("Press Enter to quit.")
done = True