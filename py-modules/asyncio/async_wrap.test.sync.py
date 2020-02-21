import time


def count():
    print("func start")
    time.sleep(1)
    print("func end")


def main():
    funcs = [count, count, count]
    for func in funcs:
        func()


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time elapse: {end-start}")
