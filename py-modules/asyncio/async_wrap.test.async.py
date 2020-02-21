import asyncio
from functools import wraps, partial
import time


def async_wrap(func):
    @wraps(func)
    async def run(*args, loop=None, executor=None, **kwargs):
        if loop is None:
            loop = asyncio.get_event_loop()
        pfunc = partial(func, *args, **kwargs)
        return await loop.run_in_executor(executor, pfunc)
    return run


async_sleep = async_wrap(time.sleep)


async def count():
    print("func start")
    await async_sleep(1)
    print("func end")


async def main():
    await asyncio.gather(count(), count(), count())


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f"Time elapse: {end-start}")
