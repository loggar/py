from collections import defaultdict

d = defaultdict(lambda: 6)
d["k"] += 1

print(d["k"])  # 7
