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

    end_time = time.time()
    print(f"Total time taken: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
