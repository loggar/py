import random
import string


def random_base26(length):
    # Generate a random number within the range of base26 values
    max_val = 26**length - 1
    random_num = random.randint(0, max_val)
    # Convert the number to a base26 string using only letters
    alphabet = string.ascii_lowercase  # Only use lowercase letters
    result = []
    while len(result) < length:
        random_num, i = divmod(random_num, 26)  # Adjust modulus to 26 for alphabet
        result.append(alphabet[i])
    # Ensure the result is at least the desired length and reverse to correct order
    return "".join(result[::-1])


# Generate a random string with 5 characters that are all letters
print(random_base26(5))
