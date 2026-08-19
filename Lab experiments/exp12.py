grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": [["the"]],
    "N": [["boy"], ["ball"]],
    "V": [["plays"]]
}

sentence = "I am from the US".split()


def earley_parse(words):
    chart = [[] for _ in range(len(words) + 1)]

    chart[0].append(("S", ["NP", "VP"], 0, 0))

    for i in range(len(words) + 1):
        changed = True

        while changed:
            changed = False

            for lhs, rule, dot, start in chart[i]:

                # Prediction
                if dot < len(rule) and rule[dot] in grammar:
                    symbol = rule[dot]

                    for new_rule in grammar[symbol]:
                        state = (symbol, new_rule, 0, i)

                        if state not in chart[i]:
                            chart[i].append(state)
                            changed = True

                # Completion
                elif dot == len(rule):
                    for p_lhs, p_rule, p_dot, p_start in chart[start]:
                        if p_dot < len(p_rule) and p_rule[p_dot] == lhs:
                            state = (p_lhs, p_rule, p_dot + 1, p_start)

                            if state not in chart[i]:
                                chart[i].append(state)
                                changed = True

        # Scanning
        if i < len(words):
            for lhs, rule, dot, start in chart[i]:
                if dot < len(rule) and rule[dot] not in grammar:
                    if rule[dot] == words[i]:
                        chart[i + 1].append(
                            (lhs, rule, dot + 1, start)
                        )

    final_state = ("S", ["NP", "VP"], 2, 0)

    return final_state in chart[len(words)]


print("Sentence:", " ".join(sentence))

if earley_parse(sentence):
    print("Sentence Accepted")
else:
    print("Sentence Rejected")