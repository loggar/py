print(type(0))
print(type(0.0))
print(type("0.0"))
print(type([]))
print(type({}))

someTuple = ('abcd', 786, 2.23, 'john', 70.2)
print(type(someTuple))

print(isinstance({}, dict))
print(isinstance([], dict))


class SampleClass1(object):
    pass


class SampleClass2(SampleClass1):
    pass


a = SampleClass1()
b = SampleClass2()

print(type(a))
print(type(b))

print(isinstance(a, object))
print(isinstance(a, SampleClass1))
print(isinstance(b, SampleClass2))
print(isinstance(b, SampleClass1))
print(isinstance(a, SampleClass2))
