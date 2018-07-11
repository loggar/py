class Person:
    def __init__(self, first_name, email):
        self.first_name = first_name
        self._email = email

    def update_email(self, new_email):
        self._email = new_email

    def email(self):
        return self._email


tk = Person('TK', 'tk@mail.com')
print(tk.email())  # => tk@mail.com

# tk._email = 'new_tk@mail.com'
# [pylint] W0212:Access to a protected member _email of a client class

print(tk.email())  # => tk@mail.com

tk.update_email('new_tk@mail.com')
print(tk.email())  # => new_tk@mail.com
