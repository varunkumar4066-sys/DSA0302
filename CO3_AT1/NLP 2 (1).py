import re
from collections import Counter

corpus = """
the student is reading a book
the student is writing an assignment
the student is learning python
the student likes machine learning
the teacher is teaching the student
the teacher is reading a book
the student reads the book
the student works on a project
"""

sentences = [['<s>'] + re.findall(r'\b[a-z]+\b', s.lower()) + ['</s>']
             for s in corpus.strip().split('\n')]

uni, bi, tri = Counter(), Counter(), Counter()

for s in sentences:
    uni.update(s)
    bi.update(zip(s, s[1:]))
    tri.update(zip(s, s[1:], s[2:]))

total = sum(uni.values())

def p1(w):
    return uni[w] / total

def p2(a, b):
    return bi[a, b] / uni[a] if uni[a] else 0

def p3(a, b, c):
    return tri[a, b, c] / bi[a, b] if bi[a, b] else 0

# Backoff: trigram -> bigram -> unigram
def backoff(a, b, c):
    if p3(a, b, c): return p3(a, b, c), "Trigram"
    if p2(b, c): return p2(b, c), "Bigram"
    return p1(c), "Unigram"

# Deleted interpolation
l1, l2, l3 = 0.2, 0.3, 0.5

def interpolate(a, b, c):
    return l1*p1(c) + l2*p2(b, c) + l3*p3(a, b, c)

def predict(text, model):
    w = re.findall(r'\b[a-z]+\b', text.lower())
    if len(w) < 2:
        return None

    result = []
    for x in uni:
        if model == "unsmoothed":
            p = p3(w[-2], w[-1], x)
        elif model == "backoff":
            p, _ = backoff(w[-2], w[-1], x)
        else:
            p = interpolate(w[-2], w[-1], x)
        result.append((x, p))

    return max(result, key=lambda x: x[1])

while True:
    print("\n1.Unsmoothed  2.Backoff  3.Interpolation  4.Compare  5.Exit")
    ch = input("Choice: ")

    if ch == "5":
        break

    text = input("Enter sentence: ")

    if ch in "123":
        model = ["unsmoothed", "backoff", "interpolation"][int(ch)-1]
        ans = predict(text, model)
        print("Prediction:", ans)

        if model == "backoff":
            w = re.findall(r'\b[a-z]+\b', text.lower())
            print("Used:", backoff(w[-2], w[-1], ans[0])[1])

    elif ch == "4":
        for model in ["unsmoothed", "backoff", "interpolation"]:
            print(model, ":", predict(text, model))