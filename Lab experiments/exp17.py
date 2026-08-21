from nltk.corpus import wordnet

word = "bank"

synsets = wordnet.synsets(word)

print("Word:", word)

print("\nSynsets and Meanings:")

for synset in synsets[:3]:
    print("\nSynset:", synset.name())
    print("Meaning:", synset.definition())
    print("Example:", synset.examples())