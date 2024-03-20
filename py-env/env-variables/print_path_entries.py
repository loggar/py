import os


def print_path_entries_with_count():
    # Get the PATH environment variable
    path = os.environ.get("PATH")
    if path is None:
        print("PATH environment variable not found.")
        return

    # Split the PATH variable into individual entries
    path_entries = path.split(os.pathsep)

    # Dictionary to keep track of entry counts
    entry_counts = {}

    # Iterate over each entry and print with current count
    for entry in path_entries:
        entry_counts[entry] = entry_counts.get(entry, 0) + 1
        print(f"{entry} {entry_counts[entry] if entry_counts[entry] > 1 else ''}")


# Execute the function
if __name__ == "__main__":
    print_path_entries_with_count()
