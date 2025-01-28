import asyncio

async def process_data(data_id, delay):
    print(f"{data_id}: starting processing...")
    await asyncio.sleep(delay)
    print(f" Data {data_id}: processing done in {delay} seconds")

async def monitor_tasks():
    """Monitor task statuses and print status every second."""
    while True:
        print("Monitoring tasks: Program still running...")
        await asyncio.sleep(1)

async def main():
    #starting tasks in the backgroud
    task1 = asyncio.create_task(process_data(1, 2))
    task2 = asyncio.create_task(process_data(2, 1))
    task3 = asyncio.create_task(process_data(3, 3))

    # Create monitoring task
    monitor_task = asyncio.create_task(monitor_tasks())


    #waiting for all tasks to finish
    await asyncio.gather(task1, task2, task3)

    # Cancel the monitoring task after other tasks are done
    monitor_task.cancel()
    try:
        await monitor_task
    except asyncio.CancelledError:
        print("Monitoring stopped. All tasks are complete.")


asyncio.run(main())

#Summary: Coroutine Switching Process
#1. The main() function is the entry point of the program.
#2. The main() function creates three tasks to run concurrently.
#3. The main() function creates a monitoring task to run concurrently.
#4. The main() function waits for all tasks to finish.
#5. The main() function cancels the monitoring task after other tasks are done.
#6. The main() function handles the CancelledError exception when the monitoring task is cancelled.
#7. The asyncio.run() function runs the main() function.

#Summary: Coroutine Switching Process
#Task encounters await asyncio.sleep → Pauses.
#Event loop checks other tasks → Runs monitor_tasks.
#Other tasks sleep or finish → Event loop switches to the next ready coroutine.
#Tasks resume after sleep → Tasks complete one by one in an overlapping manner.
#All tasks are complete → Monitoring task is cancelled.

#How the Event Loop Works at await asyncio.sleep
#Hitting await asyncio.sleep(delay) in process_data:
#When the program encounters await asyncio.sleep(delay), it tells the event loop:

#"Hey, I'm pausing this coroutine for delay seconds. You can run other tasks now!"

#The event loop immediately "releases" control from this task and moves to check other scheduled tasks.


# Jumping to Other Coroutines (monitor_tasks)
# Event Loop Jumps to monitor_tasks:
# Since monitor_tasks() is also a coroutine scheduled in asyncio.create_task, it gets its turn in the event loop.
# The event loop starts running monitor_tasks:
# It prints the message "Monitoring tasks: Program still running...".
# await asyncio.sleep(1)
# When it hits await asyncio.sleep(1) inside monitor_tasks, it pauses monitor_tasks for 1 second.
# The event loop jumps back to the next ready coroutine, which is the process_data tasks.
# The event loop keeps switching between the process_data tasks and monitor_tasks until all tasks are complete.

