pos_dict = {
    "the": "DT",
    "boy": "NN",
    "plays": "VB",
    "cricket": "NN",
    "well": "RB"
}

text = "the boy plays cricket well"

words = text.split()

print("Text:")
print(text)

print("\nPOS Tags:")
for word in words:
    tag = pos_dict.get(word, "NN")
    print(word, "->", tag)