class Byzantium:

    def __init__(self):
        self.power = 0

    def gravity_field(self):
        if self.power <= 0:
            raise SystemError("Gravity Failing")


def grab_handle():
    pass


byzantium = Byzantium()

try:
    byzantium.gravity_field()
except SystemError:
    grab_handle()
    print("Night night")
    raise
