def outer_function(text):
    (lambda:  # inner function
        print(text)
     )()


outer_function('bar')

# Output: bar
