import time
import functools
from urllib.request import urlopen
import gevent.monkey


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


# patch any other imported module that has a blocking code in it
# to make it asynchronous.
gevent.monkey.patch_all()


@timeit()
def green_threaded(n_threads, func, *args):
    jobs = []
    #pylint: disable=unused-variable
    for i in range(n_threads):
        jobs.append(gevent.spawn(func, *args))
    # ensure all jobs have finished execution
    gevent.wait(jobs)


if __name__ == '__main__':
    a = 7777
    b = 200000
    urls = [
        "http://google.com",
        "http://yahoo.com",
        "http://linkedin.com",
        "http://facebook.com"
    ]
    green_threaded(10, cpu_bound, a, b)
    green_threaded(10, io_bound, urls)
