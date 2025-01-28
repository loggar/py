import re


def is_only_non_english(text):
    # ^: start of string, $: end of string
    # Match if the entire string contains NO English letters
    return bool(re.match(r"^[^a-zA-Z]+$", text))


# Test examples
print(is_only_non_english("世界"))  # True
print(is_only_non_english("Hello世界"))  # False
print(is_only_non_english("123"))  # True
print(is_only_non_english(""))  # False
