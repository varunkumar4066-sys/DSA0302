"""
Experiment 3: Text Coherence Evaluation
------------------------------------------
Evaluate how coherent a given text is by measuring lexical/semantic
overlap between consecutive sentences.

Method:
  1. Split the text into sentences.
  2. Build TF-IDF vectors for every sentence (scikit-learn).
  3. Compute cosine similarity between each pair of ADJACENT sentences
     -> this approximates local (sentence-to-sentence) coherence.
  4. Average the adjacent-pair similarities to get an overall coherence
     score in [0, 1], and classify the text as
     Highly Coherent / Moderately Coherent / Weakly Coherent / Incoherent.
"""

import re
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# A small suffix-stripping "stemmer" so that morphological variants of the
# same word (e.g. "computers"/"computer", "processing"/"process") count as
# lexical overlap between sentences.
def crude_stem(word):
    for suf in ("ational", "ization", "ing", "edly", "ies", "ed", "es", "s"):
        if word.endswith(suf) and len(word) - len(suf) >= 3:
            return word[: -len(suf)]
    return word


def split_sentences(text):
    return [s.strip() for s in re.split(r'(?<=[.!?])\s+', text.strip()) if s.strip()]


def stemmed_tokenizer(text):
    words = re.findall(r"[A-Za-z]+", text.lower())
    return [crude_stem(w) for w in words]


def coherence_score(text):
    sentences = split_sentences(text)
    if len(sentences) < 2:
        return sentences, [], 1.0, "Not enough sentences to evaluate."

    vectorizer = TfidfVectorizer(stop_words="english", tokenizer=stemmed_tokenizer,
                                  token_pattern=None)
    tfidf_matrix = vectorizer.fit_transform(sentences)
    sim_matrix = cosine_similarity(tfidf_matrix)

    pair_scores = []
    for i in range(len(sentences) - 1):
        score = sim_matrix[i, i + 1]
        pair_scores.append((i + 1, i + 2, round(float(score), 3)))

    avg_score = sum(s for _, _, s in pair_scores) / len(pair_scores)

    if avg_score >= 0.25:
        label = "Highly Coherent"
    elif avg_score >= 0.08:
        label = "Moderately Coherent"
    elif avg_score >= 0.02:
        label = "Weakly Coherent"
    else:
        label = "Incoherent"

    return sentences, pair_scores, round(avg_score, 3), label


def evaluate_and_print(text):
    print(f"Text:\n  {text}\n")
    sentences, pair_scores, avg_score, label = coherence_score(text)

    print("Sentences:")
    for i, s in enumerate(sentences, 1):
        print(f"  [{i}] {s}")

    print("\nAdjacent-Sentence Cosine Similarities:")
    for a, b, score in pair_scores:
        print(f"  Sentence {a} <-> Sentence {b} : {score}")

    print(f"\nOverall Coherence Score : {avg_score}")
    print(f"Coherence Verdict       : {label}")
    print("-" * 70)


if __name__ == "__main__":
    print("=" * 70)
    print(" EXPERIMENT 3: TEXT COHERENCE EVALUATION ")
    print("=" * 70)

    coherent_text = (
        "Artificial intelligence is transforming the way computers "
        "understand human language. Natural language processing, a core "
        "branch of AI, enables machines to read and interpret text. "
        "Thanks to NLP, computers can now perform tasks such as "
        "translation, summarization, and sentiment analysis."
    )

    incoherent_text = (
        "The stock market rose sharply today. My cat enjoys sleeping on "
        "the windowsill in the afternoon sun. Quantum computers use "
        "qubits instead of classical bits. She bought three kilograms "
        "of mangoes from the local market."
    )

    print("\n### Sample 1: Expected to be COHERENT ###\n")
    evaluate_and_print(coherent_text)

    print("\n### Sample 2: Expected to be INCOHERENT ###\n")
    evaluate_and_print(incoherent_text)
