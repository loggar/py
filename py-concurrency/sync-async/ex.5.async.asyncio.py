import time
import functools
from urllib.request import urlopen
import asyncio
import aiohttp


class timeit(object):
    def __call__(self, f):
        @functools.wraps(f)
        def decorated(*args, **kwds):
            with self:
                return f(*args, **kwds)
        return decorated

    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, *args, **kw):
        elapsed = time.time() - self.start_time
        print("{:.3} sec".format(elapsed))


def cpu_bound(a, b):
    return a ** b


async def async_func(N, func, *args):
    coros = [func(*args) for _ in range(N)]
    # run awaitable objects concurrently
    await asyncio.gather(*coros)


async def a_cpu_bound(a, b):
    result = await loop.run_in_executor(None, cpu_bound, a, b)
    return result


async def a_io_bound(urls):
    # create a coroutine function where we will download from individual url
    async def download_coroutine(session, url):
        async with session.get(url, timeout=10) as response:
            await response.text()

    # set an aiohttp session and download all our urls
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            await download_coroutine(session, url)


if __name__ == '__main__':
    a = 7777
    b = 200000
    urls = [
        "http://google.com",
        "http://yahoo.com",
        "http://linkedin.com",
        "http://facebook.com"
    ]
    loop = asyncio.get_event_loop()
    with timeit():
        loop.run_until_complete(async_func(10, a_cpu_bound, a, b))

    with timeit():
        loop.run_until_complete(async_func(10, a_io_bound, urls))
