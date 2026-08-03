from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["relational", "relation", "relate"]

print("{:<12}{:<20}{:<15}".format(
    "Word","Intermediate","Final Stem"))

for word in words:

    if word.endswith("al"):
        inter = word[:-2]
    elif word.endswith("ion"):
        inter = word[:-3]
    elif word.endswith("ate"):
        inter = word[:-3]
    else:
        inter = word

    stem = ps.stem(word)

    print("{:<12}{:<20}{:<15}".format(
        word,inter,stem))