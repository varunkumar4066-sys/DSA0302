
def parse_word(word):

    rules = {

        "disagree": {
            "prefix": "dis-",
            "root": "agree",
            "suffix": "None",
            "type": "Derivational (prefixation)",
            "semantic_effect": "Negation of the root meaning: 'agree' -> 'not agree' (opposite polarity, sentiment-reversing)."
        },

        "agreement": {
            "prefix": "None",
            "root": "agree",
            "suffix": "-ment",
            "type": "Derivational (verb -> noun)",
            "semantic_effect": "Converts the verb 'agree' into a noun denoting the state/result of agreeing (neutral polarity carried from root)."
        },

        "agreeable": {
            "prefix": "None",
            "root": "agree",
            "suffix": "-able",
            "type": "Derivational (verb -> adjective)",
            "semantic_effect": "Converts the verb 'agree' into an adjective meaning 'able/willing to agree' (positive polarity)."
        }

    }

    entry = rules.get(word.lower())

    if not entry:
        return None

    return {
        "Original Word": word,
        "Prefix": entry["prefix"],
        "Root Word": entry["root"],
        "Suffix": entry["suffix"],
        "Transformation Category": entry["type"],
        "Semantic Interpretation": entry["semantic_effect"],
        "Normalized Base Form": entry["root"]
    }


def sentiment_polarity(word):

    polarity = {
        "disagree": "Negative",
        "agreement": "Neutral/Positive",
        "agreeable": "Positive"
    }

    return polarity.get(word.lower(), "Unknown")


if __name__ == "__main__":

    words = [
        "disagree",
        "agreement",
        "agreeable"
    ]

    print(
        f'{"Word":<12}'
        f'{"Prefix":<8}'
        f'{"Root":<8}'
        f'{"Suffix":<9}'
        f'{"Category":<30}'
        f'{"Polarity"}'
    )

    print("-" * 95)

    results = []

    for word in words:

        result = parse_word(word)
        results.append(result)

        print(
            f'{result["Original Word"]:<12}'
            f'{result["Prefix"]:<8}'
            f'{result["Root Word"]:<8}'
            f'{result["Suffix"]:<9}'
            f'{result["Transformation Category"]:<30}'
            f'{sentiment_polarity(word)}'
        )

    print("\nComprehensive Output:")

    for result in results:

        print("-" * 60)

        for key, value in result.items():
            print(f"{key:<26}: {value}")

        print(f'{"Sentiment Polarity":<26}: {sentiment_polarity(result["Original Word"])}')