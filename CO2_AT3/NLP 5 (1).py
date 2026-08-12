# Question 5 – Porter Stemming Error Analysis

from nltk.stem import PorterStemmer
import pandas as pd
import re

ps = PorterStemmer()

# ERROR IN ORIGINAL CODE:
# ps.stem() accepts ONE word, but data["Text"] contains a complete sentence.
# Therefore, the sentence must first be tokenized into words.

data = pd.DataFrame({
    "Text": [
        "The organization is organizing a new business project.",
        "The organizer announced the development of new technology.",
        "The government is developing new policies.",
        "The companies are connected with international organizations.",
        "The manager is managing the business operations."
    ]
})

# Check column names
print("Columns:", data.columns.tolist())

# Correct column name if the dataset uses "text" instead of "Text"
text_col = "Text" if "Text" in data.columns else "text"

# Apply Porter Stemmer word by word
def stem_text(text):
    words = re.findall(r"[A-Za-z]+", str(text).lower())
    return " ".join(ps.stem(word) for word in words)

data["Processed"] = data[text_col].apply(stem_text)

# 1. Compare original and stemmed text
print("\nORIGINAL WORDS -> STEMMED WORDS")
print("-" * 60)

for i in range(min(10, len(data))):
    print("\nOriginal :", data[text_col].iloc[i])
    print("Stemmed  :", data["Processed"].iloc[i])

# 2. Analyze individual words
words = set()

for text in data[text_col].head(1000):
    words.update(re.findall(r"[A-Za-z]+", str(text).lower()))

print("\n\nWORD -> PORTER STEM")
print("-" * 40)

for word in sorted(words)[:50]:
    print(word, "->", ps.stem(word))

# 3. At least 20 common stemming cases
test_words = [
    "organization", "organizer", "organizing", "organized",
    "political", "politician", "politics", "easily",
    "studies", "studying", "studied", "relational",
    "national", "nationality", "connection", "connected",
    "development", "developing", "developer", "management",
    "manager", "computers", "computerized", "business"
]

print("\n\n20+ STEMMING CASES")
print("-" * 60)

for word in test_words:
    print(word, "->", ps.stem(word))

# 4. Morphological classification
print("\n\nMORPHOLOGICAL ANALYSIS")
print("-" * 70)

cases = {
    "studies": "Inflectional",
    "studying": "Inflectional",
    "studied": "Inflectional",
    "computers": "Inflectional",
    "organizing": "Inflectional",
    "organized": "Inflectional",
    "developing": "Inflectional",
    "connected": "Inflectional",
    "political": "Derivational",
    "politician": "Derivational",
    "nationality": "Derivational",
    "organization": "Derivational",
    "organizer": "Derivational",
    "relational": "Derivational",
    "connection": "Derivational",
    "development": "Derivational",
    "developer": "Derivational",
    "management": "Derivational",
    "manager": "Derivational",
    "computerized": "Derivational",
    "business": "Derivational"
}

for word, category in cases.items():
    print(f"{word:20} -> {ps.stem(word):15} -> {category}")

print("\n\nERRORS IN ORIGINAL PROGRAM")
print("1. ps.stem() cannot process a complete sentence.")
print("2. The text must be tokenized before stemming.")
print("3. The column name 'Text' may not match the dataset.")
print("4. Missing values can cause errors, so str() is used.")
print("5. Porter stemming is a word-reduction algorithm, not")
print("   a complete morphological analyzer.")

print("\nCONCLUSION")
print("Porter stemming is useful for reducing related word forms,")
print("but it may remove derivational information and produce stems")
print("that are not valid English words. For BBC news classification,")
print("lemmatization can preserve more linguistic information.")