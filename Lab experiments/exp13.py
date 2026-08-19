import nltk

grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the'
N -> 'boy' | 'ball'
V -> 'plays'
""")

sentence = "the boy plays the ball".split()

parser = nltk.ChartParser(grammar)

print("Sentence:", " ".join(sentence))
print("\nParse Tree:")

for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()