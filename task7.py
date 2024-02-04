import random
from collections import defaultdict, OrderedDict

nums = 10_000_000
counts = defaultdict(int)
for _ in range(nums):
    dice = random.randint(1, 6)
    dice_two = random.randint(1, 6)
    counts[dice + dice_two] += 1

probabilities = {key: count / nums for key, count in counts.items()}
probabilities = OrderedDict(sorted(probabilities.items()))

print("+-----+-----------+")
print("| Key |  Value    |")
print("+-----+-----------+")

for key, value in probabilities.items():
    value = f"{value:.2%}"
    print(f"| {key:^3} | {value:<9} |")

print("+-----+-----------+")
