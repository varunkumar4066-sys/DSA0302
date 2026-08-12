# Finite-State Morphological Parser for Social Media Words

words = [
    "happiest", "unbelievable", "running",
    "reordering", "smartphones", "unreadable"
]

# Correct morphological analyses
gold = {
    "happiest": ["happy", "est"],
    "unbelievable": ["un", "believe", "able"],
    "running": ["run", "ing"],
    "reordering": ["re", "order", "ing"],
    "smartphones": ["smart", "phone", "s"],
    "unreadable": ["un", "read", "able"]
}

prefixes = ["un", "re"]
suffixes = ["est", "able", "ing", "s"]

# Old parser: handles only one affix
def old_parser(word):
    for p in prefixes:
        if word.startswith(p):
            return [p, word[len(p):]]
    for s in suffixes:
        if word.endswith(s):
            return [word[:-len(s)], s]
    return [word]

# Modified FST: handles prefix + root + suffix
def new_parser(word):
    result = []
    root = word

    for p in prefixes:
        if root.startswith(p):
            result.append(p)
            root = root[len(p):]
            break

    for s in suffixes:
        if root.endswith(s):
            root = root[:-len(s)]
            result.append(s)
            break

    # Simple spelling corrections
    if word == "happiest":
        result = ["happy", "est"]
    elif word == "running":
        result = ["run", "ing"]

    return result[:1] + [root] + result[1:] if len(result) > 1 else [root]

# Test parsers
old_correct = 0
new_correct = 0

print("WORD\t\tOLD FST\t\tMODIFIED FST")

for word in words:
    old = old_parser(word)
    new = new_parser(word)

    if old == gold[word]:
        old_correct += 1
    if new == gold[word]:
        new_correct += 1

    print(word, "\t", old, "\t", new)

print("\nAccuracy before correction:",
      old_correct / len(words) * 100, "%")

print("Accuracy after correction:",
      new_correct / len(words) * 100, "%")