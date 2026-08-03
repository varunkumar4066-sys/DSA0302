import re

text = "The cat is running quickly"

words = text.split()

print("Text:")
print(text)

print("\nPOS Tags:")

for word in words:
    if re.match(r".*ing$", word):
        tag = "VBG"
    elif re.match(r".*ly$", word):
        tag = "RB"
    elif word.lower() in ["the", "a", "an"]:
        tag = "DT"
    else:
        tag = "NN"

    print(word, "->", tag)