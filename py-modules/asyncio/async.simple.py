import asyncio


async def simple():
    print("count one")
    await asyncio.sleep(1)
    print("count two")

await simple()

# Output: count one
# Output: count two
