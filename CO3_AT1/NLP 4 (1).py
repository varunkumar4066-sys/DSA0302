import re
from collections import Counter, defaultdict

train = [
    [("the","DT"),("student","NN"),("reads","VBZ"),("a","DT"),("book","NN")],
    [("the","DT"),("teacher","NN"),("teaches","VBZ"),("the","DT"),("student","NN")],
    [("she","PRP"),("reads","VBZ"),("the","DT"),("book","NN")],
    [("he","PRP"),("likes","VBZ"),("the","DT"),("book","NN")],
    [("students","NNS"),("are","VBP"),("learning","VBG"),("python","NN")],
    [("the","DT"),("student","NN"),("is","VBZ"),("happy","JJ")],
    [("the","DT"),("student","NN"),("works","VBZ"),("hard","RB")]
]

lexicon = dict(
    x for s in train for x in s
)

def words(text):
    return re.findall(r'\b[a-z]+\b', text.lower())

# ---------------- RULE BASED ----------------

def rule_tagger(text):
    ans = []

    for w in words(text):
        if w in lexicon:
            tag = lexicon[w]
        elif w.endswith("ly"):
            tag = "RB"
        elif w.endswith("ing"):
            tag = "VBG"
        elif w.endswith("ed"):
            tag = "VBD"
        elif w.endswith("s"):
            tag = "NNS"
        else:
            tag = "NN"
        ans.append((w, tag))

    return ans

# ---------------- STOCHASTIC ----------------

emit = defaultdict(Counter)
trans = defaultdict(Counter)
tags = set()

for s in train:
    prev = "<S>"
    for w, t in s:
        emit[t][w] += 1
        trans[prev][t] += 1
        tags.add(t)
        prev = t

def stochastic(text):
    ws = words(text)
    score, path = {}, {}

    for t in tags:
        score[t] = trans["<S>"][t] * emit[t][ws[0]]
        path[t] = [t]

    for w in ws[1:]:
        new, newpath = {}, {}

        for t in tags:
            best = max(
                ((score[p] * (trans[p][t]+1) *
                  (emit[t][w]+1)), p) for p in tags
            )
            new[t] = best[0]
            newpath[t] = path[best[1]] + [t]

        score, path = new, newpath

    best = max(score, key=score.get)
    return list(zip(ws, path[best]))

# ---------------- TRANSFORMATION BASED ----------------

def transformation(text):
    result = rule_tagger(text)

    for i, (w, t) in enumerate(result):
        prev = result[i-1][1] if i else ""

        # Pronoun + noun -> verb
        if prev == "PRP" and t in ("NN", "NNS"):
            result[i] = (w, "VB")

        # Auxiliary + noun -> verb
        elif prev in ("VBZ", "VBP") and t in ("NN", "NNS"):
            result[i] = (w, "VB")

    return result

def show(title, result):
    print(title, ":", " ".join(w+"/"+t for w,t in result))

# ---------------- MAIN ----------------

while True:
    print("\n1.Rule Based  2.Stochastic  3.Transformation  4.Compare  5.Exit")
    ch = input("Choice: ")

    if ch == "5":
        break

    text = input("Enter sentence: ")

    if ch == "1":
        show("Rule Based", rule_tagger(text))

    elif ch == "2":
        show("Stochastic", stochastic(text))

    elif ch == "3":
        show("Transformation", transformation(text))

    elif ch == "4":
        show("Rule Based", rule_tagger(text))
        show("Stochastic", stochastic(text))
        show("Transformation", transformation(text))