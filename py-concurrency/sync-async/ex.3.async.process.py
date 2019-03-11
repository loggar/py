import time
import functools
from urllib.request import urlopen
from multiprocessing import Process


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


def io_bound(urls):
    data = []
    for url in urls:
        data.append(urlopen(url).read())
    return data


@timeit()
def multiprocessed(n_threads, func, *args):
    processes = []
    #pylint: disable=unused-variable
    for i in range(n_threads):
        p = Process(target=func, args=args)
        processes.append(p)

    # start the processes
    for p in processes:
        p.start()

    # ensure all processes have finished execution
    for p in processes:
        p.join()


if __name__ == '__main__':
    a = 7777
    b = 200000
    urls = [
        "http://google.com",
        "http://yahoo.com",
        "http://linkedin.com",
        "http://facebook.com"
    ]
    multiprocessed(10, cpu_bound, a, b)
    multiprocessed(10, io_bound, urls)
