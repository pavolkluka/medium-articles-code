import math
from collections import Counter

def calc_entropy(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
    byte_counts = Counter(data)
    entropy = 0.0
    for count in byte_counts.values():
        p = count / len(data)
        entropy -= p * math.log2(p)
    return entropy

print(f"Entropy for 1: {calc_entropy('export-objects/195.178.136.19/1'):.4f} bits/byte")
print(f"Entropy for 2: {calc_entropy('export-objects/195.178.136.19/2'):.4f} bits/byte")
print(f"Entropy for 3: {calc_entropy('export-objects/195.178.136.19/3'):.4f} bits/byte")
