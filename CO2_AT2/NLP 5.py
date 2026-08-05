def analyze_word(word):

    rules = {

        "create": {
            "suffix": "None (base form)",
            "root": "create",
            "category": "Base form (infinitive / present tense, all persons except 3rd singular)"
        },

        "creates": {
            "suffix": "-s",
            "root": "create",
            "category": "Third-person singular present tense"
        },

        "creating": {
            "suffix": "-ing",
            "root": "create",
            "category": "Present participle / gerund (continuous aspect)"
        }

    }

    entry = rules.get(word.lower())

    if not entry:
        return None

    return {
        "Original Word": word,
        "Identified Suffix": entry["suffix"],
        "Grammatical Category": entry["category"],
        "Extracted Root": entry["root"],
        "Normalized Base Form": entry["root"],
        "Final Normalized Representation": entry["root"]
    }


if __name__ == "__main__":

    words = [
        "create",
        "creates",
        "creating"
    ]

    results = [analyze_word(word) for word in words]

    print(
        f'{"Word":<12}'
        f'{"Suffix":<18}'
        f'{"Root":<10}'
        f'{"Grammatical Category"}'
    )

    print("-" * 90)

    for result in results:

        print(
            f'{result["Original Word"]:<12}'
            f'{result["Identified Suffix"]:<18}'
            f'{result["Extracted Root"]:<10}'
            f'{result["Grammatical Category"]}'
        )

    print("\nStructured Output for Search Optimization / Information Retrieval:")

    for result in results:

        print("-" * 60)

        for key, value in result.items():
            print(f"{key:<32}: {value}")

    group = {}

    for result in results:
        group.setdefault(
            result["Normalized Base Form"], []
        ).append(result["Original Word"])

    print("\nNormalization Group (Base Form -> Variants Mapped):")

    for base, members in group.items():
        print(f'"{base}" <= {members}')