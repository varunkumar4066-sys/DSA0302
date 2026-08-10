import re
from collections import Counter

# ---------------------------------------------------
# TRAINING CORPUS
# ---------------------------------------------------

corpus = """
The student is reading a book.
The student is writing an assignment.
The student is learning Python.
The student is studying natural language processing.
The teacher is explaining the lesson.
The teacher is helping the student.
The student likes machine learning.
The student likes computer science.
The student works on a project.
The student completes the assignment.
The teacher gives the student a book.
The student reads the book every day.
"""

# ---------------------------------------------------
# PREPROCESSING
# ---------------------------------------------------

def preprocess(text):
    text = text.lower()
    sentences = re.split(r'[.!?]+', text)

    tokenized_sentences = []

    for sentence in sentences:
        words = re.findall(r'\b[a-z]+\b', sentence)

        if words:
            words = ['<s>'] + words + ['</s>']
            tokenized_sentences.append(words)

    return tokenized_sentences


sentences = preprocess(corpus)

# ---------------------------------------------------
# CREATE N-GRAM COUNTS
# ---------------------------------------------------

def create_ngrams(sentences):
    unigram = Counter()
    bigram = Counter()
    trigram = Counter()

    for sentence in sentences:

        for word in sentence:
            unigram[word] += 1

        for i in range(len(sentence) - 1):
            bigram[(sentence[i], sentence[i + 1])] += 1

        for i in range(len(sentence) - 2):
            trigram[
                (sentence[i], sentence[i + 1], sentence[i + 2])
            ] += 1

    return unigram, bigram, trigram


unigram, bigram, trigram = create_ngrams(sentences)

# ---------------------------------------------------
# PROBABILITY FUNCTIONS
# ---------------------------------------------------

def unigram_probability(word):
    return unigram[word] / sum(unigram.values())


def bigram_probability(w1, w2):
    if unigram[w1] == 0:
        return 0

    return bigram[(w1, w2)] / unigram[w1]


def trigram_probability(w1, w2, w3):
    if bigram[(w1, w2)] == 0:
        return 0

    return trigram[(w1, w2, w3)] / bigram[(w1, w2)]


# ---------------------------------------------------
# DISPLAY COUNTS
# ---------------------------------------------------

def display_counts(n):

    if n == 1:
        print("\n--- UNIGRAM COUNTS ---")
        for word, count in unigram.items():
            print(word, ":", count)

    elif n == 2:
        print("\n--- BIGRAM COUNTS ---")
        for words, count in bigram.items():
            print(words, ":", count)

    elif n == 3:
        print("\n--- TRIGRAM COUNTS ---")
        for words, count in trigram.items():
            print(words, ":", count)


# ---------------------------------------------------
# DISPLAY PROBABILITIES
# ---------------------------------------------------

def display_probabilities(n):

    print("\n--- PROBABILITIES ---")

    if n == 1:

        total = sum(unigram.values())

        for word, count in unigram.items():
            print(
                word,
                "Count =", count,
                "Probability =",
                round(count / total, 4)
            )

    elif n == 2:

        for (w1, w2), count in bigram.items():
            probability = bigram_probability(w1, w2)

            print(
                (w1, w2),
                "Count =", count,
                "Probability =",
                round(probability, 4)
            )

    elif n == 3:

        for (w1, w2, w3), count in trigram.items():
            probability = trigram_probability(w1, w2, w3)

            print(
                (w1, w2, w3),
                "Count =", count,
                "Probability =",
                round(probability, 4)
            )


# ---------------------------------------------------
# NEXT WORD PREDICTION
# ---------------------------------------------------

def predict_next_words(text, n):

    words = re.findall(r'\b[a-z]+\b', text.lower())

    if n == 1:

        candidates = []

        for word in unigram:
            candidates.append(
                (word, unigram_probability(word))
            )

    elif n == 2:

        if len(words) == 0:
            return []

        previous = words[-1]

        candidates = []

        for word in unigram:

            probability = bigram_probability(previous, word)

            if probability > 0:
                candidates.append((word, probability))

    else:

        if len(words) < 2:
            return []

        w1 = words[-2]
        w2 = words[-1]

        candidates = []

        for word in unigram:

            probability = trigram_probability(w1, w2, word)

            if probability > 0:
                candidates.append((word, probability))

    candidates.sort(key=lambda x: x[1], reverse=True)

    return candidates[:5]


# ---------------------------------------------------
# TEST UNSEEN N-GRAM
# ---------------------------------------------------

def test_unseen():

    print("\n--- UNSEEN N-GRAM TEST ---")

    print(
        "P(bigram | student beautiful) =",
        bigram_probability("student", "beautiful")
    )

    print(
        "P(trigram | student is beautiful) =",
        trigram_probability("student", "is", "beautiful")
    )

    print("\nBecause these N-grams are not present in the corpus,")
    print("their probability is 0.")


# ---------------------------------------------------
# EVALUATION
# ---------------------------------------------------

def evaluate():

    test_sentences = [
        "the student is",
        "the teacher is",
        "the student likes"
    ]

    print("\n--- PREDICTION EVALUATION ---")

    for text in test_sentences:

        predictions = predict_next_words(text, 2)

        print("\nInput:", text)

        if predictions:
            print("Predicted next words:")

            for word, probability in predictions:
                print(
                    word,
                    "->",
                    round(probability, 4)
                )
        else:
            print("No prediction available.")


# ---------------------------------------------------
# MAIN PROGRAM
# ---------------------------------------------------

while True:

    print("\n================================")
    print("     N-GRAM LANGUAGE MODEL")
    print("================================")
    print("1. Unigram")
    print("2. Bigram")
    print("3. Trigram")
    print("4. Predict next word")
    print("5. Test unseen N-gram")
    print("6. Evaluate model")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice in ["1", "2", "3"]:

        n = int(choice)

        display_counts(n)
        display_probabilities(n)

    elif choice == "4":

        n = int(input("Enter N (1, 2 or 3): "))

        text = input("Enter incomplete sentence: ")

        predictions = predict_next_words(text, n)

        print("\nTop-5 predictions:")

        if predictions:
            for word, probability in predictions:
                print(
                    word,
                    "-> Probability:",
                    round(probability, 4)
                )
        else:
            print("No prediction found.")

    elif choice == "5":
        test_unseen()

    elif choice == "6":
        evaluate()

    elif choice == "7":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")