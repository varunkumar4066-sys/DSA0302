from nltk.wsd import lesk
from nltk.tokenize import word_tokenize

text = "I went to the bank to deposit money."

words = word_tokenize(text)

word = "bank"

sense = lesk(words, word)

print("Text:")
print(text)

print("\nWord:", word)

if sense:
    print("Meaning:", sense.definition())
else:
    print("Meaning not found.")