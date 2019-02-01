class Byzantium:

    def __init__(self):
        self.power = 0

    def gravity_field(self):
        if self.power <= 0:
            raise SystemError("Gravity Failing")


def grab_handle():
    pass


byzantium = Byzantium()


def test():
    try:
        byzantium.gravity_field()
    except SystemError as e:
        grab_handle()
        raise RuntimeError("Night night") from e


try:
    test()
except RuntimeError as e:
    print(e)
    print(e.__cause__)
