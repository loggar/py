num = 1

while num <= 10:
    print(num)
    num += 1



loop_condition = True

while loop_condition:
    print("Loop Condition keeps: %s" % (loop_condition))
    loop_condition = False



for i in range(1, 11):
    print(i)



bookshelf = [
    "The Effective Engineer",
    "The 4 hours work week",
    "Zero to One",
    "Lean Startup",
    "Hooked"
]

for book in bookshelf:
    print(book)
