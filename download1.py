import asyncio
import time

async def download_file(file_name, delay):
    print(f"Downloading {file_name}...")
    await asyncio.sleep(delay)  # Simulate download time asynchronously
    print(f"{file_name} downloaded.")

async def main():
    start_time = time.time()

    # Creating tasks to download files concurrently
    task1 = asyncio.create_task(download_file("File 1", 2))
    task2 = asyncio.create_task(download_file("File 2", 2))
    task3 = asyncio.create_task(download_file("File 3", 2))

    # Wait for all tasks to complete
    await task1
    await task2
    await task3
    #A more concise and efficient way to wait for multiple tasks:
    #await asyncio.gather(task1, task2, task3)

    end_time = time.time()
    print(f"Total time taken: {end_time - start_time:.2f} seconds")
    #Since all tasks have the same delay (2 seconds), they complete in ~2 seconds total (not 6 seconds) due to concurrency.

if __name__ == "__main__":
    asyncio.run(main())
#Task Creation ≠ Execution:

#asyncio.create_task() schedules tasks to run in the event loop but doesn't execute them immediately.

#The event loop starts processing tasks when it encounters the first await.

#Execution Flow:

#When await task1 is called:

#The event loop starts executing task1, task2, and task3 concurrently.

#The code pauses at await task1 until task1 completes.

#However, task2 and task3 are already running in the background while waiting for task1
#Maintains Concurrency: Despite appearing sequential, all three tasks run concurrently because they were created before any await is called.