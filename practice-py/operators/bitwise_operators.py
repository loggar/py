a = int('00111100', 2)
b = int('00001101', 2)

print(bin(a))
print(bin(b))

print(bin(a & b))
print(bin(a | b))
print(bin(a ^ b))
print(bin(~a))

a <<= int('11110000', 2)
print(bin(a))

a >>= int('00001111', 2)
print(bin(a))
