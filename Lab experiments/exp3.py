import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Download required resources (only first time)
nltk.download('wordnet')
nltk.download('omw-1.4')

ps = PorterStemmer()
lemmatizer = WordNetLemmatizer()

words = [
    "running",
    "playing",
    "studies",
    "better",
    "cars",
    "children"
]

print("Morphological Analysis")
print("-" * 40)

for word in words:
    stem = ps.stem(word)
    lemma = lemmatizer.lemmatize(word)

    print("Word       :", word)
    print("Stem       :", stem)
    print("Lemma      :", lemma)
    print("-" * 40)