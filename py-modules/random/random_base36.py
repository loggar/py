import random
import string


def random_base36(length):
    # Generate a random number within the range of base36 values
    max_val = 36**length - 1
    random_num = random.randint(0, max_val)
    # Convert the number to a base36 string
    alphabet = string.digits + string.ascii_lowercase
    result = ""
    while random_num:
        random_num, i = divmod(random_num, 36)
        result = alphabet[i] + result
    # Ensure the result is padded to the desired length
    return result.zfill(length)


# Generate a random base36 number with 5 characters
print(random_base36(5))
