import asyncio
import time

async def downloading_files(filepath):
    print(f"downloading first file.....{filepath}")
    await asyncio.sleep(1)
    print(f"downloading second file.....{filepath}")
    await asyncio.sleep(3)
    print(f"downloading third file.....{filepath}")
    print("download completed")

async def main():
    start_time = time.time()
    await asyncio.gather(
        downloading_files("file1"),
        downloading_files("file2"),
        downloading_files("file3")
    )
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Total time taken: {elapsed_time:.2f} seconds")

# This is how we should run it - at the top level of our script
if __name__ == "__main__":
    asyncio.run(main())
    