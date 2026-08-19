import nltk

grammar = nltk.PCFG.fromstring("""
S -> NP VP [1.0]
NP -> Det N [0.6] | Det N [0.4]
VP -> V NP [1.0]
Det -> 'the' [1.0]
N -> 'boy' [0.5] | 'ball' [0.5]
V -> 'plays' [1.0]
""")

sentence = "the boy plays the ball".split()

parser = nltk.ViterbiParser(grammar)

print("Sentence:", " ".join(sentence))
print("\nMost Probable Parse Tree:")

for tree in parser.parse(sentence):
    print(tree)
    print("\nProbability:", tree.prob())