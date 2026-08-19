grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": [["the"]],
    "N": [["boy"], ["ball"]],
    "V": [["plays"]]
}

sentence = "the boy plays the ball".split()


def parse(symbol, words, position):
    if symbol not in grammar:
        if position < len(words) and symbol == words[position]:
            return position + 1
        return None

    for rule in grammar[symbol]:
        pos = position

        for part in rule:
            pos = parse(part, words, pos)

            if pos is None:
                break

        if pos is not None:
            return pos

    return None


result = parse("S", sentence, 0)

print("Sentence:", " ".join(sentence))

if result == len(sentence):
    print("Sentence Accepted")
else:
    print("Sentence Rejected")