import time


async def count_a():
    print("one")
    await asyncio.sleep(1)
    print("four")


async def count_b():
    print("two")
    await asyncio.sleep(1)
    print("five")


async def count_c():
    print("three")
    await asyncio.sleep(1)
    print("six")


async def gather_example():
    await asyncio.gather(
        count_a(),
        count_b(),
        count_c()
    )


s = time.perf_counter()

await gather_example()

elapsed = time.perf_counter() - s
print(f"Script executed in {elapsed:0.2f} seconds.")

# Output: one
# Output: two
# Output: three
# Output: four
# Output: five
# Output: six
# Output: Script executed in 1.00 seconds.
