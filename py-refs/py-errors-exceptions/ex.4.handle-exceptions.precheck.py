# if something could regularly fail in one or more specific ways, it is often best to use a try...except statement to handle those situations.

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
