# Question 4 – Morphological Error Analysis in Information Retrieval

import re
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

# Sample Amazon product-review text
text = """
I bought two watches and I am watching the product review.
This washable cloth is useful with the washer.
The clothes were washed yesterday.
"""

words = re.findall(r"[a-z]+", text.lower())

# 1. Analyze Porter stemming errors
print("WORD -> PORTER STEM")
print("-" * 25)

for word in words:
    print(word, "->", stemmer.stem(word))

# 2. Analyze the given search terms
terms = ["watches", "watching", "washable", "washer", "washed"]

print("\nMORPHOLOGICAL ANALYSIS")
print("-" * 40)

for word in terms:
    stem = stemmer.stem(word)

    if word in ["watches", "watching", "washed"]:
        category = "Inflectional"
    else:
        category = "Derivational"

    print(word, "->", stem, "->", category)

# 3. Show related words grouped by stem
print("\nSTEM GROUPS")
print("-" * 25)

groups = {}

for word in terms:
    groups.setdefault(stemmer.stem(word), []).append(word)

for stem, group in groups.items():
    print(stem, ":", group)

# 4. Improved preprocessing strategy
def improved_preprocess(word):
    # Keep derivational forms separate
    derivational = ["able", "er"]

    for suffix in derivational:
        if word.endswith(suffix) and len(word) > len(suffix) + 2:
            return word

    # Remove only common inflectional endings
    if word.endswith("ing") and len(word) > 5:
        return word[:-3]

    if word.endswith("ed") and len(word) > 4:
        return word[:-2]

    if word.endswith("s") and not word.endswith("ss"):
        return word[:-1]

    return word

print("\nIMPROVED PREPROCESSING")
print("-" * 35)

for word in terms:
    print(word, "->", improved_preprocess(word))

print("\nCONCLUSION")
print("Inflectional suffixes such as -s, -ed and -ing can often")
print("be normalized for search. Derivational suffixes such as")
print("-able and -er should be retained because they can create")
print("new words with different meanings.")
print("A morphological analyzer or lemmatizer is preferable to")
print("blind Porter stemming for product search.")