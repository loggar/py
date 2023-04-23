PI = 3.14  # Value won't change, so it's a constant


class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    @property
    def area(self):
        return (self.radius ** 2) * PI

    @property
    def perimeter(self):
        return 2 * self.radius * PI


small_circle = Circle(1)
big_circle = Circle(5)

print(f"Area of small circle = {small_circle.area}")
print(f"Perimeter of small circle = {small_circle.perimeter}")

print(f"Area of big circle = {big_circle.area}")
print(f"Perimeter of big circle = {big_circle.perimeter}")
