# Question 3: Word Sense Disambiguation

search_data = [
    {
        "query": "Apple accessories",
        "word": "Apple",
        "senses": ["Fruit", "Technology Brand"],
        "clicked": "iPhone Charger",
        "correct": "Technology Brand"
    },
    {
        "query": "Mouse wireless",
        "word": "Mouse",
        "senses": ["Animal", "Computer Device"],
        "clicked": "Bluetooth Mouse",
        "correct": "Computer Device"
    },
    {
        "query": "Java tutorial",
        "word": "Java",
        "senses": ["Island", "Programming Language"],
        "clicked": "Coding Lessons",
        "correct": "Programming Language"
    },
    {
        "query": "Python course",
        "word": "Python",
        "senses": ["Snake", "Programming Language"],
        "clicked": "Software Development Training",
        "correct": "Programming Language"
    }
]

print("WORD SENSE DISAMBIGUATION")
print("-" * 70)

correct_count = 0

for item in search_data:

    print("\nQuery:", item["query"])
    print("Ambiguous Word:", item["word"])
    print("Possible Senses:", ", ".join(item["senses"]))
    print("Clicked Result:", item["clicked"])

    # Context-based sense identification
    if "iPhone" in item["clicked"]:
        predicted = "Technology Brand"
    elif "Mouse" in item["clicked"]:
        predicted = "Computer Device"
    elif "Coding" in item["clicked"]:
        predicted = "Programming Language"
    elif "Software" in item["clicked"]:
        predicted = "Programming Language"
    else:
        predicted = "Unknown"

    print("Predicted Sense:", predicted)
    print("Expected Sense:", item["correct"])

    if predicted == item["correct"]:
        print("Status: Correct")
        correct_count += 1
    else:
        print("Status: Incorrect")

accuracy = correct_count / len(search_data) * 100

print("\n" + "-" * 70)
print("Correct Sense Predictions:", correct_count)
print("Total Queries:", len(search_data))
print("WSD Accuracy:", accuracy, "%")

print("\nSemantic Cues Used:")
print("1. iPhone Charger -> Technology Brand")
print("2. Bluetooth Mouse -> Computer Device")
print("3. Coding Lessons -> Programming Language")
print("4. Software Development Training -> Programming Language")

print("\nConclusion:")
print("Contextual information helps the search engine select")
print("the correct meaning of ambiguous words.")
?
