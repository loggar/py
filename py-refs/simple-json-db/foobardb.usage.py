from foobardb import FoobarDB

mydb = FoobarDB("./mydb.db")
mydb.set("name", "Palash")  # Sets Value
mydb.get("name")
