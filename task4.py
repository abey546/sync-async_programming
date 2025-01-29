import asyncio

async def countdown_timer(n: int) -> None:
    """
    Coroutine that counts down from n to 0, with a 1-second delay between numbers.
    
    Args:
        n (int): The starting number for the countdown
    """
    # Store the initial value to identify this countdown in the output
    initial_value = n
    
    # Continue counting while n is greater than or equal to 0
    while n >= 0:
        print(f"Countdown from {initial_value}: {n}")
        # Pause execution for 1 second without blocking other coroutines
        await asyncio.sleep(1)
        n -= 1
    
    print(f"Countdown from {initial_value} complete!")

async def main():
    """
    Main coroutine that demonstrates running multiple countdown timers concurrently.
    Creates three countdown tasks and runs them simultaneously using asyncio.gather.
    """
    # Create three countdown coroutines with different durations
    countdown_5 = countdown_timer(5)
    countdown_3 = countdown_timer(3)
    countdown_7 = countdown_timer(7)
    
    # Run all three countdowns concurrently
    # asyncio.gather allows us to wait for multiple coroutines to complete
    print("Starting all countdowns...")
    await asyncio.gather(
        countdown_5,
        countdown_3,
        countdown_7
    )
    print("All countdowns completed!")

# Run the event loop
if __name__ == "__main__":
    # Create and run the event loop until main() completes
    asyncio.run(main())