# Question 3 – Stemming and News Article Classification

import re
import nltk
from datasets import load_dataset
from nltk.stem import PorterStemmer, WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

nltk.download("wordnet", quiet=True)
nltk.download("omw-1.4", quiet=True)

# 1. Load AG News Dataset
data = load_dataset("fancyzhx/ag_news")

train_text = data["train"]["text"][:5000]
train_y = data["train"]["label"][:5000]

test_text = data["test"]["text"][:1000]
test_y = data["test"]["label"][:1000]

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

# 2. Preprocessing methods
def words(text):
    return re.findall(r"[a-z]+", text.lower())

def no_stemming(text):
    return " ".join(words(text))

def stemming(text):
    return " ".join(stemmer.stem(w) for w in words(text))

def lemmatizing(text):
    return " ".join(lemmatizer.lemmatize(w) for w in words(text))

# 3. Show Porter Stemmer errors
test_words = [
    "organization", "organizer", "organizing",
    "organized", "organization's"
]

print("Porter Stemmer Results:")
for w in test_words:
    print(w, "->", stemmer.stem(w))

# 4. Compare three preprocessing methods
methods = {
    "Without Stemming": (no_stemming, False),
    "Porter Stemming": (stemming, False),
    "Lemmatization": (lemmatizing, False)
}

for name, (func, _) in methods.items():

    X_train_text = [func(x) for x in train_text]
    X_test_text = [func(x) for x in test_text]

    vectorizer = TfidfVectorizer(max_features=10000)
    X_train = vectorizer.fit_transform(X_train_text)
    X_test = vectorizer.transform(X_test_text)

    model = LogisticRegression(max_iter=300)
    model.fit(X_train, train_y)

    pred = model.predict(X_test)

    print("\n---", name, "---")
    print("Accuracy:", round(accuracy_score(test_y, pred) * 100, 2), "%")
    print("Confusion Matrix:")
    print(confusion_matrix(test_y, pred))

# 5. Conclusion
print("\nConclusion:")
print("Porter stemming can reduce different words to similar stems")
print("and may remove useful semantic information.")
print("Lemmatization uses valid word forms and usually preserves")
print("more meaning, so it can be better for text classification.")
print("The best method is the one giving the highest test accuracy")
print("with the least loss of semantic information.")