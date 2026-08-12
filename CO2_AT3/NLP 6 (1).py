# Question 6 – Finite-State Morphological Parser

import nltk
from nltk.corpus import wordnet as wn

nltk.download("wordnet", quiet=True)

# Irregular plurals
irregular = {
    "children": "child",
    "men": "man",
    "women": "woman",
    "mice": "mouse",
    "feet": "foot",
    "teeth": "tooth",
    "people": "person",
    "geese": "goose"
}

def parser(word):
    # Irregular plural
    if word in irregular:
        return irregular[word], "Plural Noun"

    # Words ending in -ies
    if word.endswith("ies"):
        base = word[:-3] + "y"
        if wn.morphy(base, wn.NOUN):
            return base, "Plural Noun"

    # Words ending in -es
    if word.endswith("es"):
        base = word[:-2]
        if wn.morphy(base, wn.NOUN):
            return base, "Plural Noun"

    # Regular plural ending in -s
    if word.endswith("s") and not word.endswith("ss"):
        base = word[:-1]
        if wn.morphy(base, wn.NOUN):
            return base, "Plural Noun"

    # Otherwise singular
    return word, "Singular Noun"


# Test words
words = [
    "cars", "boxes", "cities", "children",
    "dogs", "buses", "watches", "men",
    "women", "mice", "books"
]

print("WORD       BASE FORM     TYPE")
print("-" * 35)

for w in words:
    base, tag = parser(w)
    print(f"{w:<10} {base:<13} {tag}")

print("\nWORDNET VERIFICATION")
print("-" * 35)

for w in words:
    lemma = wn.morphy(w, wn.NOUN)
    print(f"{w:<10} -> {lemma}")

print("\nLIMITATIONS:")
print("1. Rule-based parsing cannot handle all English exceptions.")
print("2. Some words have irregular plural forms.")
print("3. Some words ending in 's' are actually singular.")
print("4. Spelling changes can require additional rules.")
print("5. Rules may become complex as the vocabulary increases.")