class Person:
    def __init__(self, first_name):
        self.first_name = first_name


tk = Person('TK')
print(tk.first_name)  # => TK

tk.first_name = 'Kaio'
print(tk.first_name)  # => Kaio
