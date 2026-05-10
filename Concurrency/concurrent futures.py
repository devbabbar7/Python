import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed

def do_IO_work(task_id, duration = 1):
    time.sleep(duration) # Simulate an IO
    return f'Task {task_id}, completed.'

def run_threading(tasks = 5, max_workers = 5):
    results = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(do_IO_work, i, 0.1) for i in range(tasks)]
        
        for future in as_completed(futures):
            result = future.result()
            results.append(result)
    return results

def do_calculation_work(task_id, iterations = 10000000):
    i = 0
    for i in range(iterations):
        i += 1
    return f'Task {task_id}, completed.'

def run_calculation_work(tasks = 5):
    results = []
    for i in range(tasks):
        result = do_calculation_work(i)
        results.append(result)
    return results

def run_processing(tasks = 5, max_workers = 5):
    results = []
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(do_calculation_work, i) for i in range(tasks)]
        
        for future in as_completed(futures):
            result = future.result()
            results.append(result)
    return results

if __name__ == '__main__':
    start_time = time.perf_counter()
    results = run_threading()
    elapsed_time = time.perf_counter() - start_time
    for result in results:
        print(f"{result}")
    
    print(f"Elapsed time: {elapsed_time}")
    # Process calculation tasks 5 times without multiprocessing
    start_time = time.perf_counter()
    results = run_calculation_work()
    elapsed_time = time.perf_counter() - start_time
    for result in results:
        print(f"{result}")
    
    print(f"Elapsed time: {elapsed_time}")
    # Run processing code
    start_time = time.perf_counter()
    results = run_processing()
    elapsed_time = time.perf_counter() - start_time
    for result in results:
        print(f"{result}")
    
    print(f"Elapsed time: {elapsed_time}")