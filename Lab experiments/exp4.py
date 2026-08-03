words = ["cat", "bus", "box", "baby", "class"]

print("Singular -> Plural")

for word in words:
    if word.endswith("y"):
        plural = word[:-1] + "ies"
    elif word.endswith(("s", "x", "z")):
        plural = word + "es"
    else:
        plural = word + "s"

    print(word, "->", plural)