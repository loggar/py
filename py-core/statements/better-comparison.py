def is_even(x):
    return True if x % 2 == 0 else False


x = 10

# different comparison statements which result in the same result:
if is_even(x) == True:
    print(f"{x} is an even number!")

if is_even(x) is True:
    print(f"{x} is an even number!")

if is_even(x):
    print(f"{x} is an even number!")

# more junior example
# if is_even(number) == True:

# more senior example
# if is_even is True:

# more junior example
# if value == None:

# more senior example
# if value is None:
