try:
    5 / 0
except ZeroDivisionError as e:
    print("ZeroDivisionError")
except Exception as e:
    print("Exception")
