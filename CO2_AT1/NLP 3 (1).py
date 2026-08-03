words = ["played", "player", "playing"]

print("{:<12}{:<10}{:<10}{:<15}{:<12}".format(
    "Word","Stem","Affix","Type","Normalized"))

for word in words:

    if word.endswith("ed"):
        stem = word[:-2]
        affix = "ed"
        t = "Inflectional"

    elif word.endswith("ing"):
        stem = word[:-3]
        affix = "ing"
        t = "Inflectional"

    elif word.endswith("er"):
        stem = word[:-2]
        affix = "er"
        t = "Derivational"

    print("{:<12}{:<10}{:<10}{:<15}{:<12}".format(
        word,stem,affix,t,stem))