
import asyncio

async def countdown_timer(n: int):
    """Counts down from n to 0 with a 1-second delay between each number."""
    print(f"Countdown starting from {n} seconds.")
    while n >= 0:
        print(n)
        await asyncio.sleep(1)
        n -= 1
    print(f"Countdown from {n + 1} complete!\n")

async def main():
    # Start multiple countdowns concurrently
    await asyncio.gather(
        countdown_timer(5),
        countdown_timer(3),
        countdown_timer(7)
    )

if __name__ == "__main__":
    asyncio.run(main())
