from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "Python is used for machine learning",
    "Natural language processing uses Python",
    "Machine learning is useful in data science"
]

query = "Python machine learning"

vectorizer = TfidfVectorizer()

vectors = vectorizer.fit_transform(documents + [query])

scores = cosine_similarity(vectors[-1], vectors[:-1])[0]

print("Query:", query)

print("\nDocument Ranking:")

ranking = sorted(
    enumerate(scores),
    key=lambda x: x[1],
    reverse=True
)

for index, score in ranking:
    print("Document", index + 1, "->", round(score, 2))
    print(documents[index])