import random
import string


def random_base36_alpha_only(length):
    # Create a string containing only lowercase letters
    alphabet = string.ascii_lowercase
    # Generate a random string of the desired length using the alphabet
    result = "".join(random.choice(alphabet) for _ in range(length))
    return result


# Generate a 5-character random string with only alphabet letters
print(random_base36_alpha_only(5))
