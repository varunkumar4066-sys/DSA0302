import re
import math
from collections import Counter

train = [
    "the student is reading a book",
    "the student is writing an assignment",
    "the student is learning python",
    "the student likes machine learning",
    "the teacher is teaching the student"
]

test = [
    "the student is reading a book",
    "the student likes machine learning",
    "the teacher is teaching the student",
    "the student plays football"
]

train = [['<s>'] + re.findall(r'\b[a-z]+\b', s) + ['</s>'] for s in train]
test = [['<s>'] + re.findall(r'\b[a-z]+\b', s) + ['</s>'] for s in test]

uni, bi, tri = Counter(), Counter(), Counter()

for s in train:
    uni.update(s)
    bi.update(zip(s, s[1:]))
    tri.update(zip(s, s[1:], s[2:]))

V = len(uni)
N = sum(uni.values())

def probability(s, i, n, smooth=False):
    w = s[i]

    if n == 1:
        return (uni[w] + smooth) / (N + smooth*V)

    if n == 2:
        c = bi[s[i-1], w] + smooth
        d = uni[s[i-1]] + smooth*V
    else:
        c = tri[s[i-2], s[i-1], w] + smooth
        d = bi[s[i-2], s[i-1]] + smooth*V

    return c / d if d else 0

def entropy(s, n, smooth=False):
    values = []
    for i in range(1, len(s)):
        p = probability(s, i, n, smooth)
        if p == 0:
            return float("inf")
        values.append(-math.log2(p))
    return sum(values) / len(values)

for n in [1, 2, 3]:
    print("\nN =", n)

    for s in test:
        print(
            " ".join(s),
            "->",
            entropy(s, n)
        )

print("\n--- Smoothed Entropy ---")

for n in [1, 2, 3]:
    values = [entropy(s, n, True) for s in test]
    print("N =", n, "Average =", round(sum(values)/len(values), 4))

print("\nInterpretation:")
print("Low entropy = more predictable words.")
print("High entropy = less predictable words.")
print("Smoothing avoids zero probabilities for unseen N-grams.")