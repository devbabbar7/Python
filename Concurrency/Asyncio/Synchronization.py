import asyncio

shared_resource = 0

# Lock and Semaphore demonstration
async def modify_shared_resource():
    global shared_resource
    async with semaphore:
    # async with lock:
        # Critical section: only one coroutine can access this at a time
        print("Resource before modification:", shared_resource)
        shared_resource += 1
        await asyncio.sleep(1)  # Simulate time-consuming operation
        print("Resource after modification:", shared_resource)


# Event demonstration
async def waiter():
    print("Waiting for the event to be set...")
    await event.wait()  # Wait until the event is set
    print("Event is set! Proceeding with the task.")

async def setter():
    print("Setting the event after 2 seconds...")
    await asyncio.sleep(2) # Simulate some work before setting the event
    event.set()  # Set the event to allow waiters to proceed

async def main():
    global lock, semaphore, event
    lock = asyncio.Lock()
    semaphore = asyncio.Semaphore(2)  # Limit to 2 concurrent access
    event = asyncio.Event()
    await asyncio.gather(modify_shared_resource(), modify_shared_resource(), modify_shared_resource())
    await asyncio.gather(waiter(), setter())

asyncio.run(main())
