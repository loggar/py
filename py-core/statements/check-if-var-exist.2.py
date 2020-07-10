test1 = 5

for var in ["test1", "test2"]:
    if var in {**globals(), **locals()}:
        print(f"{var} exist")
    else:
        print(f"{var} does not exist")
