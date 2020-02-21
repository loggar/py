from foobardb import FoobarDB

mydb = FoobarDB("./mydb.json")
mydb.set("name", "Palash")  # Sets Value
print(mydb.get("name"))

# python foobardb.usage.py
