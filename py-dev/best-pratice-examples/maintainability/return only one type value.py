"""
def get_secret_code(password):
    if password != "bicycle":
        return None
    else:
        return "42"

secret_code = get_secret_code("unicycle")

if secret_code is None:
    print("Wrong password.")
else:
    print("The secret code is {}".format(secret_code))
"""


def get_secret_code(password):
    if password != "bicycle":
        raise ValueError
    else:
        return "42"


try:
    secret_code = get_secret_code("unicycle")
    print("The secret code is {}".format(secret_code))
except ValueError:
    print("Wrong password.")
