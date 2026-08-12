# Question 7 – Error Analysis of Morphological Feature Extraction

import time
from nltk.stem import PorterStemmer
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

stemmer = PorterStemmer()

# 1. Load a small real-world 20 Newsgroups dataset
categories = ["sci.space", "comp.graphics"]

train = fetch_20newsgroups(
    subset="train", categories=categories,
    remove=("headers", "footers", "quotes")
)

test = fetch_20newsgroups(
    subset="test", categories=categories,
    remove=("headers", "footers", "quotes")
)

# 2. Original pipeline: Vectorization -> Stemming
start = time.time()

vectorizer1 = CountVectorizer()
X_train1 = vectorizer1.fit_transform(train.data)
X_test1 = vectorizer1.transform(test.data)

# Stemming AFTER feature extraction (incorrect)
features = [
    stemmer.stem(word)
    for word in vectorizer1.get_feature_names_out()
]

model1 = LogisticRegression(max_iter=300)
model1.fit(X_train1, train.target)
pred1 = model1.predict(X_test1)

time1 = time.time() - start

print("ORIGINAL PIPELINE")
print("Vocabulary size:", len(vectorizer1.get_feature_names_out()))
print("Accuracy:", round(accuracy_score(test.target, pred1) * 100, 2), "%")
print("Time:", round(time1, 2), "seconds")

# 3. Correct pipeline: Stemming -> Vectorization
def stem_text(text):
    words = text.lower().split()
    return " ".join(stemmer.stem(w) for w in words)

start = time.time()

train_stemmed = [stem_text(text) for text in train.data]
test_stemmed = [stem_text(text) for text in test.data]

vectorizer2 = CountVectorizer()
X_train2 = vectorizer2.fit_transform(train_stemmed)
X_test2 = vectorizer2.transform(test_stemmed)

model2 = LogisticRegression(max_iter=300)
model2.fit(X_train2, train.target)
pred2 = model2.predict(X_test2)

time2 = time.time() - start

print("\nCORRECTED PIPELINE")
print("Vocabulary size:", len(vectorizer2.get_feature_names_out()))
print("Accuracy:", round(accuracy_score(test.target, pred2) * 100, 2), "%")
print("Time:", round(time2, 2), "seconds")

# 4. Compare vocabulary
print("\nCOMPARISON")
print("-" * 40)
print("Before correction:", len(vectorizer1.get_feature_names_out()))
print("After correction :", len(vectorizer2.get_feature_names_out()))
print("Accuracy before  :", round(accuracy_score(test.target, pred1) * 100, 2), "%")
print("Accuracy after   :", round(accuracy_score(test.target, pred2) * 100, 2), "%")
print("Time before      :", round(time1, 2), "seconds")
print("Time after       :", round(time2, 2), "seconds")

# 5. Demonstrate the original problem
documents = [
    "running runners runs",
    "studies studied studying",
    "organization organized organizer"
]

v = CountVectorizer()
v.fit(documents)

print("\nSTEMMING AFTER FEATURE EXTRACTION")
print("Original vocabulary:")
print(v.get_feature_names_out())

print("Stemmed feature names:")
print([stemmer.stem(w) for w in v.get_feature_names_out()])

print("\nCONCLUSION")
print("The original program extracts features before stemming.")
print("Therefore, different word forms already become separate")
print("features and stemming cannot merge their columns.")
print("The corrected pipeline stems the text before vectorization.")
print("This reduces redundant features and can improve NLP")
print("classification by making related word forms share features.")