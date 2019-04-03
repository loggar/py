a = "welcome to codementor"
print(a.capitalize())

a = "python"
print(a.upper())

a = "Python"
print(a.lower())

a = "i love python and i love codementor"
print(a.count("love"))

a = "i love python and i love codementer"
print(a.index("o"))

a = "i love python and i love codementer"
print(a.index("o"))

a = "String string String string String"
print(a.endswith("String"))

a = "String string String string String3"
b = "StringstringStringstringString3"
print(a.isalnum())
print(b.isalnum())


a = "StringstringStringstringString3"
b = "StringstringStringstringString"
print(a.isalpha())
print(b.isalpha())

a = "StringstringStringstringString3"
b = "33434"
print(a.isdigit())
print(b.isdigit())

a = "i love codementor"
print(a.title())

a = "I love codementor"
print(a.islower())

b = "  "
print(b.isspace())

a = "I love python"
print(a.istitle())

a = "i love python"
print(a.isupper())

a = "sadhana loves python"
print(a.replace("sadhana", "manaswi"))
print(a.replace("p", "j"))

a = "Hello, python"
print(a.split(","))

a = "String string String string String"
print(a.startswith("String"))

a = "string String string string"
print(a.swapcase())

a = " Hello, Python "
print(a.strip())
print(a.rstrip())
print(a.lstrip())

a = "Hello, Codementor"
print(len(a))

s = ("Python", "love", "codementor")
x = " ".join(s)
print(x)

print("Sravan is a{0}boy, Also he is{0}student.So he{1}".format(
    "very good", "rocks"))
