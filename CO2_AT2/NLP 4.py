def parse_word(word):

    rules = {

        "activate": {
            "prefix": "None",
            "root": "active",
            "suffix": "-ate",
            "sequence": "active -> activate (-ate: adjective -> verb)",
            "class_change": "Adjective -> Verb"
        },

        "activation": {
            "prefix": "None",
            "root": "active",
            "suffix": "-ate + -ion",
            "sequence": "active -> activate -> activation (-ate: adjective -> verb, -ion: verb -> noun)",
            "class_change": "Adjective -> Verb -> Noun"
        },

        "reactivation": {
            "prefix": "re-",
            "root": "active",
            "suffix": "-ate + -ion",
            "sequence": "active -> activate -> activation -> reactivation (re-: repetition prefix added to noun)",
            "class_change": "Adjective -> Verb -> Noun (+ 're-' repetition meaning)"
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
        "Derivational Sequence": entry["sequence"],
        "Word-Class Change": entry["class_change"],
        "Normalized Base Form": entry["root"]
    }


if __name__ == "__main__":

    words = [
        "activate",
        "activation",
        "reactivation"
    ]

    results = [parse_word(word) for word in words]

    print(
        f'{"Word":<15}'
        f'{"Prefix":<8}'
        f'{"Root":<10}'
        f'{"Suffix":<15}'
        f'{"Class Change"}'
    )

    print("-" * 90)

    for result in results:

        print(
            f'{result["Original Word"]:<15}'
            f'{result["Prefix"]:<8}'
            f'{result["Root Word"]:<10}'
            f'{result["Suffix"]:<15}'
            f'{result["Word-Class Change"]}'
        )

    print("\nStructured Report for Document Classification / Semantic Indexing:")

    for result in results:

        print("-" * 60)

        for key, value in result.items():
            print(f"{key:<26}: {value}")

    print("\nFinal Parsed Representation:")

    for result in results:

        prefix = "" if result["Prefix"] == "None" else result["Prefix"]

        print(
            f'{result["Original Word"]:<15} -> '
            f'{prefix}[{result["Root Word"]}]'
            f'+{result["Suffix"]} '
            f'(normalized: {result["Normalized Base Form"]})'
        )