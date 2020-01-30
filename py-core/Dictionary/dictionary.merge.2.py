yusuke_power = {"Yusuke Urameshi": "Spirit Gun"}
hiei_power = {"Hiei": "Jagan Eye"}
powers = dict()

# Brute force
for dictionary in (yusuke_power, hiei_power):
    for key, value in dictionary.items():
        powers[key] = value

# Dictionary Comprehension
powers = {key: value for d in (yusuke_power, hiei_power)
          for key, value in d.items()}

# Copy and update
powers = yusuke_power.copy()
powers.update(hiei_power)

# Dictionary unpacking (Python 3.5+)
powers = {**yusuke_power, **hiei_power}

# Backwards compatible function for any number of dicts


def merge_dicts(*dicts: dict):
    merged_dict = dict()
    for dictionary in dicts:
        merge_dict.update(dictionary)
    return merged_dict
