def initiate_security_protocol(c):
    if c == 1:
        print("Returning onboard companion to home location...")
    if c == 712:
        print("Dematerializing to preset location...")


try:
    code = int(input("Enter security protocol code: "))
except ValueError:
    code = 0
initiate_security_protocol(code)
