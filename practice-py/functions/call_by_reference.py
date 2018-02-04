# Function definition is here
def changeme(l):
    "This changes a passed list into this function"
    print("Values inside the function before change: ", l)
    l[2] = 50
    print("Values inside the function after change: ", l)
    return


# Now you can call changeme function
mylist = [10, 20, 30]
changeme(mylist)
print("Values outside the function: ", mylist)
