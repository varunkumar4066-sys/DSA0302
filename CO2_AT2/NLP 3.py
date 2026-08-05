def analyze_word(word):

    rules = {

        "govern": {
            "root": "govern",
            "affixes": "None (base form)",
            "level": 0,
            "pos": "Verb"
        },

        "government": {
            "root": "govern",
            "affixes": "-ment",
            "level": 1,
            "pos": "Noun (institution / act of governing)"
        },

        "governance": {
            "root": "govern",
            "affixes": "-ance",
            "level": 1,
            "pos": "Noun (system / process of governing)"
        }

    }

    entry = rules.get(word.lower())

    if not entry:
        return None

    return {
        "Original Word": word,
        "Root Form": entry["root"],
        "Detected Affix(es)": entry["affixes"],
        "Derivational Level": entry["level"],
        "Part of Speech": entry["pos"],
        "Normalized Representation": entry["root"]
    }


if __name__ == "__main__":

    words = [
        "govern",
        "government",
        "governance"
    ]

    results = [analyze_word(word) for word in words]

    print(
        f'{"Word":<14}'
        f'{"Root":<10}'
        f'{"Affix(es)":<18}'
        f'{"Deriv.Lvl":<12}'
        f'{"POS"}'
    )

    print("-" * 80)

    for result in results:

        print(
            f'{result["Original Word"]:<14}'
            f'{result["Root Form"]:<10}'
            f'{result["Detected Affix(es)"]:<18}'
            f'{result["Derivational Level"]:<12}'
            f'{result["Part of Speech"]}'
        )

    print("\nStructured Output for Topic Modeling / Clustering:")

    for result in results:

        print("-" * 60)

        for key, value in result.items():
            print(f"{key:<28}: {value}")

    cluster = {}

    for result in results:
        cluster.setdefault(
            result["Normalized Representation"], []
        ).append(result["Original Word"])

    print("\nFinal Cluster (Normalized -> Members):")

    for norm, members in cluster.items():
        print(f'"{norm}" -> {members}')