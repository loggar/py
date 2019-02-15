from foobardb import FoobarDB

mydb = FoobarDB("./mydb.db")
mydb.set("name", "Palash")  # Sets Value
print(mydb.get("name"))
# python foobardb.usage.py
