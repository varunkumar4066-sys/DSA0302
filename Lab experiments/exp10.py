text = "The boy is playing"

words = text.split()

tags = []

for word in words:
    tags.append([word, "NN"])

for tag in tags:
    if tag[0].lower() in ["the", "a", "an"]:
        tag[1] = "DT"
    elif tag[0].lower() == "is":
        tag[1] = "VBZ"
    elif tag[0].endswith("ing"):
        tag[1] = "VBG"

print("Text:")
print(text)

print("\nPOS Tags:")

for word, pos in tags:
    print(word, "->", pos)