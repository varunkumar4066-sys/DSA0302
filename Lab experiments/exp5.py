from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["playing", "studies", "running", "walking", "happiness"]

print("Original Word -> Stemmed Word")

for word in words:
    print(word, "->", ps.stem(word))