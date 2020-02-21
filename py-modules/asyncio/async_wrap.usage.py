import time
import os

from async_wrap import async_wrap

async_sleep = async_wrap(time.sleep)
async_remove = async_wrap(os.remove)

# or use decorator style
@async_wrap
def my_async_sleep(duration):
    time.sleep(duration)
