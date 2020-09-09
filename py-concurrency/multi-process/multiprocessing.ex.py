import time
from multiprocessing import Pool


def increment(input):
    for i in range(1000000):
        input = input + 1


if __name__ == "__main__":
    inputs = [1] * 100
    pool = Pool(8)
    started = time.time()
    pool.map(increment, inputs)

    elapsed = time.time()
    print('Time taken MultiProcess :', elapsed - started)

    pool.close()
