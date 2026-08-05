
def morphological_process(word):
    """
    Decompose a word into root and affixes,
    classify as inflectional or derivational,
    and normalize it to a common indexing form.
    """

    rules = {
        "analyzing": {
            "root": "analyze",
            "affix": "-ing",
            "type": "Inflectional",
            "note": "Present participle / progressive form of the verb 'analyze'."
        },

        "analysis": {
            "root": "analyze",
            "affix": "-sis (noun-forming)",
            "type": "Derivational",
            "note": "Noun form derived from the verb 'analyze' (verb -> noun)."
        },

        "analytical": {
            "root": "analyze",
            "affix": "-tical (adj-forming)",
            "type": "Derivational",
            "note": "Adjective form derived from 'analysis/analyze' (noun/verb -> adjective)."
        }
    }

    entry = rules.get(word.lower())

    if not entry:
        return None

    normalized = "analyze"

    return {
        "Original Word": word,
        "Root": entry["root"],
        "Affix(es)": entry["affix"],
        "Transformation Type": entry["type"],
        "Semantic Note": entry["note"],
        "Normalized (Index) Form": normalized
    }


def generate_report(words):
    report = []

    for word in words:
        result = morphological_process(word)
        if result:
            report.append(result)

    return report


def print_report(report):

    header = f'{"Word":<14}{"Root":<12}{"Affix(es)":<26}{"Type":<15}{"Normalized":<12}'
    print(header)
    print("-" * len(header))

    for r in report:
        print(
            f'{r["Original Word"]:<14}'
            f'{r["Root"]:<12}'
            f'{r["Affix(es)"]:<26}'
            f'{r["Transformation Type"]:<15}'
            f'{r["Normalized (Index) Form"]:<12}'
        )

    print("\nDetailed Structured Report:")

    for r in report:
        print("-" * 60)
        for key, value in r.items():
            print(f"{key:<28}: {value}")


if __name__ == "__main__":

    input_words = [
        "analyzing",
        "analysis",
        "analytical"
    ]

    report = generate_report(input_words)

    print_report(report)

    print("\nIndexing Group -> Unified Representation:")

    groups = {}

    for r in report:
        groups.setdefault(
            r["Normalized (Index) Form"], []
        ).append(r["Original Word"])

    for norm, members in groups.items():
        print(f'"{norm}" <= {members}')