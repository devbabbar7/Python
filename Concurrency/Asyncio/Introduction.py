import asyncio

# Coroutine function
# It needs to be awaited to execute, otherwise it will return a coroutine object
async def main():
    print("1")
    await asyncio.sleep(1) # Simulate an IO operation
    await main2() # Wait for main2 to finish executing before proceeding
    await asyncio.sleep(1)
    print("4")

async def main2():
    print("2")
    await asyncio.sleep(1) # Simulate an IO operation
    print("3")

asyncio.run(main())
# main() # This will not execute the coroutine, it will return a coroutine object instead.
# Output:
# 1
# 2
# 3
# 4





# Introduction to create_task

# The problem with the below code is that if fn finishes before fn2, then fn2 will not execute till completion without awaiting it.
# We can solve this using await task.
async def fxn():
    # create_task will add fun2 to the event loop and it will run concurrently with fn
    task=asyncio.create_task(fxn2())
    print("one")
    print('four')
    await asyncio.sleep(1)
    print('five')
    await asyncio.sleep(1)
    # Solution:
    await task # by adding this, we guarantee that fn2 will finish executing otherwise as soon as fn finishes, the program will exit and fn2 will not execute till completion.

async def fxn2():
    #await asyncio.sleep(1)
    print("two")
    await asyncio.sleep(1)
    print("three")
    
asyncio.run(fxn())
# Output
# one
# four
# two
# five
# three



async def fn():
    print("one")
    await asyncio.sleep(1)
    print('four')
    await asyncio.sleep(1)
    print('five')
    await asyncio.sleep(1)
    return True

async def fn2():
    await asyncio.sleep(1)
    print("two")
    await asyncio.sleep(1)
    print("three")
    return False

async def set_future_result(future):
    await asyncio.sleep(1)
    future.set_result("Future result") # We can set the result of the future using set_result method
    print("Future result set")


# We can't call create_task or await outside of an async function, so we need to create a main function to call create_task and run it using asyncio.run
async def main():
    # Synchronous execution, fn will execute first and then fn2 will execute, which is not what we want in this case.
    task1 = fn()
    task2 = fn2()
    await task1
    await task2


    # Asynchronously execute both functions using create_task
    task1 = asyncio.create_task(fn())
    task2 = asyncio.create_task(fn2())

    # If we don't use below await statements, main will finish executing before fn and fn2 finish executing
    # By adding these await statements, we guarantee that main will wait for both fn and fn2 to finish executing before exiting.
    result1 = await task1
    result2 = await task2
    print(result1, result2) # Output: True False



    # Asynchronously execute both functions using gather
    task = asyncio.gather(fn(), fn2()) # gather will run both functions concurrently and wait for both to finish before proceeding
    # task = asyncio.gather(*[fn(), fn2()]) # This is another way to call gather, it will unpack the list of coroutines and pass them as separate arguments to gather
    result1, result2 = await task

    # or

    # results = await asyncio.gather(fn(), fn2())
    # result1, result2 = results
    # print(result1, result2) # Output: True False




    # Asynchronously execute both functions using TaskGroup
    # If any of the tasks in the TaskGroup raises an exception, the TaskGroup will cancel all other tasks and raise the exception. 
    # This is useful for ensuring that if one task fails, all other tasks are also cancelled to prevent any unintended consequences.
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(fn())
        task2 = tg.create_task(fn2())
    print(task1.result(), task2.result()) # Output: True False





# Introduction to futures
# Future
# A Future is a low-level object that represents a result that may not be available yet. 
# It is used to bridge the gap between callback-based code and async/await code.
# A future method guarantees that the result will be set at some point in the future, and we can await the future to get its result once it is set.
loop = asyncio.get_running_loop() # We can get the current event loop using get_running_loop method, which will allow us to create a future that is associated with the current event loop.

future = loop.create_future() 
asyncio.create_task(set_future_result(future)) # We can set the result of the future in a separate task, which will allow us to simulate an asynchronous operation that sets the result of the future after some time.

result = await future # We can await the future to get its result once it is set.
print(result) # Output: Future result



asyncio.run(main())