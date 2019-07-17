players = ["John", "Anne", "Hannah"]

for counter, player in enumerate(players):
    print(f"{counter}: {player}")

for counter, player in enumerate(players, start=1):
    print(f"{counter}: {player}")
