class SonicScrewdriver:

    def __init__(self):
        self.memory = 0

    def perform_division(self, lhs, rhs):
        try:
            result = float(lhs)/float(rhs)
        except ZeroDivisionError:
            print("Wibbly wobbly, timey wimey.")
            result = "Infinity"
        except (ValueError, UnicodeError):
            print("Oy! Don't diss the sonic!")
            result = "Cannot Calculate"
        else:
            self.memory = result
        finally:
            print(f"Calculation Result: {result}\n")


sonic = SonicScrewdriver()

sonic.perform_division(8, 4)
sonic.perform_division(4, 0)
sonic.perform_division(4, "zero")

print(f"Memory Is: {sonic.memory}")
