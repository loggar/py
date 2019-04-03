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
            return result
        finally:
            print(f"Calculation Result: {result}\n")
            result = -1


sonic = SonicScrewdriver()

print(sonic.perform_division(8, 4))
