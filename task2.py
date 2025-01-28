import asyncio
import time

async def proccess_data(data_id, delay):
    print(f"Start processing data with id: {data_id}")
    await asyncio.sleep(delay) # Simulate delay
    print(f"Data {data_id}: Processing complete after {delay} seconds.")
async def main():

    time_start = time.time()
    await asyncio.gather(
        proccess_data(1,2),

        proccess_data(2,3),
        proccess_data(3,1)

    )
    time_end = time.time()
    time_elapsed = time_end - time_start
    print(f"Time elapsed: {time_elapsed}")

asyncio.run(main()) 