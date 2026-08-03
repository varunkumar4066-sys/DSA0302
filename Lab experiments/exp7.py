import nltk

text = "The boy is playing cricket in the ground."

words = nltk.word_tokenize(text)
tags = nltk.pos_tag(words)

print("Text:")
print(text)

print("\nPOS Tags:")
for word, tag in tags:
    print(word, "->", tag)