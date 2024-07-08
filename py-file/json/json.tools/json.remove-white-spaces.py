import json

# Step 1: Read the original JSON file
with open("original.json", "r") as file:
    data = json.load(file)

# Step 2: Write the data to a new JSON file without whitespace
with open("compact.json", "w") as file:
    json.dump(data, file, separators=(",", ":"))
