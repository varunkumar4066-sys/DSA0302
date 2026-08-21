
import re

# ----------------------------------------------------------------------
# 1. Small hand-built lexicon (word -> POS tag)
# ----------------------------------------------------------------------
LEXICON = {
    "the": "DT", "a": "DT", "an": "DT", "this": "DT", "that": "DT",
    "quick": "JJ", "brown": "JJ", "lazy": "JJ", "old": "JJ", "wooden": "JJ",
    "beautiful": "JJ", "young": "JJ", "small": "JJ", "large": "JJ",
    "fox": "NN", "dog": "NN", "man": "NN", "woman": "NN", "table": "NN",
    "book": "NN", "river": "NN", "bank": "NN", "boy": "NN", "girl": "NN",
    "scientist": "NN", "computer": "NN", "program": "NN", "language": "NN",
    "sentence": "NN", "meaning": "NN", "bridge": "NN", "city": "NN",
    "jumps": "VBZ", "jumped": "VBD", "sat": "VBD", "reads": "VBZ",
    "wrote": "VBD", "built": "VBD", "crossed": "VBD", "walked": "VBD",
    "over": "IN", "on": "IN", "near": "IN", "across": "IN", "in": "IN",
    "and": "CC", "of": "IN", "with": "IN",
}

# ----------------------------------------------------------------------
# 2. Rule-based semantic dictionary (gloss / "meaning") for noun heads
# ----------------------------------------------------------------------
GLOSSARY = {
    "fox": "a small carnivorous mammal with a bushy tail, known for cunning.",
    "dog": "a domesticated four-legged animal often kept as a pet or for work.",
    "man": "an adult human male.",
    "woman": "an adult human female.",
    "table": "a piece of furniture with a flat top and legs, used for eating/working.",
    "book": "a set of printed or written pages bound together, meant for reading.",
    "river": "a large natural stream of water flowing towards a sea or lake.",
    "bank": "the land alongside a river, OR a financial institution (context-dependent).",
    "boy": "a young male human.",
    "girl": "a young female human.",
    "scientist": "a person who studies or has expert knowledge of a science.",
    "computer": "an electronic device that processes data according to instructions.",
    "program": "a set of coded instructions that a computer can execute.",
    "language": "a system of communication used by humans, spoken or written.",
    "sentence": "a set of words expressing a complete grammatical thought.",
    "meaning": "what is signified, indicated, or understood by something.",
    "bridge": "a structure built to span a physical obstacle, such as a river.",
    "city": "a large, permanent human settlement.",
}


def tokenize(sentence: str):
    """Split a sentence into word tokens (keeps contractions simple)."""
    return re.findall(r"[A-Za-z]+", sentence)


def pos_tag(tokens):
    """Assign a POS tag to every token using the lexicon, falling back to
    simple morphological (suffix) heuristics for unseen words."""
    tags = []
    for tok in tokens:
        low = tok.lower()
        if low in LEXICON:
            tags.append((tok, LEXICON[low]))
        elif low.endswith("ly"):
            tags.append((tok, "RB"))          # adverb
        elif low.endswith("ing"):
            tags.append((tok, "VBG"))         # verb, gerund
        elif low.endswith("ed"):
            tags.append((tok, "VBD"))         # verb, past tense
        elif low.endswith("s") and not low.endswith("ss"):
            tags.append((tok, "NNS"))         # plural noun (default guess)
        elif tok[0].isupper():
            tags.append((tok, "NNP"))         # proper noun
        else:
            tags.append((tok, "NN"))          # default: common noun
    return tags


def chunk_noun_phrases(tagged):
    """
    Apply the chunk grammar:  NP -> (DT)? (JJ)* (NN | NNS | NNP)+
    Implemented as a simple state-machine scan over the POS tag sequence
    (equivalent to applying a regex over the tag string).
    """
    tag_string = "".join(f"{t[1]}|" for t in tagged)
    pattern = re.compile(r"(DT\|)?(JJ\|)*((NN|NNS|NNP)\|)+")

    # Build parallel list so we can map regex span (in the tag string) back
    # to the token indices it covers.
    spans = []
    idx = 0
    positions = []
    for tok, tag in tagged:
        positions.append((idx, idx + len(tag) + 1))
        idx += len(tag) + 1

    noun_phrases = []
    for m in pattern.finditer(tag_string):
        if m.group(0) == "":
            continue
        start, end = m.span()
        words = [tagged[i][0] for i, (s, e) in enumerate(positions) if s >= start and e <= end]
        if words:
            noun_phrases.append(" ".join(words))
    return noun_phrases


def semantic_analysis(sentence: str):
    tokens = tokenize(sentence)
    tagged = pos_tag(tokens)
    nps = chunk_noun_phrases(tagged)

    print(f"Sentence : {sentence}")
    print(f"Tokens   : {tokens}")
    print(f"POS Tags : {tagged}")
    print("Noun Phrases & Meanings:")
    for np in nps:
        head = np.split()[-1].lower()
        gloss = GLOSSARY.get(head, "meaning not found in local glossary.")
        print(f"   - NP: '{np}'  ->  head noun: '{head}'  ->  meaning: {gloss}")
    print("-" * 70)
    return nps


if __name__ == "__main__":
    print("=" * 70)
    print(" EXPERIMENT 1: SYNTAX-DRIVEN SEMANTIC ANALYSIS ")
    print(" (Noun Phrase Extraction + Meaning Attachment) ")
    print("=" * 70)

    sample_sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "The old scientist wrote a beautiful program in a new language.",
        "A young boy crossed the wooden bridge near the river bank.",
    ]

    for sent in sample_sentences:
        semantic_analysis(sent)
