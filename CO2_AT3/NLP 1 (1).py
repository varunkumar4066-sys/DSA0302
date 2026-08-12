import re
from datasets import load_dataset
from nltk.stem import PorterStemmer

# 1. Load PubMed 20k RCT dataset
data = load_dataset("pietrolesci/pubmed-20k-rct", split="train")

# Use first 5000 sentences for a simple experiment
texts = data["text"][:5000]

# 2. Preprocessing and tokenization
words = []

for text in texts:
    text = text.lower()
    words.extend(re.findall(r"[a-z]+", text))

# Remove duplicate words
words = list(set(words))

# 3. Apply Porter Stemmer
stemmer = PorterStemmer()

print("Total unique words:", len(words))
print("\nWord -> Porter Stem")

for word in words[:50]:
    print(word, "->", stemmer.stem(word))

# 4. Check important biomedical words
test_words = [
    "infection",
    "infectious",
    "infected",
    "infect",
    "infections",
    "infecting",
    "infective"
]

print("\n--- Biomedical Morphology Analysis ---")

for word in test_words:
    print(word, "->", stemmer.stem(word))

# 5. Find words with the same stem
print("\n--- Words grouped by Stem ---")

groups = {}

for word in test_words:
    stem = stemmer.stem(word)
    groups.setdefault(stem, []).append(word)

for stem, group in groups.items():
    print(stem, ":", group)

# 6. Explanation
print("\n--- Conclusion ---")
print("Porter Stemmer removes word endings using rules.")
print("It does not understand the real morphological structure")
print("or meaning of biomedical words.")
print("Therefore, derivational information can be lost.")