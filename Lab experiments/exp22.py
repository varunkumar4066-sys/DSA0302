"""
Experiment 2: Reference Resolution (Coreference Resolution)
-------------------------------------------------------------
Given a short text, resolve pronouns (he, she, it, they, him, her, them,
his, her, its, their) to their most likely antecedent noun phrase, using a
rule-based (Hobbs-style, simplified) heuristic:

  1. Split text into sentences and tokenize.
  2. Extract candidate antecedents = proper nouns / definite noun phrases
     seen so far, tagged with a simple gender/number profile.
  3. For each pronoun, scan backwards through the candidate list and pick
     the closest candidate whose gender/number agrees with the pronoun.
  4. Print the resolved text and a mapping table.

No external NLP libraries required (pure Python / regex).
"""

import re

PRONOUNS = {
    "he": "male_sg", "him": "male_sg", "his": "male_sg",
    "she": "female_sg", "her": "female_sg", "hers": "female_sg",
    "it": "neutral_sg", "its": "neutral_sg",
    "they": "plural", "them": "plural", "their": "plural", "theirs": "plural",
}

# Minimal gender knowledge base for candidate nouns/names used in the demo text.
GENDER_KB = {
    "raj": "male_sg", "arjun": "male_sg", "mr. sharma": "male_sg", "he": "male_sg",
    "priya": "female_sg", "meera": "female_sg", "ms. iyer": "female_sg",
    "company": "neutral_sg", "robot": "neutral_sg", "laptop": "neutral_sg",
    "the company": "neutral_sg", "a robot": "neutral_sg", "a laptop": "neutral_sg",
    "laptop": "neutral_sg",
    "team": "plural", "students": "plural", "engineers": "plural",
    "the team": "plural",
}


def split_sentences(text):
    return [s.strip() for s in re.split(r'(?<=[.!?])\s+', text.strip()) if s.strip()]


def tokenize(sentence):
    return re.findall(r"[A-Za-z']+|[.,!?]", sentence)


def guess_gender(phrase):
    """Look up gender/number profile for a candidate noun phrase, falling
    back to the head (last) word of the phrase if the full phrase is not
    in the knowledge base."""
    key = phrase.lower()
    if key in GENDER_KB:
        return GENDER_KB[key]
    head = key.split()[-1]
    if head in GENDER_KB:
        return GENDER_KB[head]
    if head.endswith("s"):
        return "plural"
    return "neutral_sg"


KNOWN_ADJECTIVES = {"new", "old", "young", "beautiful", "wooden", "quick",
                     "brown", "lazy", "innovative", "fast", "popular"}


def extract_candidates_with_positions(tokens):
    """
    Candidate antecedents = capitalized proper nouns, or definite/indefinite
    noun phrases ('the X' / 'a X'). Returns list of (end_index, phrase),
    where end_index is the token index right after the phrase (so a pronoun
    can only be resolved to candidates that appeared strictly before it).
    """
    candidates = []
    i = 0
    while i < len(tokens):
        tok = tokens[i]
        low = tok.lower()
        if low in ("the", "a", "an") and i + 1 < len(tokens) and tokens[i + 1].isalpha():
            # Det (Adj)? Noun: if the word right after the article is a known
            # adjective, the noun phrase extends one more word (its head noun).
            j = i + 1
            words = [tokens[j]]
            if tokens[j].lower() in KNOWN_ADJECTIVES and j + 1 < len(tokens) and tokens[j + 1].isalpha():
                j += 1
                words.append(tokens[j])
            head = words[-1]
            candidates.append((j + 1, f"{low} {head}"))
            i = j + 1
            continue
        if tok[0:1].isupper() and tok.isalpha() and low not in PRONOUNS:
            candidates.append((i + 1, tok))
        i += 1
    return candidates


def resolve_references(text):
    sentences = split_sentences(text)
    all_tokens = []
    for s in sentences:
        all_tokens.extend(tokenize(s))

    candidates = extract_candidates_with_positions(all_tokens)
    resolutions = []
    output_tokens = []

    for idx, tok in enumerate(all_tokens):
        lower = tok.lower()
        if lower in PRONOUNS:
            needed_profile = PRONOUNS[lower]
            antecedent = None
            # scan backwards through candidates that appeared strictly before this pronoun
            for end_idx, cand in reversed(candidates):
                if end_idx <= idx and guess_gender(cand) == needed_profile:
                    antecedent = cand
                    break
            if antecedent:
                resolutions.append((tok, antecedent))
                output_tokens.append(f"{tok}[{antecedent}]")
            else:
                output_tokens.append(tok)
        else:
            output_tokens.append(tok)

    resolved_text = " ".join(output_tokens)
    resolved_text = re.sub(r"\s+([.,!?])", r"\1", resolved_text)
    return resolved_text, resolutions


if __name__ == "__main__":
    print("=" * 70)
    print(" EXPERIMENT 2: REFERENCE RESOLUTION ")
    print("=" * 70)

    texts = [
        "Raj bought a new laptop. He was very happy with it because it was fast.",
        "Priya met Arjun at the office. She told him that the team had "
        "finished their project ahead of schedule.",
        "The company launched a robot last year. It quickly became "
        "popular because its design was innovative.",
    ]

    for text in texts:
        print(f"\nOriginal Text : {text}")
        resolved, mapping = resolve_references(text)
        print(f"Resolved Text : {resolved}")
        print("Coreference Mapping:")
        if mapping:
            for pron, ante in mapping:
                print(f"   '{pron}'  ->  '{ante}'")
        else:
            print("   (no pronouns resolved)")
        print("-" * 70)
