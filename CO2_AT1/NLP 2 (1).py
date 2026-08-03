words = ["unhappy", "happiness", "happily"]

print("{:<12}{:<10}{:<10}{:<10}{:<15}{:<12}".format(
    "Word","Prefix","Root","Suffix","Type","Normalized"))

for word in words:

    if word == "unhappy":
        prefix = "un"
        root = "happy"
        suffix = "-"
        t = "Derivational"

    elif word == "happiness":
        prefix = "-"
        root = "happy"
        suffix = "ness"
        t = "Derivational"

    elif word == "happily":
        prefix = "-"
        root = "happy"
        suffix = "ly"
        t = "Derivational"

    print("{:<12}{:<10}{:<10}{:<10}{:<15}{:<12}".format(
        word,prefix,root,suffix,t,root))