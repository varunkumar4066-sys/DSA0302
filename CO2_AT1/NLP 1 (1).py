words = ["connected", "connecting", "connection"]

print("{:<12}{:<12}{:<10}{:<15}{:<12}".format(
    "Word", "Root", "Suffix", "Type", "Normalized"))

for word in words:

    if word.endswith("ed"):
        root = word[:-2]
        suffix = "ed"
        t = "Inflectional"

    elif word.endswith("ing"):
        root = word[:-3]
        suffix = "ing"
        t = "Inflectional"

    elif word.endswith("ion"):
        root = "connect"
        suffix = "ion"
        t = "Derivational"

    else:
        root = word
        suffix = "-"
        t = "-"

    print("{:<12}{:<12}{:<10}{:<15}{:<12}".format(
        word, root, suffix, t, "connect"))