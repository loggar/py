# The "forgiveness, not permission" comes into play here: instead of testing first, we use try...except.

datafile_index = {
    # Omitted for brevity.
    # Just assume there's a lot of data in here.
}


def get_datafile_id(subject):
    if subject in datafile_index:
        identi = datafile_index[subject]
        print(f"See datafile {identi}.")
    else:
        print(f"Datafile not found on {subject}")


datafile_index["Clara Oswald"] = 2342342
get_datafile_id("Clara Oswald")
get_datafile_id("Ashildir")

# In Python, we don't consider exceptions to be something to be avoided. In fact, try...except is a regular part of many Python design patterns and algorithms. Don't be afraid of raising and catching exceptions! In fact, even keyboard interruptions are handled this way, via the KeyboardInterrupt exception.

# Gotcha Alert: try...except is a powerful tool, but it isn't for everything. For example, returning None from a function is often considered better than raising an exception. Only raise an exception when an actual error occurs that is best handled by the caller.
